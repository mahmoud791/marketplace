from django.urls import path 
from . import views

urlpatterns = [
  path('',views.sellerProfile, name = "sellerProfile"),
  path('addproduct/', views.addNewProduct, name='addproduct')
]