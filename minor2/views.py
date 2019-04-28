from rest_framework.response import Response
from rest_framework.views import APIView , status
from .models import Auth
from .serializers import questionSerializer,S_detailsserializer
class authentication(APIView):
	def post(self,request):
		pasw=Auth.objects.get(userid=request.data.get('userid','')).password
		print("pasw is " + str(pasw))
		if pasw==request.data.get('password',''):
			return Response("login successful")
		return Response("not found")

class quiz(APIView):

	def get(self,request):
		quest=questions.objects.all()
		print(quest)
		serializer=questionSerializer(quest,many=True)
		return Response(serializer.data)

	def post(self,request):
		subject_code = request.data.get('subject_code', '')
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