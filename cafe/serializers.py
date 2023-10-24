from rest_framework import serializers
from .models import Cafe

class cafeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cafe
        fields=['nombre','tipo','region']