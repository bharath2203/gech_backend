from django.db import models

class Student(models.Model):

	ug_programs = (
		('CS', 'COMPUTER SCIENCE & ENGG'),
		('ENC', 'ELECTRONICS AND COMMUNICATION & ENGG'),
		('CV', 'CIVIL ENGG'),
		('ME', 'MECHANICAL ENGG'),
	)

	usn = models.CharField(max_length = 10, primary_key= True)
	name = models.CharField(max_length = 100)
	ug_program = models.CharField(choices = ug_programs, max_length = 40)
	student_phone_no = models.CharField(max_length = 10)
	parents_phone_no = models.CharField(max_length = 10)
	father_name = models.CharField(max_length = 100)
	mother_name = models.CharField(max_length = 100)
	date_of_birth = models.DateField()
	address = models.TextField(max_length = 500)

class Notification(models.Model):

	notification_types = (
		('CS', 'COMPUTER SCIENCE & ENGG'),
		('ENC', 'ELECTRONICS AND COMMUNICATION & ENGG'),
		('CV', 'CIVIL ENGG'),
		('ME', 'MECHANICAL ENGG'),	
		('GECH','COLLEGE')
	)

	title = models.CharField(max_length = 300)
	content = models.TextField()
	image = models.ImageField(blank = True, null = True)
	type = models.CharField(choices = notification_types, max_length = 100)
	created_time = models.DateTimeField(auto_now_add = True)
