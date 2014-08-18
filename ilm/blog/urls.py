from django.conf.urls import patterns, url

from .views import ListPostsView, DetailPostView, PostYearArchiveView


urlpatterns = patterns('',
                url(r'^posts/$',
                    ListPostsView.as_view(),
                    name='list_posts'),
                url(r'^posts/(?P<slug>[-_\w]+)/detail/$',
                    DetailPostView.as_view(),
                    name='detail_post'),
                url(r'^posts/(?P<year>[0-9]{4})/$',
                    PostYearArchiveView.as_view(),
                    name="post_year_archive"),
                )
