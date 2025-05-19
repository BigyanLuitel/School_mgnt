"""
URL configuration for TVS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from school import views as school_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',school_views.home,name='home'),
    path('admission/',school_views.admission,name='admission'),
    path('update_records/<int:student_id>/', school_views.update_records, name='update_records'),
    path('delete_records/<int:student_id>/', school_views.delete_records, name='delete_records'),
    path('student_details/',school_views.student_details,name='student_details'),
    path('library', school_views.library, name='library'),
    path('library_management/<int:id>/',school_views.library_management,name='library_management'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
