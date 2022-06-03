from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'froyo_blog'

urlpatterns = [
    path('blog/', views.blog, name='blog'),
    path('singlepost/<int:pk>/', views.singlepost, name='singlepost'),
]

urlpatterns += staticfiles_urlpatterns()
