from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'froyo_product'

urlpatterns = [
    path('product/', views.product, name='product'),
]

urlpatterns += staticfiles_urlpatterns()
