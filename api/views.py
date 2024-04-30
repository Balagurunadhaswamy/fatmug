from django.shortcuts import render
from .models  import Vendor, HistoricalPerformance, PurchaseOrder
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import VendorSerializer

class VendorViewset(APIView):
    def get(self, request, format=None):
        data = Vendor.objects.all()
        serializer = VendorSerializer(data, many=True)
        return Response(serializer.data)
    

    def post(self, request, format=None):
        import pdb; pdb.set_trace()
        serializer = VendorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)