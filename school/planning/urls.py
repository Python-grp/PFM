from django.urls import path
from . import views

urlpatterns = [
    path('holidays/', views.holiday_list, name='holidays'),
    path('timetable/', views.timetable_view, name='timetable'),
]