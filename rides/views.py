from .forms import RideForm, NewRideForm
from django.shortcuts import render, redirect

from .models import Person

# relative import of forms
from .forms import RideForm

# Create your views here.


def index(request):

  context = {}

  if "search_city" in request.GET:
    search_city = request.GET["search_city"]
    search_state = request.GET["search_state"].upper()

    context["people"] = Person.objects.filter(
        origination__icontains=search_city) | Person.objects.filter(destination_city__icontains=search_city) & Person.objects.filter(destination_state__icontains=search_state)
 

  context["form"] = RideForm()
  context["new_ride_form"] = NewRideForm()
  return render(request, "index_view.html", context)

def create(request):
  if request.method == "POST":
    new_ride = NewRideForm(request.POST)
    new_ride.save()

  return redirect("/rides")

def addride(request):
  context = {}
  context["new_ride_form"] = NewRideForm()
  return render(request, "create.html", context)



