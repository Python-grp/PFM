from django.urls import path
from . import views

urlpatterns = [
    # Exams
    path('exams/', views.ExamListView.as_view(), name='exam-list'),
    path('exams/add/', views.ExamCreateView.as_view(), name='exam-add'),
    path('exams/<int:pk>/edit/', views.ExamUpdateView.as_view(), name='exam-edit'),
    path('exams/<int:pk>/delete/', views.ExamDeleteView.as_view(), name='exam-delete'),

    # Results
    path('results/', views.ResultListView.as_view(), name='result-list'),
    path('results/add/', views.ResultCreateView.as_view(), name='result-add'),
    path('results/<int:pk>/edit/', views.ResultUpdateView.as_view(), name='result-edit'),
    path('results/<int:pk>/delete/', views.ResultDeleteView.as_view(), name='result-delete'),
]
