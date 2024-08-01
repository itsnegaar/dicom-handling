
from django.urls import path
from .views import UploadDicomView, DicomSeriesListView, DicomSeriesDetailView

urlpatterns = [
    path('upload-dicom/', UploadDicomView.as_view(), name='upload-dicom'),
    path('dicom-series/', DicomSeriesListView.as_view(), name='dicom-series-list'),
    path('dicom-series/<int:pk>/', DicomSeriesDetailView.as_view(), name='dicom-series-detail'),
]


