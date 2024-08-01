# serializers.py
from rest_framework import serializers
from .models import DicomSeries

class DicomSeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DicomSeries
        fields = '__all__'
