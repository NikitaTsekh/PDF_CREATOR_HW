
from rest_framework import serializers

from pdf_creator_app.models import ReplenismentEvent


class CompaniesSerializer(serializers.ModelSerializer):
    contract_date = serializers.DateTimeField(format="%Y-%m-%d")
    #category = serializers.SlugRelatedField(slug_field='name', queryset=ProductCategory.objects.all())
    class Meta:
        model = ReplenismentEvent
        fields = ('id', 'organization_name', 'organization_legal_address', 'organization_inn', 'organization_kpp', 'contract_number', 'contract_date',
                  'payment_sum_without_commission','commission_payment_sum','total')