from django.conf.urls import include, url
from rest_framework.urlpatterns import format_suffix_patterns
from timer import views
from .filters import MapFilter


urlpatterns = [
    url(r'^maps/$', views.MapList.as_view()),
    url(r'^maps/(?P<pk>[0-9]+)/$', views.MapDetail.as_view()),
    url(r'^players/$', views.PlayerList.as_view()),
    url(r'^players/(?P<pk>[0-9]+)/$', views.PlayerDetail.as_view()),
    url(r'^servers/$', views.ServerList.as_view()),
    url(r'^servers/(?P<pk>[0-9]+)/$', views.ServerDetail.as_view()),
    url(r'^times/$', views.TimeList.as_view()),
    url(r'^times/(?P<pk>[0-9]+)/$', views.TimeDetail.as_view())

]

urlpatterns = format_suffix_patterns(urlpatterns)
