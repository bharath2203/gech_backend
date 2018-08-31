from django.db import models

class Department(models.Model):
	departments = (
		('CS', 'COMPUTER SCIENCE & ENGG'),
		('ENC', 'ELECTRONICS AND COMMUNICATION & ENGG'),
		('CV', 'CIVIL ENGG'),
		('IS', 'INFORMATION SCIENCE'),
	)

	name = models.CharField(choices = departments, max_length = 100, primary_key = True)


	def __str__(self):
		return self.name

class Student(models.Model):


	sems = (('1', 'First'), ('2', 'Second'), ('3', 'Third'), ('4', 'Fourth'),
			('5', 'Fifth'), ('6', 'Sixth'), ('7', 'Seventh'), ('8', 'Eighth')
	)

	usn = models.CharField(max_length = 10, primary_key= True)
	name = models.CharField(max_length = 100)
	department_id = models.ForeignKey('Department', on_delete = models.CASCADE, null = True)
	student_phone_no = models.CharField(max_length = 10)
	parents_phone_no = models.CharField(max_length = 10)
	father_name = models.CharField(max_length = 100)
	mother_name = models.CharField(max_length = 100)
	date_of_birth = models.DateField()
	address = models.TextField(max_length = 500)
	sem = models.CharField(choices = sems, max_length = 10)


	def __str__(self):
		return self.usn

class Notification(models.Model):

	title = models.CharField(max_length = 300)
	content = models.TextField()
	image = models.ImageField(blank = True, null = True)
	belongs_to = models.ForeignKey('Department', on_delete = models.CASCADE, null = True)
	created_time = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return self.title
