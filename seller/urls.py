from django.urls import path
from . import views

app_name = 'seller'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.get_seller_by_id, name='detail'),
]