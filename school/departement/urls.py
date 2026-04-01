from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.departement_list, name='departement_list'),
    path('add/', views.add_departement, name='add_departement'),
    path('edit/<int:pk>/', views.edit_department, name='edit_department'),
    path('delete/<int:pk>/', views.delete_departement, name='delete_departement'),
]