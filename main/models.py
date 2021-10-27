from django.db import models

# Create your models here.
OPTIONS = (
	(1, 1),
	(2, 2),
	(3, 3),
	(4, 4),
	(5, 5),
)

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
	word_count = models.CharField(max_length=255, blank=False, default='')

	file = models.FileField(upload_to='documents/')
	
	# Todo: the file field .. for attachemt
	# also , it might end up being a multi field attachment 
	# for multiple assignment .. 

	# Todo: you need to handle unique to avoid multiple submission for the same request 

	def __str__(self):
		return f'Assignment({self.full_name})'

	__repr__ = __str__

	# .. more helpers below 


# Create your models here.
class Review(models.Model):
	title = models.CharField(max_length=256)
	name = models.CharField(max_length=256)
	qualification = models.CharField(max_length=256)
	assignment_id = models.CharField(max_length=256)
	star = models.IntegerField(choices=OPTIONS)	
	description = models.TextField()
	
	def __str__(self):
		return self.title

	__repr__ = __str__


