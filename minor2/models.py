from django.db import models

class Auth(models.Model):
	userid=models.CharField(max_length=10,unique=True)
	password=models.CharField(max_length=10)

class questions(models.Model):
	subject_code=models.CharField(max_length=10)
	ques=models.CharField(max_length=150)

class S_details(models.Model):
	name=models.CharField(max_length=40)
	userid=models.CharField(max_length=10)
	batch=models.CharField(max_length=2)
	subject_code=models.CharField(max_length=10)
	marks=models.IntegerField()


class Uploadfile(models.Model):
	file=models.FileField("uploaded file")
	