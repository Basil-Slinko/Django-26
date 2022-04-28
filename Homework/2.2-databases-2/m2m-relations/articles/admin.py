from django.contrib import admin
from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, TagArticles


class ArticleScopeInline(admin.TabularInline):
    model = TagArticles
    extra = 3


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'published_at', 'image', ]
    search_fields = ['text']
    inlines = [ArticleScopeInline]

    # def clean(self):
    #     for form in self.forms:
    #         '''В form.cleaned_data будет словарь с данными
    #         каждой отдельной формы, которые вы можете проверить'''
    #         print('-------')
    #         print('-------')
    #         form.cleaned_data
    #         print('-------')
    #         print('-------')
    #         '''вызовом исключения ValidationError можно указать админке о наличие ошибки
    #         таким образом объект не будет сохранен,
    #         а пользователю выведется соответствующее сообщение об ошибке'''
    #         raise ValidationError('Тут всегда ошибка')
    #     return super().clean()  # вызываем базовый код переопределяемого метода
