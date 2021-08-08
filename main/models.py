from django.db import models

# Create your models here.

class Assignment(models.Model):
	full_name = models.CharField(max_length=255, blank=False, null=False)
	email = models.EmailField(max_length=255)
	country = models.CharField(max_length=255, blank=False, null=False)
	phone = models.CharField(max_length=255, blank=False)
	subject = models.CharField(max_length=255, blank=False)
	deadline = models.DateTimeField(auto_now=True)
	education_level = models.CharField(max_length=255, blank=False)
	referencing_style = models.CharField(max_length=255, blank=False)
	paper_type = models.CharField(max_length=255, blank=False)
	paper_length = models.CharField(max_length=255, blank=False)
	question = models.TextField()
	
	# Todo: the file field .. for attachemt
	# also , it might end up being a multi field attachment 
	# for multiple assignment .. 

	def __str__(self):
		return f'Assignment({self.name})'

	__repr__ = __str__

	# .. more helpers below 
