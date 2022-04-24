from django.urls import path
from nusmap import views

urlpatterns = [
   
   path('', views.home, name="home"),
   path('collections', views.collections, name="collections"),
   path('blog', views.blog, name="blog"),
   path('collections/<str:slug>', views.collectionsview, name="collectionsview"),
   path('Product_View/<str:cate_slug>/<str:prod_slug>', views.productview, name="productview"),
   path('signup', views.signup, name="signup"),

  
]