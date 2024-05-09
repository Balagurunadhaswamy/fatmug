from django.shortcuts import render
from .models  import Vendor, HistoricalPerformance, PurchaseOrder
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import VendorSerializer, PurchaseOrderSerializer, VendorPerformanceSerializer
from django.http import Http404
from django.http import JsonResponse
from rest_framework.mixins import UpdateModelMixin
from django.db.models import Q
from .exceptions import DataNotFound, PermissionDenied, BadRequest, NoContent, Created

class VendorViewset(APIView):
    def get(self, request, format=None):
        data = Vendor.objects.all()
        serializer = VendorSerializer(data, many=True)
        if len(serializer.data) == 0:
            raise DataNotFound
        else:
            return Response(serializer.data)
    

    def post(self, request, format=None):
        # import pdb; pdb.set_trace()
        serializer = VendorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            raise Created
        raise BadRequest


class VendorDetailViewset(APIView):

    def get_object(self, pk):
        try:
            return Vendor.objects.get(id=pk)
        except Vendor.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        vendor = self.get_object(pk)
        serializer = VendorSerializer(vendor)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        vendor = self.get_object(pk)
        serializer = VendorSerializer(vendor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        raise BadRequest

    def delete(self, request, pk, format=None):
        vendor = self.get_object(pk)
        vendor.delete()
        raise NoContent
    
class PurchaseOrderTrackingViewset(APIView):
    def get(self, request, format=None):
        data = PurchaseOrder.objects.all()
        serializer = PurchaseOrderSerializer(data, many=True)
        if len(serializer.data) == 0:
            raise DataNotFound
        else:
            return Response(serializer.data)
    
    def post(self, request, format=None):
        """
        Dummy data for testing and creating new records

        {
        "po_number": CHANGE NUMBER,
        "vendor": CHANGE ID,
        "order_date": "2024-05-06T10:36:39Z",
        "delivery_date": "2024-05-14T18:00:00Z",
        "items": {
            "object": "notebook"
        },
        "quantity": 1,
        "status": "Order Recieved",
        "quality_rating": 5.0,
        "issue_date": "2024-05-06T05:08:24Z"
    }
        """
        
        po_number = request.data.get('po_number')
        vendor_id = request.data.get('vendor')
        order_date = request.data.get('order_date')
        delivery_date = request.data.get('delivery_date')
        items = request.data.get('items')
        quantity = request.data.get('quantity')
        status = request.data.get('status')
        quality_rating = request.data.get('quality_rating')
        issue_date = request.data.get('issue_date')
        vendor = Vendor.objects.get(id=vendor_id)
        PurchaseOrder.objects.create(po_number=po_number, vendor=vendor, order_date=order_date,
                                     delivery_date=delivery_date, items=items, quantity=quantity,
                                     status=status, quality_rating=quality_rating, issue_date=issue_date)
        
        return JsonResponse({"response":"Data created Successfully!"})
    

class PurchaseOrderDetailViewset(APIView, UpdateModelMixin):

    serializer_class =  PurchaseOrderSerializer


    def get_object(self, pk):
        try:
            return PurchaseOrder.objects.get(id=pk)
        except PurchaseOrder.DoesNotExist:
            raise DataNotFound
        
    def get(self, request, pk, format=None):
        po = self.get_object(pk)
        serializer = PurchaseOrderSerializer(po)
        if len(serializer.data) == 0:
            raise DataNotFound
        else:
            return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        """
        For partial update of any field, change the 'vendor' and the value attached to it.

                {
        "{": {},
        "'vendor':{'id': 4},": {},
        "}": {}
        }
        """
        # import pdb;pdb.set_trace()
        if  request.user.is_superuser == True:
            po = self.get_object(pk)
            serializer = PurchaseOrderSerializer(po, data=request.data, partial= True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            raise BadRequest
        else:
            raise PermissionDenied()
    
    def delete(self, request, pk, format=None):
        po = self.get_object(pk)
        po.delete()
        raise NoContent
    

class VendorPerformanvceViewset(APIView):

    def get(self, request, pk, format=None):
        data = Vendor.objects.filter(id=pk)
        serializer = VendorPerformanceSerializer(data, many=True)
        if len(serializer.data) == 0:
            raise DataNotFound
        else:
            # import pdb;pdb.set_trace()
            return Response(serializer.data)
        
class VendorAcknowledgeViewset(APIView):
    def put(self, request, pk, format=None):
        import pdb;  pdb.set_trace()