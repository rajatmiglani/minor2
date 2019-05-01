from rest_framework import viewsets
from fileupload_rest.serializers import uploadfileserializer
from minor2.models import Uploadfile

class UploadfileViewSet(viewsets.ModelViewSet):
	queryset=Uploadfile.objects.all()
	serializer_class=uploadfileserializer