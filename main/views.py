from django.shortcuts import render
from django.views.generic import CreateView, TemplateView, FormView

from main.forms import AssignmentForm
# Create your views here.


class IndexView(TemplateView):
	'''
	The home page and the likes 
	'''
	template_name = 'main/index.html'
	def get_context_data(self, *args, **kwargs):
		return super().get_context_data()


class ProcessAssignmentView(CreateView):
	'''
	Sends email data to the receiver 
	as well as stores in DB. 
	so , definitely, model is required for the form data 
	'''

	form_class = AssignmentForm

	# def post(self, request, *args, **kwargs): ...


	# def form_valid(self, form):
		# '''
		# send email and store the data 
		# '''
		# pass


	def form_invalid(self, form):
		'''
		What do we do if the form is invalid .. ?
		'''
		return super().form_invalid(form)
