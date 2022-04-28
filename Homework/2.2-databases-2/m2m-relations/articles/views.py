from django.shortcuts import render

from articles.models import Article


# def articles_list(request):
#     context = {
#         'object_list': Article.objects.order_by('-published_at').all()
#     }
#     return render(request, 'articles/news.html', context)
def articles_list(request):
    template = 'articles/news.html'
    articles = Article.objects.all().prefetch_related('scopes').order_by('-published_at')

    for article in articles:
        for scope in article.scopes.all():
            article_set = scope.tag.get(article=article)
            scope.is_main = article_set.is_main

    context = {'object_list': articles}

    ordering = '-published_at'

    return render(request, template, context)

