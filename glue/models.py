from django.db import models

class Notification(models.Model):

	title = models.CharField(max_length = 300)
	content = models.TextField()
	image = models.ImageField(blank = True, null = True)
	created_time = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return title


class CoreMember(models.Model):

	sems = (('1', 'First'), ('2', 'Second'), ('3', 'Third'), ('4', 'Fourth'),
			('5', 'Fifth'), ('6', 'Sixth'), ('7', 'Seventh'), ('8', 'Eighth')
	)

	usn = models.CharField(max_length = 10, primary_key= True)
	name = models.CharField(max_length = 100)
	student_phone_no = models.CharField(max_length = 10)
	date_of_birth = models.DateField()
	address = models.TextField(max_length = 500)
	sem = models.CharField(choices = sems, max_length = 10)
	email_id = models.EmailField(null = True)

	def __str__(self):
		return self.name


class GlueBlog(models.Model):

	sl_no = models.IntegerField()
	title = models.CharField(max_length = 100)
	blog_content = models.TextField()
	attendence = models.IntegerField()
	speakers = models.ForeignKey('CoreMember', on_delete = models.SET_NULL, null = True)
	documenter = models.ForeignKey('CoreMember', on_delete = models.SET_NULL, null = True, related_name = "Docs"	)
	session_date = models.DateField()
	session_time = models.TimeField()
	resource_link = models.URLField(null = True)

	class meta:
		ordering = ['sl-no']

	def __str__(self):
		return self.title



