from django.urls import path
from . import views

urlpatterns = [
    # Holidays
    path('holidays/', views.HolidayListView.as_view(), name='holiday-list'),
    path('holidays/add/', views.HolidayCreateView.as_view(), name='holiday-add'),
    path('holidays/<int:pk>/edit/', views.HolidayUpdateView.as_view(), name='holiday-edit'),
    path('holidays/<int:pk>/delete/', views.HolidayDeleteView.as_view(), name='holiday-delete'),

    # TimeTable
    path('timetable/', views.TimeTableListView.as_view(), name='timetable-list'),
    path('timetable/add/', views.TimeTableCreateView.as_view(), name='timetable-add'),
    path('timetable/<int:pk>/edit/', views.TimeTableUpdateView.as_view(), name='timetable-edit'),
    path('timetable/<int:pk>/delete/', views.TimeTableDeleteView.as_view(), name='timetable-delete'),
]