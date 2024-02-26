from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('projects/', views.projects, name='projects'),
    path('', views.about, name='about'),
    path('education/', views.education, name='home'),
    path('certifications/', views.certifications, name='certifications'),
    path('skills/', views.skills, name='skills'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)