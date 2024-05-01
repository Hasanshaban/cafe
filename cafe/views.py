from django.shortcuts import render
from .forms import ReservationForm

# Create your views here.
def homeview(request):
    return render(request,'cafe/index.html')
def reservationview(request):
    reservation_form=ReservationForm()
    if request.method=='POST':
        reservation_form=ReservationForm(request.POST)
        if reservation_form.is_valid():
            reservation_form.save()
    else:
        reservation_form=ReservationForm()

    context={
        'form':reservation_form
    }
    return render(request,'cafe/reservation.html',context)