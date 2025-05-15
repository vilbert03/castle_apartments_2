from django.urls import path
from . import views

app_name = 'Offer'

urlpatterns = [
    path('', views.offer_list, name='list'),
    path('make_an_offer/<int:property_id>/', views.make_an_offer, name='make_an_offer'),
    path('finalize/<int:offer_id>/step1/', views.finalize_step1, name='finalize_step1'),
    path('finalize/<int:offer_id>/step2/', views.finalize_step2, name='finalize_step2'),
    path('finalize/<int:offer_id>/review/', views.finalize_review, name='finalize_review'),
    path('finalize/success/', views.finalize_success, name='finalize_success'),
]
