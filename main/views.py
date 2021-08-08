from django.shortcuts import render, redirect
from django.urls import reverse
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
	template_name = 'main/index.html'
	form_class = AssignmentForm

	def get_success_url(self):
		'''
		Redirect user to the success page .. 
		'''
		name = self.request.POST.get('full_name', 'Blankee')
		return f"{reverse('main:submit-success')}?name={name}"


	# def form_valid(self, form):
		# '''
		# send email and store the data 
		# '''
	


	def form_invalid(self, form):
		'''
		What do we do if the form is invalid .. ?
		we redirect to the home page 
		'''
		return super().form_invalid(form)
		# redirect(reverse('index'))


class SuccessAssignmentView(TemplateView):
	'''
	Where users are redirected to after a successful submission 
	'''
	
	template_name = 'main/success.html'

	def get_context_data(self, *args, **kwargs):
		'''
		Add whatever relevant message the user might need 
		such as the order ID
		ts = self.request.query_params.get('ts', 0)
		'''
		name = self.request.GET.get('name', 'John Doe')
		return super().get_context_data(name=name, **kwargs)
