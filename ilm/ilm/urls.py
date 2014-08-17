from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ilm.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^auth/', include('auth.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^markdown/', include('django_markdown.urls')),
)
