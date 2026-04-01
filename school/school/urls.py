from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # لوحة تحكم الأدمن
    path('admin/', admin.site.urls),
    
    # ربط كاع الـ Apps اللي عندك
    path('', include('faculty.urls')), # الصفحة الرئيسية غالبا هنا
    path('student/', include('student.urls')),
    path('authentication/', include('home_auth.urls')),
    path('teacher/', include('teacher.urls')),
    path('planning/', include('planning.urls')),
    path('departements/', include('departement.urls')),
    path('subjects/', include('subjects.urls')),
]

# هاد الجزء هو اللي كيخلي التصاور (Media) والملفات (Static) يخدموا في مرحلة التطوير
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)