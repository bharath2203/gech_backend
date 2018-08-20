from django.db import models

class Notification(models.Model):

	title = models.CharField(max_length = 300)
	content = models.TextField()
	image = models.ImageField(blank = True, null = True)
	created_time = models.DateTimeField(auto_now_add = True)


