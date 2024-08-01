from rest_framework import viewsets
from .serializer import DicomSeriesSerializer
import zipfile
import io
import pydicom
from django.core.files.uploadedfile import InMemoryUploadedFile
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .models import DicomSeries
from rest_framework import generics

class UploadDicomView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        file = request.FILES.get('dicom_archive')

        if not file:
            return Response({"error": "No file provided."}, status=status.HTTP_400_BAD_REQUEST)

        if not file.name.endswith('.zip'):
            return Response({"error": "The provided file is not a ZIP archive."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            with zipfile.ZipFile(file, 'r') as zip_file:
                for file_name in zip_file.namelist():
                    if file_name.lower().endswith('.dcm'):
                        with zip_file.open(file_name) as dicom_file:
                            try:
                                ds = pydicom.dcmread(dicom_file)

                                # Extract and convert data to ensure it's in the correct format
                                dicom_data = {
                                    "Patient_id": str(getattr(ds, 'PatientID', '')),  # Default to empty string if attribute is missing
                                    "Patient_name": str(getattr(ds, 'PatientName', '')),
                                    "Modality": str(getattr(ds, 'Modality', '')),
                                    "Study_Date": str(getattr(ds, 'StudyDate', ''))
                                }

                                # Create and validate the serializer with the data
                                serializer = DicomSeriesSerializer(data=dicom_data)
                                if serializer.is_valid():
                                    serializer.save()
                                else:
                                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

                            except Exception as e:
                                return Response({"error": f"Error processing DICOM file {file_name}: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

        except zipfile.BadZipFile:
            return Response({"error": "The file is not a valid ZIP archive."}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": f"Error processing ZIP archive: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({"status": "DICOM files processed successfully"}, status=status.HTTP_201_CREATED)

class DicomSeriesListView(generics.ListCreateAPIView):
    queryset = DicomSeries.objects.all()
    serializer_class = DicomSeriesSerializer

class DicomSeriesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DicomSeries.objects.all()
    serializer_class = DicomSeriesSerializer