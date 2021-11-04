import mimetypes
import os

from django.shortcuts import render, redirect
from django.urls import resolve
from django.views.generic import ListView, CreateView, TemplateView, FormView, DetailView
from django.http import HttpResponse

from main.forms import AssignmentForm, ReviewForm
from main.models import Review, Sample


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

	def form_invalid(self, form):
		'''
		What do we do if the form is invalid .. ?
		we redirect to the home page 
		'''
		return super().form_invalid(form)


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


class ReviewsView(ListView):
	model = Review
	template_name = 'main/reviews.html'
	paginate_by = 5
	ordering = ['-id']


class ProcessReviews(CreateView):
	template_name = 'main/reviews.html'
	form_class = ReviewForm

	def get_success_url(self):
		return f"{reverse('main:reviews')}"


class ServicesView(TemplateView):
	template_name = 'main/services.html'


class SamplesView(ListView):
	template_name = 'main/samples.html'
	model = Sample
	paginate_by = 5


class SamplesDetailView(DetailView):
	model = Sample
	template_name = 'main/sample_details.html'


class SampleSearchView(CreateView):
	template_name = 'main/sample_base.html'
	paginate_by = 5

	def post(self, request, *args, **kwargs):
		search = self.request.POST.get('search')
		if search:
			queryset = Sample.objects.filter(heading__icontains=search)
		else:
			search = self.request.POST.get('categories')
			queryset = Sample.objects.filter(subject__icontains=search)

		return render(request, 'main/samples.html', {'object_list': queryset})


class ExpertsView(TemplateView):
	template_name = 'main/experts.html'


def download_file(request, filename):
	BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	filepath = os.path.join(BASE_DIR, os.path.join('media', 'documents'), filename)
	fl = open(filepath, 'rb')
	mimetype, _ = mimetypes.guess_type(filepath)
	response = HttpResponse(fl, content_type=mimetype)
	response['Content-Disposition'] = "attachment; filename=%s" % filename
	return response