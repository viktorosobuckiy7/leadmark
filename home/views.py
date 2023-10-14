from django.shortcuts import render, HttpResponse, redirect
from .models import Service, Portfolio, AboutUs, Blog
from .forms import UserReservationForm
# Create your views here.


def home(request):
    if request.method == 'POST':
        reservation = UserReservationForm(request.POST)
        if reservation.is_valid():
            reservation.save()
            return redirect('/')

    services = Service.objects.all()[:3]
    portfolios = Portfolio.objects.all()
    about_us = AboutUs.objects.all()
    blogs = Blog.objects.all()[:3]
    reservation = UserReservationForm()

    data = {
        'services': services,
        'portfolios': portfolios,
        'about_us': about_us,
        'blogs': blogs,
        'reservation_form': reservation,
    }
    return render(request, 'home.html', context=data)


def about(request):
    return render(request, 'about.html')


def service(request):
    return render(request, 'service.html')


def contact(request):
    return render(request, 'contact.html')


def portfolio(request):
    return render(request, 'portfolio.html')


def testemonial(request):
    return render(request, 'testemonial.html')

