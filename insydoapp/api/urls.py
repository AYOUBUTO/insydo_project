__author__ = 'Apolikamixitos'


from insydoapp.api.longest_string.views import LongestStringAPIView
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
# Examples:
# url(r'^$', 'soundy.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

    url(r'^longest_string/$', LongestStringAPIView.as_view()),
)