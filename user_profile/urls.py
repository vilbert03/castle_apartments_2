from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name="user/login.html"), name='login'),
    path('logout/', LogoutView.as_view(next_page='home:index'), name='logout'),
    path('my_profile/', views.profile_view, name='my_profile'),
]
