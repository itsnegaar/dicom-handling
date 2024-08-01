from django.shortcuts import render
from rest_framework import viewsets
from serializer import DicomSeriesSerializer
from models import DicomSeries

class DicomSeriesViewset(viewsets.ModelViewSet):
    queryset = DicomSeries.objects.all()
    serializer_class = DicomSeriesSerializer


