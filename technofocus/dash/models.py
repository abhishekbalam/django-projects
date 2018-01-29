from django.db import models
from django.utils import timezone

class PaperList(models.Model):
	title = models.TextField()
	names = models.TextField()
	abstract = models.TextField()
	keywords = models.TextField()
	file = models.FileField(upload_to='files/projects_all/%Y/%m/%d')
	accepted = models.BooleanField()

	def __str__(self):
		return self.name


