from django.contrib import messages
from django.shortcuts import render , redirect
from django.contrib.auth import authenticate, login, logout
from account.forms import Registerform
from django.contrib.auth.models import Group


# Create your views here.
# Register new user
def register(request):
    form = Registerform()

    if request.method == "POST":
        # get the data from the register input value
        form = Registerform(request.POST)
        # check whether valid or not
        if form.is_valid():
            # save the form
            user = form.save()
            
            group = Group.objects.get(name = 'student')

            user.groups.add(group)

            username = form.cleaned_data.get('username')
            messages.success(
                request, "An account was successfully created for " + username + " !")
            return redirect('/login/login_redirect')
    return render(request , 'user_account/register.html' , {'form' : form})

# Redirecting user to login page. 
def loginre(request):
    return render(request, "user_account/login.html")

# Log in
def loginfn(request):
    if request.user.is_authenticated:
        return redirect('/admin_side/admin_dashboard')
    else:
        return redirect('/login/login_redirect')

# Log in Validation
def validation(request):

    # getting data from the FORM inside the login.html file. 
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(request,username=username , password= password)

    # checking whether the user exists or not in django auth_user table
    if user is not None:
        login(request, user)
        return redirect('/admin_side/admin_dashboard')
    else:
        messages.info(request, 'Invalid Username or Password!')
        return redirect('/login/login_redirect')

# Loggin out
def logoutfn(request):
    logout(request)
    return redirect('/login/login_redirect')