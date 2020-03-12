from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import redirect, render

from managecar.models import Rent

# Create your views here.

@login_required
@permission_required('managecar.change_rent')
@permission_required('managecar.change_car')
def dashboard(request):
    context = {}
    Rents = Rent.objects.all().order_by('-id')
    context['Rents'] = Rents
    if request.method == 'POST':
        details = int(request.POST.get('details'))
        rental = Rent.objects.get(pk=details)
        context['details'] = rental
    return render(request, 'dashboard/dashboard.html', context=context)

@login_required
@permission_required('managecar.change_rent')
def rent_approve(request, id_rent):
    rent_order = Rent.objects.get(pk=id_rent)
    rent_order.status = 'Approved'
    rent_order.save()
    return redirect('dashboard')

@login_required
@permission_required('managecar.change_rent')
def rent_deniel(request, id_rent):
    rent_order = Rent.objects.get(pk=id_rent)
    rent_order.status = 'Denied'
    rent_order.save()
    return redirect('dashboard')
