from django.conf.urls import include, url
from rest_framework.urlpatterns import format_suffix_patterns
from timer import views


urlpatterns = [
    url(r'^maps/$', views.MapList.as_view()),
    url(r'^maps/(?P<pk>[0-9]+)/$', views.MapDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
