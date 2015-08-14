from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'insydo_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'insydoapp.views.longest_string_view', name='longest_string'),
)
