from django.urls import path
from webapp import views

urlpatterns = [
    path('products', views.index, name="index"),
    path('products/create', views.create, name="create")
]
