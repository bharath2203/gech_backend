from student.models import Notification, Student
from rest_framework import serializers


class NotificationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Notification
		fields = ('id', 'title', 'content', 'image', 'type', 'created_time')


class StudentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Student
		fields = ('usn', 'name', 'ug_program', 'student_phone_no', 'parents_phone_no',
			'father_name', 'mother_name','date_of_birth', 'address',

		)