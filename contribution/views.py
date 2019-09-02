from django.shortcuts import get_object_or_404, render
from .models import Contribution

def contributions(request):

    return render(request, 'contribution/contributions.html')

def contribution(request, contribution_id):
    contribution = get_object_or_404(Contribution, pk=contribution_id)
    context = {
        'contribution': contribution
    }
    return render(request, 'contribution/contribution.html', context)
