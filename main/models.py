import os

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
	
	class Meta:
		ordering = ('id',)

	def __str__(self) -> str:
		return f'Assignment({self.full_name})'

	__repr__ = __str__

	# .. more helpers below 


class Review(models.Model):
	title = models.CharField(max_length=256)
	name = models.CharField(max_length=256)
	qualification = models.CharField(max_length=256)
	# assignment_id = models.CharField(max_length=256)
	star = models.IntegerField(choices=OPTIONS)	
	description = models.TextField()
	
	class Meta:
		ordering = ('id',)

	def __str__(self) -> str:
		return self.title

	__repr__ = __str__


class Sample(models.Model):
	heading = models.CharField(max_length=256)
	subject = models.CharField(max_length=256)
	description = models.TextField(blank=True, null=True)
	slug = models.SlugField(max_length=250, default='')
	url = models.CharField(max_length=256, blank=True, null=True, default='')

	class Meta:
		ordering = ('id',)

	def __str__(self) -> str:
		return self.heading

	__repr__ = __str__


class SampleMultipleFile(models.Model):
	file = models.FileField(upload_to='samples/')
	sample = models.ForeignKey(Sample, on_delete=models.CASCADE, related_name='samples')

	def __str__(self) -> str:
		return os.path.split(self.file.name)[-1]

	__repr__ = __str__


class Question(models.Model):
	category = models.CharField(max_length=256)
	date = models.DateField(blank=True, null=True)
	description = models.TextField()
	# TODO: add an images fields  

	def __str__(self) -> str:
		return self.category 

	__repr__ = __str__