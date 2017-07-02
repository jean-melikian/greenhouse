from django.conf.urls import url

from . import views

app_name = 'greenhouseApp'

urlpatterns = [
	url(r'^login$', views.login, name='login'),

	url(r'^sensorsEntry/$', views.sensorsEntry_list, name='sensorsentry-list'),
	url(r'^sensorsEntry/(?P<pk>[0-9]+)/$', views.sensorsEntry_details, name='sensorsentry-details'),

]
