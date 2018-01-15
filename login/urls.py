from django.conf.urls import url
from .views import *


app_name = 'login'

urlpatterns = [
	url(r'^$', landing, name='landing'),
	url(r'^signin$', signin, name='signin'),
	url(r'^login/$', loginView, name='loginView'),
	url(r'^register/$', registerView, name='registerView'),
	url(r'^home/$',home,name='home'),
	url(r'^logout/$',logoutView,name='logoutView'),
]
