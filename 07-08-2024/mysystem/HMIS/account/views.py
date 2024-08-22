from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login as auth_login, logout
from django.http import HttpResponse
from django.core.cache import cache
from django.contrib.auth.decorators import login_required

# Function for login

def login(request):
    remembered_email = ""
    remembered_password = ""
    error_message = ""

    if request.method == 'POST':
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        remember_me = request.POST.get('remember_me') == 'true'

        if email and password:
            # Authenticate the user
            user = authenticate(request, email=email, password=password)
            if user is not None:
                # Log the user in
                auth_login(request, user)

                # Save the email and password if 'Remember me' is checked
                if remember_me:
                    request.session['remembered_email'] = email
                    request.session['remembered_password'] = password
                else:
                    request.session['remembered_email'] = ""
                    request.session['remembered_password'] = ""

                # Redirect based on user role
                if request.user.role == 'Doctor':
                    return redirect('/addbiodata')
                elif request.user.role == 'SuperAdmin':
                    return redirect('/viewusers')
                elif request.user.role == 'None':
                    return redirect('/biodata')
            else:
                # Authentication failed
                error_message = "Invalid email or password."
        else:
            error_message = "Both email and password are required."

    # Handle GET request or if the POST request fails
    remembered_email = request.session.get('remembered_email', '')
    remembered_password = request.session.get('remembered_password', '')
    
    return render(request, 'accounts/login.html', {
        'remembered_email': remembered_email,
        'remembered_password': remembered_password,
        'error_message': error_message,
    })

def custom_logout_view(request):
    request.session.flush()
    cache.clear()
    logout(request)
    return redirect('/')

# Function for creating users
def adduser(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        role = request.POST.get('role', '')
        password = request.POST.get('password', '')
        confirm_password = request.POST.get('confirm-password', '')

        if name and email and phone and role and password and confirm_password:
            if password == confirm_password:
                try:
                    User = get_user_model()
                    user = User.objects.create_user(name=name, email=email, phone=phone, role=role, password=password)
                    print('User created:', user)
                    return redirect('/login/')
                except Exception as e:
                    print('Error creating user:', str(e))
                    return HttpResponse(f"An error occurred while creating the user: {str(e)}")
            else:
                print('Passwords do not match.')
                return HttpResponse("Passwords do not match.")
        else:
            print('All fields are required.')
            return HttpResponse("All fields are required.")
    
    return render(request, 'accounts/adduser.html')

def signup(request):
    return render(request, 'accounts/adduser.html')

def viewusers(request):
    User = get_user_model()
    users = User.objects.all()
    return render(request, 'core/index.html', {'users': users})
