from django.urls import path

from . import views

app_name = 'property'

urlpatterns = [
    path('', views.index, name='property_list'),
    #path('', views.index, name='Property-index'),
    path('<int:id>', views.get_property_by_id, name='property_by_id'),

    path('<int:id>/make_an_offer', views.make_an_offer, name='make_an_offer'),


]
