from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from pdf_creator_app.models import ReplenismentEvent
from pdf_creator_app.serializers import CompaniesSerializer


class CompanyModelViewSet(ModelViewSet):
    queryset = ReplenismentEvent.objects.all()
    serializer_class = CompaniesSerializer
