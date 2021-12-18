from django.urls import path
from home import views

urlpatterns = [
    path('',views.homePage,name = 'home'),
    path('profile',views.user_profile, name = 'profile'),
    path('addproduct/', views.addNewProduct, name='addproduct'),
    path('addcredits/', views.addcredits, name='addcredits'),
    path('buyproduct/', views.buyproduct, name='buyproduct'),
    path('clothes',views.category,{'category':'clothes'},name='clothes'),
    path('shoes',views.category,{'category':'shoes'},name='shoes'),
    path('watches',views.category,{'category':'watches'},name='watches'),
    path('laptops',views.category,{'category':'laptops'},name='laptops'),
    path('mobile_phones',views.category,{'category':'mobile_phones'},name='mobile_phones'),
    path('headphones&headsets',views.category,{'category':'headphones&headsets'},name='headphones&headsets'),
    path('perfumes&deodrants',views.category,{'category':'perfumes&deodrants'},name='perfumes&deodrants'),
    path('accessories',views.category,{'category':'accessories'},name='accessories'),
    path('kid_toys',views.category,{'category':'kid_toys'},name='kid_toys'),
    path('household',views.category,{'category':'household'},name='household'),
    path('cart',views.cart,name = "cart"),
    path('checkout',views.checkout,name = "checkout"),
    path('update_item/',views.updateItem,name = "update_item"),
    path('product/<slug:slug>/',views.product_detail,name='product_detail'),
    path('search/',views.search,name="search"),
    path('api/products',views.product_list,name='api')
    
]