from django.urls import path, include
from rest_framework import routers
from api.views import CompanyModelViewSet
from pdf_creator_app.views import endpoint1

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'companies',CompanyModelViewSet)

urlpatterns = [
   path('', include(router.urls)),
   path('organization-name', endpoint1),
   # path('', ProductListAPIView.as_view(), name='product_list'),
]

