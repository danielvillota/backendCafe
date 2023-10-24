from django.shortcuts import render
from .serializers import cafeSerializer
from .models import Cafe
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class cafeView(APIView):
    
    def get(self, request):
        cafes=Cafe.objects.all()
        serializer=cafeSerializer(cafes, many=True)
        return Response(serializer.data)
