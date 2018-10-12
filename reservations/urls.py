from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('meal/<int:meal_id>/',views.meal,name='meal'),
    path('people/<int:people_id>/',views.people,name='people'),
]
