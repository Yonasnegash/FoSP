from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contribution.models import Contribution
from categories.models import Categories

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        conf_password = request.POST['conf_password']

        #check password match
        if password == conf_password:
            #check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'This email is taken')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, password=password, email=email,
                    first_name=first_name, last_name=last_name)
                    user.save()
                    messages.success(request, 'You are now registered and can log in')
                    return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now Logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('index')
    else:
        return 

# def dashboard_cat(request):
#     object_list = Categories.objects.all()
#     context = {
#         'object_list': object_list
#     }
#     return render(request, 'accounts/dashboard.html', context)

def dashboard(request):
    object_list = Contribution.objects.order_by('-post_date').filter(user_id=request.user.id)
    context = {
        'object_list': object_list
    }
    return render(request, 'accounts/dashboard.html')
    if request.method == 'POST':
        user_id = request.POST['user_id']
        category = request.POST['category']
        title = request.POST['title']
        description = request.POST['description']
        photo = request.POST['photo']

        contribution = Contribution(category_id=category, user_id=user_id, title=title, description=description, photo=photo)
        contribution.save()

        messages.success(request, 'You have submitted your contribution')
        return render(request, 'accounts/dashboard.html')
    # return render(request, 'accounts/dashboard.html')
    else:
        return render(request, 'accounts/dashboard.html')