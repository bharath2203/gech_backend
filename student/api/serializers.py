from student.models import Notification, Student, Faculty
from rest_framework import serializers


class NotificationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Notification
		fields = ('id', 'title', 'content', 'image', 'belongs_to', 'created_time'
			, 'created_date')


class StudentSerializer(serializers.ModelSerializer):

	#photo_url = serializers.SerializerMethodField()

	class Meta:
		model = Student
		fields = ('usn', 'name', 'department_id', 'sem', 'student_phone_no', 'parents_phone_no',
			'image',  'father_name', 'mother_name','date_of_birth', 'address', 'email_id'
		)

	#def get_photo_url(self, student):
	#	request = self.context.get('request')
	#	photo_url = student.image
	#	return request.build_absolute_uri(photo_url)

class FacultySerializer(serializers.ModelSerializer):
	class Meta:
		model = Faculty
		fields = ('name', 'degree', 'achievements', 'department_id',
				'phone_no', 'email_id', 'position', 'image'
			)