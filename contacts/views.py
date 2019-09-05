from django.shortcuts import render, redirect
from django.contrib import messages

from categories.models import Categories
from contribution.models import Contribution

def contact(request):
    object_list = Categories.objects.all()
    context = {
        'object_list': object_list
    }
    return render(request, 'accounts/dashboard.html', context)

    if request.method == 'POST':
        user_id = request.POST['user_id']
        category_id = request.POST['category_id']
        title = request.POST['title']
        description = request.POST['description']
        photo = request.POST['photo']

        contribution = Contribution(category_id=category_id, user_id=user_id, title=title, description=description, photo=photo)
        contribution.save()
        messages.success(request, 'You have submitted your contribution')
        return redirect(request, 'accounts/dashboard.html')
