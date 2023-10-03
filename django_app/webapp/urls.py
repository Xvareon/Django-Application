from django.urls import path
from webapp import views

urlpatterns = [
    path('products', views.index, name="index"),
    path('products/create', views.create, name="create"),
    path('products/update/<int:pk>', views.update, name='update'),
    path('products/delete/<int:pk>', views.delete, name='delete'),
    path('products/view/<int:pk>', views.view, name='view'),
]
