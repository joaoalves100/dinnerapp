from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Meals
from .models import People
def index(request):
    meals_available = Meals.objects.all()
    context = {'meals_available': meals_available}
    return render(request, 'reservations/index.html', context)


def meal(request, meal_id):
    meal_selected = Meals.objects.get(id=meal_id)
    #context = {'meals_available': meals_available}
    #return render(request, 'reservations/index.html', context)
    response = "You're looking at the meal %s."
    return HttpResponse(response % meal_selected.meal_description)

def people (request,people_id):
    response = "You're looking at the people %s."
    return HttpResponse(response % people_id)
