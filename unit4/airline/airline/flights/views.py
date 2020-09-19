from django.shortcuts import render 
from .models import Flight , Passenger
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.


#displays a list of all the flitghts
def index(request):
    return render(request, "flights/index.html",{
           "flights": Flight.objects.all()    }       )    

def flight(request, flight_id):
    flight = Flight.objects.get(pk = flight_id)
    return render(request, "flights/flight.html",
    {"flight":flight, 
    "passengers": flight.passengers.all(),
    "non_passengers": Passenger.objects.exclude(flights=flight).all()   } )

 
def book(request, flight_id):
    if request.method == "POST":
        try:
            passenger = Passenger.objects.get(pk=int(request.POST["passenger"]))
            flight = Flight.objects.get(pk=flight_id)
        except KeyError:
            return HttpResponseBadRequest("Bad Request: no flight chosen")
        except Flight.DoesNotExist:
            return HttpResponseBadRequest("Bad Request: flight does not exist")
        except Passenger.DoesNotExist:
            return HttpResponseBadRequest("Bad Request: passenger does not exist")
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse("flight", args=(flight_id,)))