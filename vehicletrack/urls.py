from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:vehicle_id>/', views.vehicledetail, name='vehicle detail'),
    # ex: /polls/5/results/
    path('<int:nav_id>/results/', views.navresults, name='nav results'),
]