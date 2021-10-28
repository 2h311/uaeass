from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from main.views import IndexView, ProcessAssignmentView, SuccessAssignmentView, ReviewsView, ProcessReviews, ServicesView,  SamplesView, ExpertsView


app_name ='main'
urlpatterns = [
	path('', IndexView.as_view(), name='index'),
	path('submit/', ProcessAssignmentView.as_view(), name='submit'),
	path('success/', SuccessAssignmentView.as_view(), name='submit-success'),

	path('reviews/', ReviewsView.as_view(), name='reviews'),
	path('review-submit/', ProcessReviews.as_view(), name='submit-reviews'),

	path('services/', ServicesView.as_view(), name='services'),
	path('samples/', SamplesView.as_view(), name='samples'),
	path('expert/', ExpertsView.as_view(), name='experts'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)