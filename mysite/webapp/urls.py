from django.conf.urls import url
from . import views#. is a relative import (import from current package)

urlpatterns=[
	url(r'^$',views.index,name='index')]#^$ is start (^) then end($) so just the index of the website
