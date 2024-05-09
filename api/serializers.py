from rest_framework import serializers 
from .models import Vendor, PurchaseOrder, HistoricalPerformance
import datetime
from django.db.models import F, Avg

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
        fields = ['po_number', 'vendor', 'order_date', 'delivery_date', 'items', 'quantity', 'status', 'quality_rating', 'issue_date', 'delivery_date']

    def update(self, instance, validated_data):
        if validated_data['status'] == 'DD':
            validated_data['delivered_date'] = datetime.datetime.now()
        super().update(instance=instance, validated_data=validated_data)

        """
        Code to update vendor on time delivery rate
        """
        completed_po = len(PurchaseOrder.objects.filter(vendor=instance.vendor, status='DD'))
        tot_po = len(PurchaseOrder.objects.filter(vendor=instance.vendor))
        fulfilment_rate = "{:.2f}".format(completed_po/tot_po) #Order Fulfillment rate calculation
        if validated_data['status'] == 'DD':
            data = PurchaseOrder.objects.filter(vendor=instance.vendor, status='DD') 
            del_rate = len(data)/len(data.filter(delivered_date__lte=F('delivery_date'))) #delivery rate calculation
            avg_quality_rating = PurchaseOrder.objects.filter(vendor__id=3, status='DD').aggregate(Avg("quality_rating", default=1)) #Average Quality  calculation
            Vendor.objects.filter(id=instance.vendor.id).update(on_time_delivery_rate=del_rate, quality_rating_avg=avg_quality_rating.get('quality_rating__avg'), fulfillment_rate=fulfilment_rate)
        elif validated_data['status'] == 'OC':
            #Average response time calculation
            res_time = PurchaseOrder.objects.filter(vendor=instance.vendor).aggregate(avg_res_time=Avg(F('delivery_date')-F('order_date')))
            # import pdb; pdb.set_trace()
            avg_days = "{:.2f}".format(res_time['avg_res_time']/datetime.timedelta(days=1))
            Vendor.objects.filter(id=instance.vendor.id).update(average_response_time = avg_days, fulfillment_rate=fulfilment_rate)
        else:
            Vendor.objects.filter(id=instance.vendor.id).update(fulfillment_rate=fulfilment_rate)
        return instance
    
class VendorPerformanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vendor
        fields =  ['on_time_delivery_rate', 'quality_rating_avg', 'average_response_time', 'fulfillment_rate']