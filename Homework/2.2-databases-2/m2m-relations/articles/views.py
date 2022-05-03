from pprint import pprint

from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    # pprint(Article.objects.scopes.all())
    articles = Article.objects.all().prefetch_related('scopes').order_by('-published_at')
    pprint(articles)
    for article in articles:
        print(f'article  -------------   {article}')
        for scope in article.scopes.all():
            print(f'scope  -------------   {scope}')
            article_set = scope.tag.get(article=article)
            print(f'article_set  -------------   {article_set}')
            scope.is_main = article_set.is_main
            print(f'scope.is_main  -------------   {scope.is_main}')
            print(f'article_set.is_main  -------------   {article_set.is_main}')
    context = {
        'object_list': articles
    }
    return render(request, 'articles/news.html', context)
