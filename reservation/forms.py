from django import forms
from . models import reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model=reservation
        fields="__all__"

