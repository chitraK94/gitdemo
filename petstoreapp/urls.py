from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('pets/', views.pets_list, name = 'pets_list'),
    path('pets/create/',views.pet_create, name = 'pet_create'),
    path('search/',views.search_results, name='search_results')
]
