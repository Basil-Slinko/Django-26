from django.views.generic import ListView
from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    context = {
        'object_list': Article.objects.order_by('-published_at').all()
    }
    return render(request, 'articles/news.html', context)












 # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    # ordering = '-published_at'
    # .order_by('title', 'text', 'published_at', 'image')
