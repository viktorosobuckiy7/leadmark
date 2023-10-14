from django.shortcuts import render, redirect, HttpResponse
from home.models import UserReservation


def reservations_list(request):
    lst = UserReservation.objects.filter(is_processed=False)
    return render(request, 'reservations_list.html', context={
        'lst': lst,
    })


def update_reservation(request, pk):
    UserReservation.objects.filter(pk=pk).update(is_processed=True)
    return redirect('manager:reservations_list')


def manager(request):
    return HttpResponse('Hello')

