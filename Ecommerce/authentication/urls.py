from django.urls import path 
from . import views

urlpatterns = [
  path('login',views.login_page, name = "login"),
  path('logout',views.log_out, name = "logout"),
  path('register',views.register,name = "register"),
  path('createuser',views.test_user_creation,name = "testing_user"),
  path('api/users',views.User_list,name='api')
]