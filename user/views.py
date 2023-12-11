import random
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import VendorModel
from .serializers import VendorSerializer


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def vendor(request, vendor_id=None):
    # Displaying all the vendors
    if request.method == 'GET' and vendor_id == None:
        vendor = VendorModel.objects.all()
        serializer = VendorSerializer(vendor, many=True)
        return Response(serializer.data, safe=False)
    
    # Creating new vendor
    elif request.method == 'POST' and vendor_id == None:
        pass
    
    # Retrieving a specific vendor detail
    elif request.method == 'GET' and vendor_id != None:
        pass

    # Update a vendor's details
    elif request.method == 'PUT':
        pass
    
    #  Delete a vendor
    elif request.method == 'DELETE':
        pass