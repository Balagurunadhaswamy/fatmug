from rest_framework import serializers 
from .models import Vendor, PurchaseOrder, HistoricalPerformance

class VendorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vendor
        fields = ['id', 'name', 'contact_details', 'address', 'vendor_code', 'on_time_delivery_rate', 'quality_rating_avg', 'average_response_time', 'fulfillment_rate']

class VendorPOSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vendor
        fields = ['id']

class PurchaseOrderSerializer(serializers.ModelSerializer):
    vendor = VendorPOSerializer(required=False)
    class Meta:
        model = PurchaseOrder
        fields = ['po_number', 'vendor', 'order_date', 'delivery_date', 'items', 'quantity', 'status', 'quality_rating', 'issue_date']

    # def update(self, instance, validated_data):
    #     import pdb; pdb.set_trace()