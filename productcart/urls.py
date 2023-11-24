from django.urls import path
from . import views

app_name = "productcart"


urlpatterns=[
    path('', views.checkout, name='checkout'),
]