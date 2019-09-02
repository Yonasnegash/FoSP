from django.urls import path

from . import views

urlpatterns = [
    path('', views.contributions, name='contributions'),
    path('<int:contribution_id>', views.contribution, name='contribution'),
]