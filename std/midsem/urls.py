from django.conf.urls import patterns, url

from midsem import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<e_id>\d+)/$', views.detail, name='detail'),
    url(r'^hod/$', views.hod, name='hod'),
)
