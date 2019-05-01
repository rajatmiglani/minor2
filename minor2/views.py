from rest_framework.response import Response
from rest_framework.views import APIView , status
from .models import Auth,questions,Uploadfile,uploadcode
from django.core.files.storage import FileSystemStorage
from .serializers import questionSerializer,S_detailsserializer,codeSerializer
import requests
import shutil, os
from .settings import FILES_FOLDER,MEDIA_ROOT
class authentication(APIView):
	def post(self,request):
		pasw=Auth.objects.get(userid=request.data.get('userid','')).password
		print("pasw is " + str(pasw))
		if pasw==request.data.get('password',''):
			return Response(1)
		return Response("not found")

class quiz(APIView):

	def get(self,request):
		quest=questions.objects.all()
		#print(quest)
		serializer=questionSerializer(quest,many=True)
		return Response(serializer.data)

	def post(self,request):
		#subject_code = request.data.get('subject_code', '')
		ques = request.data.get('ques', '')
		obj = questions(subject_code=subject_code, ques=ques)
		obj.save()
		return Response("ok")

class batchdetails(APIView):
	def get(self,request):
		var=S_details.objects.all()
		serializer=S_detailsserializer(var,many=True)
		return Response(serializer.data)

class submit_marks(APIView):
	def post(self,request):
		userid=request.data.get('userid','')
		name=request.data.get('name','')
		batch=request.data.get('batch','')
		subject_code=request.data.get('subject_code','')
		marks=request.data.get('marks','')
		#quiz_instance=request.data.get('quiz_instance','')
		obj=S_details(name=name,userid=userid,batch=batch,subject_code=subject_code,marks=marks)
		obj.save()
		return Response("ok")

'''class submit_file(APIView):
	def get(self,request):
		#file=request.data.get('file','')
		#obj=Uploadfile(file=file)
		#obj.save()
		#file=request.FILES['file']
		#fs=FileSystemStorage()
		#fs.save(file.name,file)
		#path= FILES_FOLDER+'input.txt'
		#dest=/home/miglani/minor 2
		#shutil.move(os.path.join(path,'input.txt'), os.path.join(/home/miglani/minor 2,'input.txt'))
		return Response("ok")		
		#file=request.FILES['path']
		#file=requests.get(path)
		#fs=FileSystemStorage()
		#fs.save(file.name,file)'''
		
class submitcode(APIView):
	def post(self,request):
		cd = request.data.get('code','')
		obj = uploadcode(code=cd)
		obj.save()
		latest_change = uploadcode.objects.last()
		#cd=uploadcode.objects.all()
		#serializer=codeSerializer(cd,many=True)
		print(latest_change.code)
		f=open("code.txt","w")
		for line in latest_change.code:
			f.write(line)
		f.close()
		return Response("ok")

class answer(APIView):
	def get(self,request):
		with open("marks.txt", "r") as ins:
			array=[]
			for line in ins:
				array.append(line)
			s=""
			s=s.join(array)
			#print(s)
			return Response(s)