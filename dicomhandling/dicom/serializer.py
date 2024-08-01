from rest_framework import serializers
from models import DicomSeries
from views import DicomSeriesViewset

class DicomSeriesSerializer(serializers.ModelSerializer):
    model = DicomSeries

    class Mate:
        fields = '__all__'
