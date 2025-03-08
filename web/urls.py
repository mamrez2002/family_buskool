from django.urls import path
from .views import login_view, welcome_view , home ,logout_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('welcome/', welcome_view, name='welcome'),
    path('', home, name='home'),
    path("logout/", logout_view, name="logout"),
]