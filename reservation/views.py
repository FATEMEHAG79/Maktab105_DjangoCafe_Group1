from django.shortcuts import render
from . forms import ReservationForm

# Create your views here.
def reserve(request):
    reserve_form=ReservationForm()
    if request.method=="post":
        reserve_form=ReservationForm(request.POST)
        if reserve_form.is_valid():
            reserve_form.save()
    else:
        reserve_form=ReservationForm()

    
    
    context={
        "form":reserve_form,
    }
    return render(request,'templates/reservation.html',context)


