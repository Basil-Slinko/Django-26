from django.shortcuts import render


def omlet_view(request, count_person):
    context = {
        'recipe': {
            'omlet': {
                'яйца, шт': 2 * count_person,
                'молоко, л': round((0.1 * count_person), 2),
                'соль, ч.л.': round((0.5 * count_person), 2),
            },
        }
    }
    return render(request, 'calculator/index.html', context)


def pasta_view(request, count_person):
    context = {
        'recipe': {
            'pasta': {
                'макароны, г': round((0.3 * count_person), 2),
                'сыр, г': round((0.05 * count_person), 2),
            }
        }
    }
    return render(request, 'calculator/index.html', context)


def buter_view(request, count_person):
    context = {
        'recipe': {
            'buter': {
                'хлеб, ломтик': 1 * count_person,
                'колбаса, ломтик': 1 * count_person,
                'сыр, ломтик': 1 * count_person,
                'помидор, ломтик': 1 * count_person,
            }
        }
    }
    return render(request, 'calculator/index.html', context)
