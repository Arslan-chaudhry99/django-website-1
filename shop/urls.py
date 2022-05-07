from django.urls import path
from shop import views

urlpatterns = [
   
   path('', views.collections, name="home"),
   path('collections', views.collections, name="collections"),
   path('collections/<str:slug>', views.collections_view, name="collectionsview"),
   path('Product_View/<str:cate_slug>/<str:prod_slug>', views.product_view, name="productview"),
   path('signup/', views.signup, name="signup"),
   path('us_logout/', views.us_logout, name="us_logout"),
   path('userlogin/', views.user_login, name="userlogin"),
   path("profile/", views.profile_view, name="profile_view"),
   path("recover password/", views.reset_pass, name="reset_pass"),

  
]