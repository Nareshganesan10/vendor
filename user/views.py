import random
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import VendorModel

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def vendor(request, vendor_id=None):
    pass
