import datetime
from django.conf.urls.defaults import *
from django.views.generic import create_update, list_detail
from django.contrib.auth.decorators import user_passes_test
from django.contrib.syndication.views import feed

from simplenews.models import Article
from simplenews.feeds import ArticlesFeed

feeds = {'articles': ArticlesFeed}

staff_required = user_passes_test(lambda u: u.is_staff)

create_update_info_dict = { 'model': Article }
list_detail_info_dict = {
    'queryset': Article.objects.published(),
}

urlpatterns = patterns('',
    url(r'^feeds/(?P<url>.*)/$', feed, {'feed_dict': feeds}, name='news_feed'),
    url(r'^create/$',
        staff_required(create_update.create_object),
        create_update_info_dict,
        name='news_create'),
    url(r'^update/(?P<object_id>\d+)/$',
        staff_required(create_update.update_object),
        create_update_info_dict,
        name='news_update'),
    url(r'^delete/(?P<object_id>\d+)/$',
        staff_required(create_update.delete_object),
        dict(create_update_info_dict, post_delete_redirect='../..'),
        name='news_delete'),
    url(r'^(?P<object_id>\d+)/$',
        list_detail.object_detail,
        list_detail_info_dict,
        name='news_detail'),
    url(r'^$',
        list_detail.object_list,
        dict(list_detail_info_dict, paginate_by=5),
        name='news_list'),
)

