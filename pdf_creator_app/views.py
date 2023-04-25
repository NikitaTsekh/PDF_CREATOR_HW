from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import ReplenismentEvent
import json
# Create your views here.
@csrf_exempt
def endpoint1(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        my_model = ReplenismentEvent.objects.create(
            name=data['name'],
            age=data['age'],
        )
        response_data = {
            'status': 'success',
            'data': {
                'id': my_model.id,
                'name': my_model.name,
                'age': my_model.age,
            }
        }
        return JsonResponse(response_data)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})