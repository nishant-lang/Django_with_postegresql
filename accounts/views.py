
from django.contrib import messages
from django.shortcuts import  render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import views as auth_views




# Create your views here.
def login(request):
    if request.method =='POST':
        username=request.POST['username']
        
        password=request.POST['password']
        
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.info(request,'you are logedin')
            return redirect("/")
        else:
            messages.info(request,'invalid credentials') 
            return redirect('login')
    else:

        return render(request,"login.html")

def register(request):
    if request.method =='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        email=request.POST['email']

        if password1==password2:
            if User.objects.filter(username=username).exists():
               messages.info(request,'username allready taken') 
               return redirect('register')

            elif User.objects.filter(email=email).exists():
               messages.info(request,'email allready taken') 
               return redirect('register')
            else:
                user=User.objects.create_user(first_name=first_name,username=username, password=password1, email=email, last_name=last_name)

                user=auth.create_user_with_email_and_password(email=email,username=username,first_name=first_name,last_name=last_name)
                user.save()
                messages.info(request,'user created Sucessfully')
                return redirect('login')
        else:
            messages.info(request,'password not matching') 
            return redirect("register")
       
    else:     
       return render(request,"register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')


def about(request):
   return render(request,'about.html')


def password_reset(request):
    return render(request,"password_reset.html")
