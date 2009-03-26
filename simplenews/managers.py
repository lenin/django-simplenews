import datetime
from django.db.models.manager import Manager

class ArticleManager(Manager):
    def published(self):
        return self.get_query_set().filter(pub_date__lte=datetime.datetime.now())
