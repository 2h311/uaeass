from django import forms 
from main.models import Assignment, Review

class AssignmentForm(forms.ModelForm):
	class Meta:
		model = Assignment
		fields = '__all__'


class ReviewForm(forms.ModelForm):
	class Meta:
		model = Review
		fields = '__all__'