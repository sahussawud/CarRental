
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Q
from django.shortcuts import render

from managecar.models import Car


# Create your views here.
def homepage(request):
    context = {}
    cars = {}
    if request.method == 'POST':
        select = request.POST.get('selection')
        keyword = request.POST.get('keyword')
        context['keyword'] = keyword
        context['selection'] = select
        if request.user.is_superuser == True or request.user.is_staff == True:
            if select == 'year':
                cars = Car.objects.filter(years=keyword)
            elif select == 'color':
                cars = Car.objects.filter(color__icontains=keyword)
            elif select == 'name':
                cars = Car.objects.filter(name__icontains=keyword)
            else:
                cars = Car.objects.filter(  Q(years__contains=keyword) |
                                            Q(color__contains=keyword) |
                                            Q(name__icontains=keyword))
        else:
            if select == 'year':
                cars = Car.objects.filter(years=keyword).exclude(status='HIDE')
            elif select == 'color':
                cars = Car.objects.filter(color__icontains=keyword).exclude(status='HIDE')
            elif select == 'name':
                cars = Car.objects.filter(name__icontains=keyword).exclude(status='HIDE')
            else:
                cars = Car.objects.filter(  Q(years__contains=keyword) |
                                            Q(color__contains=keyword) |
                                            Q(name__icontains=keyword))
    else:
        if request.user.is_superuser == True or request.user.is_staff == True:
            cars = Car.objects.all()
        else:
            cars = Car.objects.all().exclude(status='HIDE')
    context['cars'] = cars


    return render(request,'homepage/home.html',context=context)

@login_required
@permission_required('managecar.add_car')
def add_edit_car(request):
    return redirect('homepage')

@login_required
@permission_required('managecar.change_car')
def change_car(request):
    return redirect('homepage')

@login_required
@permission_required('managecar.change_car')
def car_detail(request, id_car):
    context = {}
    car = Car.objects.get(pk=id_car)
    context['car'] = car
    return render(request, 'homepage/car_detail.html',context=context)

def handler404(request, exception, template_name="404.html"):
    response = render_to_response(template_name)
    response.status_code = 404
    return response