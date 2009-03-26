from datetime import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _

from simplenews.managers import ArticleManager

class Article(models.Model):
    title = models.CharField(_(u'title'), max_length=50)
    content = models.TextField(_(u'content'))
    pub_date = models.DateTimeField(_(u'publication date'), default=datetime.now)

    objects = ArticleManager()

    class Meta:
        ordering = ['-pub_date']
        verbose_name = _(u'article')
        verbose_name_plural = _(u'articles')

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return ('news_detail', None, { 'object_id': self.id })
    get_absolute_url = models.permalink(get_absolute_url)
