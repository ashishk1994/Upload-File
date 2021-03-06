from django.conf.urls import patterns, include, url
from django.contrib.auth import views as auth_views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'edu.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include('upload.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/',include('registration.backends.default.urls')),
)
