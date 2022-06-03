from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'froyo_contact'

urlpatterns = [
    path('contact/', views.contact, name='contact'),
]

urlpatterns += staticfiles_urlpatterns()
