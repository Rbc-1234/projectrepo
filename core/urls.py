from django.contrib import admin
from django.urls import path,include
from .views import Pr_home,Pr_Add,EditProduct

urlpatterns = [
    path('',Pr_home.as_view(),name="home"),
    path('addproduct',Pr_Add.as_view(),name="addproduct"),
    path('edit-product/<int:id>/', EditProduct.as_view(), name='edit-product'),
   
]