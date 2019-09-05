from django.shortcuts import get_object_or_404, render
from contribution.models import Contribution
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

def index(request):
    contribution = Contribution.objects.order_by('-post_date').filter(is_published=True)
    # contribution = Contribution.objects.all()

    paginator = Paginator(contribution, 1)
    page = request.GET.get('page')
    paged_contributions = paginator.get_page(page)

    
    paginator = Paginator(contribution, 2)
    page = request.GET.get('page')
    paged_contributions = paginator.get_page(page)

    context = {
        'contribution': paged_contributions
    }

    return render(request, 'pages/index.html', context)

def about(request):
    return render(request, 'pages/about.html')

def projects(request):
    return render(request, 'pages/projects.html')

def contribution(request, contribution_id):
    contribution = get_object_or_404(Contribution, pk=contribution_id)
    context = {
        'contribution': contribution
    }
    return render(request, 'pages/contribution.html', context)
