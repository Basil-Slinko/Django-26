from django.views.generic import ListView
from django.shortcuts import render

from .models import Student, Teacher


def students_list(request):
    context = {
        'object_list': Teacher.objects.order_by('name', 'subject').all()
    }
    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    # ordering = 'group'               prefetch_related('teachers').

    return render(request, 'school/students_list.html', context)
