from student.models import Notification, Student, Faculty
from .serializers import NotificationSerializer, StudentSerializer, FacultySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404

class NotificationList(APIView):

	def get(self, request, format = None):
		print("Notification")
		notifications = Notification.objects.all()
		serializer = NotificationSerializer(notifications, many = True)
		return Response(serializer.data)

class NotificationDetail(APIView):

	def get_object(self, pk):
		try:
			return Notification.objects.get(pk = pk)
		except Notification.DoesNotExist:
			raise Http404

	def get(self, request, pk, format = None):
		notification = self.get_object(pk)
		serializer = NotificationSerializer(notification)
		return Response(serializer.data)
		
class StudentDetail(APIView):

	def get_object(self, slug):
		try:
			return Student.objects.get(usn = slug)
		except Student.DoesNotExist:
			raise Http404

	def get(self, request, slug, format = None):
		#dict = request.query_params
		#if not 'token' in dict.keys():
			#return Response(status = 400)
		student = self.get_object(slug)
		serializer = StudentSerializer(student, context = {"request": request})
		return Response(serializer.data)

class FacultyList(APIView):
	
	def get(self, request, format = None):
		dict = request.query_params
		faculties = Faculty.objects.all()	
		if not 'dep' in dict.keys():
			serializer = FacultySerializer(faculties, many = True)
		else:
			department_name = dict["dep"]
			faculty_list = []
			for faculty in faculties:
				if faculty.department.name == department_name:
					faculty_list.append(faculty)
			serializer = FacultySerializer(faculty_list, many = True)
		return Response(serializer.data)
