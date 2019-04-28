from rest_framework import serializers
from minor2.models import Uploadfile

class uploadfileserializer(serializers.ModelSerializer):
	class Meta:
		model=Uploadfile
		fields=('pk','file',)