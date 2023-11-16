from django.shortcuts import render
from django.http import HttpResponse
from ex03.models import Movies

DATA = [
        {"episode_nb": 1, "title": "The Phantom Menace", "director": "George Lucas", "producer": "Rick McCallum ", "release_date": "1999-05-19"},
        {"episode_nb": 2, "title": "Attack of the Clones", "director": "George Lucas", "producer": "Rick McCallum ", "release_date": "2002-05-16"},
        {"episode_nb": 3, "title": "Revenge of the Sith", "director": "George Lucas", "producer": "Rick McCallum ", "release_date": "2005-05-19"},
        {"episode_nb": 4, "title": "A New Hope", "director": "George Lucas", "producer": "Gary Kurtz, Rick McCallum", "release_date": "1977-05-25"},
        {"episode_nb": 5, "title": "The Empire Strikes Back", "director": "George Lucas", "producer": "Gary Kurtz, Rick McCallum", "release_date": "1980-05-17"},
        {"episode_nb": 6, "title": "Return of the Jedi", "director": "George Lucas", "producer": "Howard G. Kazanjian, George Lucas, Rick McCallum", "release_date": "1983-05-25"},
        {"episode_nb": 7, "title": "The Force Awakens", "director": "J. J. Abrams", "producer": "Kathleen Kennedy, J. J. Abrams, Bryan Burk", "release_date": "2015-12-11"}
    ]

def insert_in_table(request):
    try:
        for data in DATA:
            Movies.objects.create(
                episode_nb=data['episode_nb'],
                title=data['title'],
                director=data['director'],
                producer=data['producer'],
                release_date=data['release_date']
            )
    except Exception as err:
        return HttpResponse(f"<h1 style='font-family: sans-serif'>Error: cannot insert to the database: {err}</h1>")
    return HttpResponse("<h1 style='font-family: sans-serif'>OK</h1>")

def display(request):
        all_objects = Movies.objects.all()
        if (len(all_objects) == 0):
             return HttpResponse("<h1 style='font-family: sans-serif'>No data available</h1>")
        return render(request, 'table1.html', {"items": all_objects})
