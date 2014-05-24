from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'std.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^lalit/', include(admin.site.urls)),
    url(r'^lk/', include('midsem.urls')),
)
