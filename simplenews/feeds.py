import datetime
from django.contrib.syndication.feeds import Feed
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse

from simplenews.models import Article

class ArticlesFeed(Feed):
    title = Site.objects.get_current().name

    def link(self):
        return reverse('news_list')

    def items(self):
        return Article.objects.filter(pub_date__lte=datetime.datetime.now())[:10]

    def item_pubdate(self, obj):
        return obj.pub_date
