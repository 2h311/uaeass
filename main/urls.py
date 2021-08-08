from django.urls import path
from main.views import IndexView, ProcessAssignmentView

app_name ='main'
urlpatterns = [
	path('', IndexView.as_view(), name='index'),
	path('submit/', ProcessAssignmentView.as_view(), 'submit')
]