from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.data_list, name='data_list'),
	url(r'^report/new/$', views.report_new, name = 'report_new')
]