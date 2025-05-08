from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='Property-index'),
    path('<int:id>', views.get_property_by_id, name='property_by_id'),
]
