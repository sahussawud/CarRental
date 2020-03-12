
from django.contrib.auth.decorators import permission_required, login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .models import Car,Rent


# Create your views here.
@login_required
@permission_required('managecar.change_car')
def car_hide(request, id_car):
    car = Car.objects.get(pk=id_car)
    car.status = 'HIDE'
    car.save()
    return redirect('car_dashboard')

@login_required
@permission_required('managecar.change_car')
def car_unhide(request, id_car):
    car = Car.objects.get(pk=id_car)
    car.status = 'AVAILABLE'
    car.save()
    return redirect('car_dashboard')

@login_required
@permission_required('managecar.change_car')
def home_car_hide(request, id_car):
    car = Car.objects.get(pk=id_car)
    car.status = 'HIDE'
    car.save()
    return redirect('homepage')

@login_required
@permission_required('managecar.change_car')
def notavailable(request, id_rent):
    rent = Rent.objects.get(pk=id_rent)
    car = Car.objects.get(pk=rent.car_id.id)
    car.status = 'NO_AVAILABLE'
    car.save()
    return redirect('dashboard')

@login_required
@permission_required('managecar.change_car')
def available(request, id_rent):
    rent = Rent.objects.get(pk=id_rent)
    car = Car.objects.get(pk=rent.car_id.id)
    car.status = 'AVAILABLE'
    car.save()
    return redirect('dashboard')

@login_required
@permission_required('managecar.change_car')
def car_dashboard(request):
    context = {}
    available = []
    not_available = []
    hidden = []
    cars = Car.objects.all()
    for car in cars:
        if car.status == 'AVAILABLE':
            available.append(car)
        elif car.status == 'NO_AVAILABLE':
            not_available.append(car)
        elif car.status == 'HIDE':
            hidden.append(car)
    if len(available): context['available'] = available
    if len(not_available): context['not_available'] = not_available
    if len(hidden): context['hidden'] = hidden

    return render(request, 'managecar/car_dashboard.html', context=context)
