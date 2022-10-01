from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.
def register(request):
    if request.method =="POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        user_name = request.POST["user_name"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

    ## Save the data
        if password1 == password2 :
            if User.objects.filter(username= user_name).exists():
                messages.info(request, "Username taken")
                return redirect('/accounts/register')

            elif User.objects.filter(email= email).exists():
                messages.info(request, "Email taken")
                return redirect('/accounts/register')
            else:
                user = User.objects.create_user(username =user_name,password=password1,email=email,first_name =first_name,last_name =last_name)
                user.save()
                messages.info(request, "User successfully created")
                return redirect('/accounts/register')
        else:
            messages.info(request, "Passwords are not matching")
        return redirect('/accounts/register')
    else:

        return render(request,'register.html')

def login(request):
    if  request.method == "POST":
        user_name = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username =user_name, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect('/', {"user":user.username})
        else:
            messages.info(request,"Invalid credentials")
            return redirect('/accounts/register')
    else:

        return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')