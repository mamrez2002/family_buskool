from django.shortcuts import render , redirect
from django.contrib.auth import authenticate , login , logout
import hashlib
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import FitLog
from django.contrib.auth.decorators import login_required
from .forms import FitLogForm
import jdatetime
# Create your views here.


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            response = redirect('home')
            user_hash = hashlib.sha256(f"{user.username}{user.id}".encode()).hexdigest()
            response.set_cookie('user_token', user_hash, max_age=604800, httponly=True)

            return response
        else:
            return render(request, 'login.html',{'error':"نام کاربری یا رمزعبور اشتباه است"})
    return render(request, 'login.html')


def welcome_view(request):
    user_token = request.COOKIES.get('user_token')

    if user_token:
        for user in User.objects.all():
            valid_token = hashlib.sha256(f"{user.username}{user.id}".encode()).hexdigest()
            if user_token == valid_token:
                return HttpResponse(f"{user.username} welcome!")
    return redirect('login')




@login_required(login_url='/login/')
def home(request):
    if request.method == "POST":
        form = FitLogForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('home')
    else:
        form = FitLogForm()
    measurements = FitLog.objects.filter(user=request.user).order_by('-date')

    for item in measurements:
        item.shamsi_date = jdatetime.datetime.fromgregorian(datetime=item.date).strftime('%Y/%m/%d %H:%M')
    return render(request, "home.html", {"form": form, "measurements": measurements , "username": request.user.username})



def logout_view(request):
    logout(request)
    return redirect("login")