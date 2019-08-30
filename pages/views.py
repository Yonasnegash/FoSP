from django.shortcuts import render
from contribution.models import Contribution
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

def index(request):
    contribution = Contribution.objects.all()

    paginator = Paginator(contribution, 1)
    page = request.GET.get('page')
    paged_contributions = paginator.get_page(page)

    
    context = {
        'contribution': paged_contributions
    }

    return render(request, 'pages/index.html', context)

def about(request):
    return render(request, 'pages/about.html')
