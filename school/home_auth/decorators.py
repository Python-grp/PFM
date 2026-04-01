from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from django.contrib import messages

def get_dashboard_redirect(user):
    if hasattr(user, 'is_admin') and user.is_admin:
        return redirect('admin_dashboard')
    elif hasattr(user, 'is_teacher') and user.is_teacher:
        return redirect('teacher_dashboard')
    elif hasattr(user, 'is_student') and user.is_student:
        return redirect('student_dashboard')
    return redirect('login')

def admin_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            from django.contrib.auth.views import redirect_to_login
            return redirect_to_login(request.get_full_path())
        if hasattr(request.user, 'is_admin') and request.user.is_admin:
            return view_func(request, *args, **kwargs)
        
        messages.error(request, "Accès refusé. Cette section est réservée aux administrateurs.")
        return get_dashboard_redirect(request.user)
    return _wrapped_view

def teacher_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            from django.contrib.auth.views import redirect_to_login
            return redirect_to_login(request.get_full_path())
        if hasattr(request.user, 'is_teacher') and (request.user.is_teacher or request.user.is_admin):
            return view_func(request, *args, **kwargs)
        
        messages.error(request, "Accès refusé. Cette section est réservée aux enseignants.")
        return get_dashboard_redirect(request.user)
    return _wrapped_view

def student_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            from django.contrib.auth.views import redirect_to_login
            return redirect_to_login(request.get_full_path())
        if hasattr(request.user, 'is_student') and (request.user.is_student or request.user.is_admin):
            return view_func(request, *args, **kwargs)
        
        messages.error(request, "Accès refusé. Cette section est réservée aux étudiants.")
        return get_dashboard_redirect(request.user)
    return _wrapped_view
