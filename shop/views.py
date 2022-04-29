from django.shortcuts import render, HttpResponse,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import re
# Create your views here.




def blog(request):
    return HttpResponse('blog')
    
   
    return render(request, "store/blog/post.html",)
def home(request):
    
    return render(request, "store/collections.html")

def collections(request):
    category=Category.objects.filter(status=0)
    context={"category":category}
    return render(request, 'store/collections.html', context )

def collectionsview(request, slug):
  if request.method=='POST':
    prod_id=request.POST.get('proid')
    
  else:
    if(Category.objects.filter(slug=slug, status=0)):
      products=Product.objects.filter(category__slug=slug)
      category_name=Category.objects.filter(slug=slug).first()
      contex={"products":products,"category_name":category_name}
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
  if request.user.is_authenticated:
    messages.error(request, "You already have an account")
    return redirect("/collections")
  else:
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
        messages.error(request, f'{username} is not valid username Maximum   0-13 charcter allowed*')
        return redirect('/signup')
        #username validation
          
      if not username.isalnum():
        messages.error(request, 'Username only contain numbers and letters*')
        return redirect('/signup')
      if re.search(r'^[A-Za-z0-9_-]+$', password):
        messages.error(request, 'Password must contain upcase lower case and symbles*')
        return redirect('/signup')
    
      try:
        user = User.objects.create_user(username, email, password)
        user.save()
        return redirect('/userlogin')
      except Exception as e:
        messages.error(request, f'{username} username is not valid.Try another username')
        return redirect('/signup')

      

      
      
    return render(request, 'store/auth/signup.html')

def userlogin(request):
  if request.user.is_authenticated:
    messages.error(request, "You are already logedin")
    return redirect("/collections")
  else:
    if request.method=='POST':
     username=request.POST.get('username')
     password=request.POST.get('password')
     user=authenticate(username=username,password=password)
     if user is not None:
      login(request, user)
      return redirect('/collections' )   
     else:
       messages.error(request, "Seems Like password or username incorrect")
       return redirect("/userlogin")
    return render(request, "store/auth/login.html")


def us_logout(request):
  if request.user.is_authenticated:  
   logout(request)
   messages.error(request, "Logout successfuly")
   return redirect('/collections')
    

def profile_view(request):
  if request.user.is_authenticated:
   return render(request, "store/auth/profile.html")
  else:
    return HttpResponse("Error 404 page not found")
