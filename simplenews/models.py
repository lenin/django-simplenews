from datetime import datetime

from django.db import models
from django.db.models import permalink
from django.utils.translation import ugettext_lazy as _

class Article(models.Model):

    title = models.CharField(max_length=50)
    content = models.TextField()
    pub_date = models.DateTimeField(default=datetime.now, editable=False)

    class Meta:
        ordering = ['-pub_date']
        verbose_name = _(u'article')
        verbose_name_plural = _(u'articles')

    def __unicode__(self):
        return self.title

    @permalink
    def get_absolute_url(self):
        return ('news_detail', None, { 'object_id': self.id })

