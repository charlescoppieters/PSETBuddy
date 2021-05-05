from django import forms
from .models import Person
from .models import Feedback



class BuddyForm(forms.Form):
  search_course = forms.CharField(label='Search Courses', max_length=64, required=False)
  

class NewBuddyForm(forms.ModelForm):
  class Meta:
    model = Person
    exclude = [Person.has_group1, Person.date]

class NewFeedbackForm(forms.ModelForm):
    class Meta:
      model = Feedback
      exclude = []
