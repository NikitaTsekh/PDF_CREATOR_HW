
import pdfkit
from dataclasses import dataclass
from decimal import Decimal
import io
from num2words import num2words
from datetime import datetime
from django.template import loader
from django.http import HttpResponse
from django.conf import settings


@dataclass()
class ReplenismentEvent():
    organization_name: str
    organization_legal_address: str
    organization_inn: str
    organization_kpp: str
    contract_number: str
    contract_date: datetime
    payment_sum_without_commission: Decimal
    commission_payment_sum: Decimal
    total: Decimal


@dataclass()
class InvoiceCreatorService:
    replenishment_event: ReplenismentEvent
    invoice_number: str
    invoice_date: datetime

    def create_pdf(self) -> io.BytesIO:

        # Define a function to handle the decimal part of the number
        def get_decimal_part(num, lang):
            dec_part = int(round(num * 100))
            if dec_part == 0:
                return '00 копеек'
            elif dec_part % 10 == 1 and dec_part != 11:
                return f"{dec_part:02d} копейка"
            elif dec_part % 10 in [2, 3, 4] and dec_part not in [12, 13, 14]:
                return f"{dec_part:02d} копейки"
            else:
                return f"{dec_part:02d} копеек"

        # Convert the integer part of the number to words
        int_part = int(self.replenishment_event.total)
        if int_part == 1000:
            int_part_words = 'одна тысяча'
        else:
            int_part_words = num2words(int_part, lang='ru').replace('-', ' ')

        # Get the decimal part of the number
        dec_part_words = get_decimal_part(self.replenishment_event.total - int_part, 'ru')

        # Check if the last digit of the integer part is 1, 2, 3 or 4
        last_digit = int_part % 10
        last_two_digits = int_part % 100
        if last_digit == 1 and last_two_digits != 11:
            ruble_word = 'рубль'
        elif last_digit in [2, 3, 4] and last_two_digits not in [12, 13, 14]:
            ruble_word = 'рубля'
        else:
            ruble_word = 'рублей'

        self.result_str = f"{int_part_words} {ruble_word} {dec_part_words}"

        # return self.result_str это затычка для теста

        context = {'invoice_number': self.invoice_number, 'invoice_date': self.invoice_date,
                   'organization_name': self.replenishment_event.organization_name,
                    'organization_legal_address': self.replenishment_event.organization_legal_address,
                    'organization_inn': self.replenishment_event.organization_inn,
                     'organization_kpp': self.replenishment_event.organization_kpp,
                     'contract_number': self.replenishment_event.contract_number,
                    'contract_date': self.replenishment_event.contract_date,
                    'payment_sum_without_commission': self.replenishment_event.payment_sum_without_commission,
                    'commission_payment_sum': self.replenishment_event.commission_payment_sum,
                    'total': self.replenishment_event.total, 'result_str': self.result_str}

        template = loader.get_template('invoice.html')
        output_text = template.render(context)

        #template_loader = jinja2.FileSystemLoader('./')
        # template_env = jinja2.Environment(loader=template_loader)
        #template = template_env.get_template('invoice.html')  # output_text = template.render(context)

        config = pdfkit.configuration(wkhtmltopdf='/usr/bin/wkhtmltopdf') #change at server
        pdfkit.from_string(output_text, 'invoice.pdf', configuration=config)
        pdf_bytes = pdfkit.from_string(output_text, output_path=False, configuration=config)
        pdf_io = io.BytesIO(pdf_bytes)
        return pdf_io

#
# if __name__ == '__main__':
#     megafon = ReplenismentEvent(organization_name='Мегафон',
#                                 organization_legal_address='127006, г.москва , пер. Оружейный, д. 41',
#                                 organization_inn='7812014560', organization_kpp='770701001', contract_number='1378А',
#                                 contract_date='05.08.2021,', payment_sum_without_commission=2000.00,
#                                 commission_payment_sum=200.00, total=2200.00)
#
#     invoice_service = InvoiceCreatorService(invoice_number="ЛК99", invoice_date='12.04.2026',
#                                             replenishment_event=megafon)
#
#     with open('output_invoice.pdf', 'wb') as f:
#         f.write(invoice_service.create_pdf().getvalue())
