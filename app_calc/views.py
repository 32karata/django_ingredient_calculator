from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}

def calculate_recipe(recipe_name, servings=1):
    """Рассчитывает ингредиенты для указанного количества порций"""
    if recipe_name not in DATA:
        return {}
    
    recipe = DATA[recipe_name].copy()
    if servings > 1:
        for ingredient in recipe:
            recipe[ingredient] *= servings
    return recipe

def omlet(request):
    servings = int(request.GET.get('servings', 1))
    context = {
        'recipe': calculate_recipe('omlet', servings)
    }
    return render(request, 'home.html', context)

def pasta(request):
    servings = int(request.GET.get('servings', 1))
    context = {
        'recipe': calculate_recipe('pasta', servings)
    }
    return render(request, 'home.html', context)

def buter(request):
    servings = int(request.GET.get('servings', 1))
    context = {
        'recipe': calculate_recipe('buter', servings)
    }
    return render(request, 'home.html', context)