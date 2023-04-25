from django.urls import path, include
from rest_framework import routers
from api.views import CompanyModelViewSet

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'companies',CompanyModelViewSet)

urlpatterns = [
   path('', include(router.urls)),
   # path('', ProductListAPIView.as_view(), name='product_list'),
]

