from django.shortcuts import render, HttpResponse,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import re
# Create your views here.




def blog(request):
    
   
    return render(request, "store/blog/post.html",)
def home(request):
    
    return render(request, "store/index.html")

def collections(request):
    category=Category.objects.filter(status=0)
    context={"category":category}
    return render(request, 'store/collections.html', context )

def collectionsview(request, slug):
    if(Category.objects.filter(slug=slug, status=0)):
      products=Product.objects.filter(category__slug=slug)
      category_name=Category.objects.filter(slug=slug).first()
      contex={"products":products,"category_name":category_name}
      print(products)
      return render(request, "store/product/index.html", contex)
    else:
     return HttpResponse('This is not a valid product')
    

def productview(request, cate_slug, prod_slug):
    if(Category.objects.filter(slug=cate_slug, status=0)):
        if(Product.objects.filter(slug=cate_slug, status=0)):
          products=Product.objects.filter(name=prod_slug, status=0).first()
          contex={"products":products}
        else:
         messages.error(request, "error 404 page Not found")
        
    else:
        messages.error(request, "error 404 page Not found")
        return redirect('collections')
    
    return render(request, "store/product/proview.html", contex)


def signup(request):
    if request.method=='POST':
      username=request.POST.get('username')
      email=request.POST.get('email')
      password=request.POST.get('password')
      cpass=request.POST.get('cpass')
      #username length   
      if(password != cpass):
        messages.error(request, "Seems Like password is not same")
        redirect("/signup")
        # user name length
      if len(username)>13:
        messages.error(request, 'Maximum username 0-13*')
        return redirect('/signup')
        #username validation
          
      if not username.isalnum():
        messages.error(request, 'Username only contain numbers and letters*')
        return redirect('/signup')
      if re.search(r'^[A-Za-z0-9_-]+$', password):
        messages.error(request, 'Password must contain upcase lower case and symbles*')
        return redirect('/signup')
      else:
       try:
        user = User.objects.create_user(username, email, password)
        user.save()
        return render(request, 'store/auth/login.html')
       except Exception as e:
        messages.error(request, 'Try another username')
        return redirect('/signup')

      

      
      
    return render(request, 'store/auth/signup.html')

def user_login(request):
    if request.method=='POST':
     username=request.POST.get('username')
     password=request.POST.get('password')
     user=authenticate(username=username,password=password)
     if user is not None:
        login(request, user)
        return render(request, "store/t.html")
        return redirect("/user_login")
     else:
       messages.error(request, "Seems Like password or username incorrect")
    return render(request, "store/auth/login.html")
     

def us_logout(request, user_username):
    return HttpResponse(f"Dear {user_username} you are succesfuly logout")
    