from django.conf.urls import patterns, url

from .views import ListPostsView, DetailPostView


urlpatterns = patterns('',
                url(r'^posts/$',
                    ListPostsView.as_view(),
                    name='list_posts'),
                url(r'^posts/(?P<slug>[-_\w]+)/detail/$',
                    DetailPostView.as_view(),
                    name='detail_post'),
                )
