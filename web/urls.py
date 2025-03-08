from django.urls import path
from .views import login_view, welcome_view , home

urlpatterns = [
    path('login/', login_view, name='login'),
    path('welcome/', welcome_view, name='welcome'),
    path('', home, name='home'),
]