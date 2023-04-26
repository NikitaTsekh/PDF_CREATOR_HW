from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse,FileResponse
from .models import ReplenismentEvent
from .Invoice_classes import InvoiceCreatorService
from datetime import datetime
# import json
# # Create your views here.
# @csrf_exempt

@api_view(['POST'])
def endpoint1(request):
    if request.method == 'POST':
        replenishment_id = request.data.get("replenishment_id")
        replenishment_event = ReplenismentEvent.objects.get(pk=replenishment_id)
        invoice_date = datetime.now().strftime('%d.%m.%Y')
        obj = InvoiceCreatorService(replenishment_event=replenishment_event,invoice_number='123',invoice_date=invoice_date)
        buffer = obj.create_pdf()
        buffer.seek(0)

        return FileResponse(buffer, as_attachment=True, filename='hello.pdf')

# @api_view(['POST'])
# def endpoint1(request):
#     if request.method == 'POST':
#         replenishment_id = request.data.get("replenishment_id")
#         replenishment_event = ReplenismentEvent.objects.get(pk=replenishment_id)
#         invoice_date = datetime.now().strftime('%d.%m.%Y')
#         obj = InvoiceCreatorService(replenishment_event=replenishment_event, invoice_number='123',
#                                     invoice_date=invoice_date)
#
#         response = HttpResponse(obj.create_pdf(), content_type='application/pdf')
#         response['Content-Disposition'] = 'attachment; filename=invoice.pdf'
#         return response  # return Response(data=replenishment_event.organization_name)



