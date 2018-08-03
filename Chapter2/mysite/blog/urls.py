from django.conf.urls import url

from . import views

urlpatterns = [
    # blog list views
    url(r'^$',
        views.post_list,
        name='post_list'),
    # blog list by tag
    url(r'^tag/(?P<tag_slug>[-\w]+)$',
        views.post_list,
        name='post_list_by_tag'),
    # url(r'^$',
    #     views.PostListView.as_view(),
    #     name='post_list'),
    # blog detail views with tags
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$',
        views.post_detail,
        name='post_detail'),
    #
    url(r'^(?P<post_id>\d+)/share/$',
        views.post_share,
        name='post_share'),
]
