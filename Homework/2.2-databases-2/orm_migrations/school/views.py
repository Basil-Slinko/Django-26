from django.views.generic import ListView
from django.shortcuts import render

from .models import Student, Teacher


def students_list(request):
    context = {
        'object_list': Student.objects.prefetch_related('teachers').order_by('name', 'group').all()
    }
    return render(request, 'school/students_list.html', context)
