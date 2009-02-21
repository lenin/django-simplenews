from django.contrib import admin

from simplenews.models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date')
    list_filter = ('pub_date',)
    search_fields = ('title', 'content')
    date_hierarchy = 'pub_date'

admin.site.register(Article, ArticleAdmin)
