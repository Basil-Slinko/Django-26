from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, TagArticles


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        counter = 0
        for form in self.forms:
            if form.cleaned_data['is_main']:
                counter += 1
        if counter == 0:
            raise ValidationError('Укажите основной раздел')
        elif counter > 1:
            raise ValidationError('Основным может быть только один раздел')
        return super().clean()


class ArticleScopeInline(admin.TabularInline):
    model = TagArticles
    formset = RelationshipInlineFormset
    extra = 0
    list_display = ['name', ]


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'published_at', 'image', ]
    search_fields = ['text']
    inlines = [ArticleScopeInline]


