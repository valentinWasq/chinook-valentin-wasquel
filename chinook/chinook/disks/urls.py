from django.urls import path

from . import views

app_name = 'disks'
urlpatterns = [
    # ex: /disks/
    path('', views.IndexView.as_view(), name='Index'),
    # ex: /disks/5/
    path('<int:pk>/', views.detailView.as_view(), name='detail'),
    # ex: /disks/Recherche/Wild/
    path('Recherche/<rechercheText>/', views.recherche, name='recherche')
]