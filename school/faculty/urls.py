from django.urls import path 
from . import views 

urlpatterns =[
  path('' , views.index , name="index"),
  path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
  path('teacher-dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
  path('student-dashboard/', views.student_dashboard, name='student_dashboard'),

  # Department URLs
  path('departments/', views.DepartmentListView.as_view(), name='department-list'),
  path('departments/add/', views.DepartmentCreateView.as_view(), name='department-add'),
  path('departments/<int:pk>/edit/', views.DepartmentUpdateView.as_view(), name='department-edit'),
  path('departments/<int:pk>/delete/', views.DepartmentDeleteView.as_view(), name='department-delete'),

  # Subject URLs
  path('subjects/', views.SubjectListView.as_view(), name='subject-list'),
  path('subjects/add/', views.SubjectCreateView.as_view(), name='subject-add'),
  path('subjects/<int:pk>/edit/', views.SubjectUpdateView.as_view(), name='subject-edit'),
  path('subjects/<int:pk>/delete/', views.SubjectDeleteView.as_view(), name='subject-delete'),
]