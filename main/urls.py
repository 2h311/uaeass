from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from main.views import *


app_name ='main'
urlpatterns = [
	path('', IndexView.as_view(), name='index'),
	path('submit/', ProcessAssignmentView.as_view(), name='submit'),
	path('success/', SuccessAssignmentView.as_view(), name='submit-success'),

	path('reviews/', ReviewsView.as_view(), name='reviews'),
	path('review-submit/', ProcessReviews.as_view(), name='submit-reviews'),

	path('services/', ServicesView.as_view(), name='services'),
	
	path('samples/', SamplesView.as_view(), name='samples'),
	path('samples/<slug>', SamplesDetailView.as_view(), name='samples_detail'),
	path('search_sample/', SampleSearchView.as_view(), name='search_sample'), # process the search sample input field

	path('experts/', ExpertsView.as_view(), name='experts'),

	path('<str:filename>/', download_file, name='download'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)