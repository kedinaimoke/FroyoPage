"""froyosite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('froyo_home/', include('froyo_home.urls', namespace='froyo_home')),
    path('froyo_about/', include('froyo_about.urls', namespace='froyo_about')),
    path('froyo_product/', include('froyo_product.urls', namespace='froyo_product')),
    path('froyo_blog/', include('froyo_blog.urls', namespace='froyo_blog')),
    path('froyo_contact/', include('froyo_contact.urls', namespace='froyo_contact')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
