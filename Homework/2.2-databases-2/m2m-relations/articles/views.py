from pprint import pprint

from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    pprint(Article.objects.scopes.all())
    articles = Article.objects.all().prefetch_related('scopes').order_by('-published_at')

    for article in articles:
        for scope in article.scopes.all():
            articleset = scope.get(article=article)
            scope.is_main = articleset.is_main


    context = {
        'object_list': articles
    }
    return render(request, 'articles/news.html', context)
