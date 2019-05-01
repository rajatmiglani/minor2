from rest_framework import serializers
from minor2 import models
from minor2.models import Auth,questions,S_details,Uploadfile
from rest_framework import exceptions
from django.contrib.auth.models import User

class questionSerializer(serializers.ModelSerializer):
	class Meta:
		model=questions
		fields=('ques',
			)

class S_detailsserializer(serializers.ModelSerializer):
	class Meta:
		model=S_details
		fields=(
			'name',
			'userid',
			'batch',
			'subject_code',
			'marks'
		)
