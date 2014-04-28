from django.conf.urls import patterns, url
from upload import views

urlpatterns = patterns('',
#		 url(r'^$',views.index,name='index'),
		 url(r'^$',views.index, name='index'),
		 url(r'^logout/$', views.logout_page),
		 url(r'^list_file/$',views.list_file, name='list_file'),
#		 url(r'^logout/$', views.logout_page, name='logout'),	
		)
