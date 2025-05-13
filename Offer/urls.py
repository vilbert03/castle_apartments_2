from django.urls import path
from . import views

app_name = 'Offer'

urlpatterns = [
    path('', views.offer_list, name='list'),
]