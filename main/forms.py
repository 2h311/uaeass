from django import forms 
from django.forms import ClearableFileInput

from main.models import Assignment, Review, Sample

class AssignmentForm(forms.ModelForm):
	class Meta:
		model = Assignment
		fields = '__all__'


class ReviewForm(forms.ModelForm):
	class Meta:
		model = Review
		fields = '__all__'


class SampleForm(forms.ModelForm):
	class Meta:
		model = Sample
		fields = '__all__'
		widgets = {
            'file': ClearableFileInput(attrs={'multiple': True}),
        }