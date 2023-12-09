from django.shortcuts import render
from django.views import View
from .models import People, Movies
from django.http import HttpResponse
from .forms import MoviesFilter

class Display(View):
    genders = list(People.objects.values_list('gender', flat=True).distinct())
    def get(self, request, *args, **kwargs):
        movies = MoviesFilter(self.genders)
        return render(request, 'movies_form.html', {"movies": movies})
    def post(self, request, *args, **kwargs):
        movies = MoviesFilter(self.genders, request.POST)
        if movies.is_valid():
            infos = []
            min_date = movies.cleaned_data.get('min_date')
            max_date = movies.cleaned_data.get('max_date')
            diameter = movies.cleaned_data.get('diameter_gt')
            gender = movies.cleaned_data.get('gender')
            films = Movies.objects.filter(release_date__gt=min_date, release_date__lt=max_date)
            caracters = [[film.title, film.characters.all().filter(gender=gender, homeworld__diameter__gt=diameter)] for film in films]
            if (len(caracters) == 0):
                return HttpResponse("<h1 style='font-family: sans-serif'>Nothing corresponding to your research</h1>")
            for caracter in caracters:
                for caract in caracter[1]:
                    infos.append([caracter[0], 
                                 caract.name,
                                 caract.gender,
                                 caract.homeworld.diameter])
            movies = MoviesFilter(self.genders)
            return  render(request, 'movies_info.html', {"infos": infos})
        return render(request, 'movies_form.html', {"movies": movies})