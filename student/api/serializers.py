from student.models import Notification, Student, Faculty
from rest_framework import serializers


class NotificationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Notification
		fields = ('id', 'title', 'content', 'image', 'belongs_to', 'created_time'
			, 'created_date')


class StudentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Student
		fields = ('usn', 'name', 'department_id', 'ug_program', 'sem', 'student_phone_no', 'parents_phone_no',
			'father_name', 'mother_name','date_of_birth', 'address', 'email_id'
		)

class FacultySerializer(serializers.ModelSerializer):
	class Meta:
		model = Faculty
		fields = ('name', 'degree', 'achievements', 'department_id',
				'phone_no', 'email_id', 'position', 'image'
			)