from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .models import Planets

# Create your views here.
class Display(View):
    def get(self, request, *args, **kwargs):
        planets = Planets.objects.filter(climate__contains="windy")
        poeple_info = []
        if len(planets) == 0:
            return HttpResponse("<h1 style='font-family: sans-serif'>No data available. use : python manage.py loaddata ex09/ex09_initial_data.json</h1>")
        for planet in planets:
            for pla in planet.people_set.all():
                poeple_info.append([pla.name, planet.name, planet.climate])
        return render(request, 'people_table.html', {"poeple_info": poeple_info})
        
    
