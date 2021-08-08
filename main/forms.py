from django import forms 
from main.models import Assignment

class AssignmentForm(forms.ModelForm):
	class Meta:
		model = Assignment
		fields = '__all__'