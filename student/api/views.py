from student.models import Notification, Student
from .serializers import NotificationSerializer, StudentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404

class NotificationList(APIView):

	def get(self, request, format = None):
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
		student = self.get_object(slug)
		serializer = StudentSerializer(student)
		return Response(serializer.data)
