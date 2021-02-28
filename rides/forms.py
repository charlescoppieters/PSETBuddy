from django import forms
from .models import Person


class RideForm(forms.Form):
  search_city = forms.CharField(label='Search City', max_length=64, required=False)
  search_state = forms.CharField(label='Search State', max_length=64, required=False)


class NewRideForm(forms.ModelForm):
  class Meta:
    model = Person
    exclude = []
