from django.urls import path
from shop import views

urlpatterns = [
   
   path('', views.collections, name="home"),
   path('collections', views.collections, name="collections"),
   path('collections/<str:slug>', views.collectionsview, name="collectionsview"),
   path('Product_View/<str:cate_slug>/<str:prod_slug>', views.productview, name="productview"),
   path('signup/', views.signup, name="signup"),
   path('us_logout/', views.us_logout, name="us_logout"),
   path('userlogin/', views.userlogin, name="userlogin"),
   path("profile_view/", views.profile_view, name="profile_view"),

  
]