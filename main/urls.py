from django.urls import path
from main.views import IndexView, ProcessAssignmentView, SuccessAssignmentView

app_name ='main'
urlpatterns = [
	path('', IndexView.as_view(), name='index'),
	path('submit/', ProcessAssignmentView.as_view(), name='submit'),
	path('success/', SuccessAssignmentView.as_view(), name='submit-success')
]