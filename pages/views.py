from django.shortcuts import render
from contribution.models import Contribution

def index(request):
    contribution = Contribution.objects.all()
    
    context = {
        'contributions': contribution
    }

    return render(request, 'pages/index.html', context)

def about(request):
    return render(request, 'pages/about.html')
