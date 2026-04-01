from django.contrib.auth.mixins import AccessMixin
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

class AdminRequiredMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        if hasattr(request.user, 'is_admin') and request.user.is_admin:
            return super().dispatch(request, *args, **kwargs)
            
        messages.error(request, "Accès refusé. Action réservée aux administrateurs.")
        return get_dashboard_redirect(request.user)

class AdminOrTeacherRequiredMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        if hasattr(request.user, 'is_admin') and (request.user.is_admin or getattr(request.user, 'is_teacher', False)):
            return super().dispatch(request, *args, **kwargs)
            
        messages.error(request, "Accès refusé. Action réservée aux enseignants ou administrateurs.")
        return get_dashboard_redirect(request.user)
