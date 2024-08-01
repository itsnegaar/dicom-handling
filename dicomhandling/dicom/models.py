from django.db import models

class DicomSeries(models.Model):
    Patient_id = models.CharField(max_length=100, blank=False, null=False)
    Patient_name = models.CharField(max_length=255, blank=True, null=True)
    Modality = models.CharField(max_length=10, blank=False, null=False)
    Study_Date = models.CharField(max_length=10, blank=True, null=True)
