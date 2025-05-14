from django.urls import path
from . import views

app_name = 'Offer'

urlpatterns = [
    path('', views.offer_list, name='list'),
    path('make_an_offer/<int:property_id>/', views.make_an_offer, name='make_an_offer'),
]
