from django.db import models

class DicomSeries(models.Model):
    Patient_id = models.CharField(required=True)
    Patient_name = models.CharField()
    Modality = models.CharField(required=True)
    Study_Date = models.CharField()

# Create your models here.
