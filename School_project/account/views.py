from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,logout,login
from .forms import RegisterUserForm
from django.contrib.auth.models import Group



def login_now(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is None:
            print("user is not available")
            return render(request,'accounts/login.html')
        else:
            login(request,user)
            return redirect('landing_page')
    else:
        print("This is not POST method")

    return render(request, 'accounts/login.html')

def register_now(request):
    form = RegisterUserForm()
    if request.method == 'POST':
        select = request.POST.get("selection")
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            if select == "Teacher":
                group = Group.objects.get(name="Teacher")
                user.groups.add(group)
            elif select == "Student":
                group = Group.objects.get(name="Student")
                user.groups.add(group)
            return redirect('login')
        else:
            print("Please enter correct form of data")
    return render(request, 'accounts/register.html',{'form':form})

def logout_user(request):
    logout(request)
    return redirect('landing_page')