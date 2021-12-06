from django.urls import path 
from . import views

urlpatterns = [
  path('',views.sellerProfile, name = "sellerProfile"),
  path('addproduct/', views.addNewProduct, name='addproduct'),
  path('addcredits/', views.addcredits, name='addcredits'),
  path('buyproduct/', views.buyproduct, name='buyproduct'),
]