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
      username=request.POST['username']
      email=request.POST['email']
      password=request.POST['password']
      cpass=request.POST['cpass']
      #username length
    

      if len(username)>13:
        messages.error(request, 'Maximum username 0-13*')
        return redirect('/signup')
        #username validation
      if not username.isalnum():
        messages.error(request, 'Username only contain numbers and letters*')
        return redirect('/signup')
        #password strength
      if re.search(r'^[A-Za-z0-9_-]+$', password):
        messages.error(request, 'Password must contain upcase lower case and symbles*')
        return redirect('/signup') 
        #password validation
      if password != cpass:
          messages.error(request, 'Password is not same*')
          return redirect('/signup')
      
      user = User.objects.create_user(username, email, password)
      user.save()
      return render(request, 'store/index.html')
      return redirect('#')
     
         

        
      # return render(request, 'user.html')
      # return redirect('/user')
    # return render(request, 'signup.html')
        
      
        
      # return render(request, 'user.html')
      # return redirect('/user')
      # return render(request, 'store/auth/signup.html')

    return render(request, 'store/auth/signup.html')