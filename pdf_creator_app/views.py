from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from .models import ReplenismentEvent
from .Invoice_classes import InvoiceCreatorService
# import json
# # Create your views here.
# @csrf_exempt
@api_view(['POST'])
def endpoint1(request):
    if request.method == 'POST':
        replenishment_id = request.data.get("replenishment_id")
        replenishment_event = ReplenismentEvent.objects.get(pk=replenishment_id)

        obj = InvoiceCreatorService(replenishment_event=replenishment_event,invoice_number='123',invoice_date='24.04.2023')

        #return Response(data=obj.create_pdf())
        #return HttpResponse(data=obj.create_pdf())
        response = HttpResponse(obj.create_pdf(), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename=invoice.pdf'
        return response
        #return Response(data=replenishment_event.organization_name)

    # @api_view(['POST'])
    # def endpoint1(request):
    #     if request.method == 'POST':
    #         replenishment_id = request.data.get("replenishment_id")
    #         replenishment_event = ReplenismentEvent.objects.get(pk=replenishment_id)
    #
    #         return Response(data=replenishment_event.organization_name)

        # data = json.loads(request.body)
    #     my_model = ReplenismentEvent.objects.create(
    #         name=data['name'],
    #         age=data['age'],
    #     )
    #     response_data = {
    #         'status': 'success',
    #         'data': {
    #             'id': my_model.id,
    #             'name': my_model.name,
    #             'age': my_model.age,
    #         }
    #     }
    #     return JsonResponse(response_data)
    # else:
    #     return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})