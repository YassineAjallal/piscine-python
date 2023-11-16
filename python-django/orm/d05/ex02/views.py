from django.shortcuts import render
import psycopg2
from django.http import HttpResponse

DATA = [
        {"episode_nb": 1, "title": "The Phantom Menace", "director": "George Lucas", "producer": "Rick McCallum ", "release_date": "1999-05-19"},
        {"episode_nb": 2, "title": "Attack of the Clones", "director": "George Lucas", "producer": "Rick McCallum ", "release_date": "2002-05-16"},
        {"episode_nb": 3, "title": "Revenge of the Sith", "director": "George Lucas", "producer": "Rick McCallum ", "release_date": "2005-05-19"},
        {"episode_nb": 4, "title": "A New Hope", "director": "George Lucas", "producer": "Gary Kurtz, Rick McCallum", "release_date": "1977-05-25"},
        {"episode_nb": 5, "title": "The Empire Strikes Back", "director": "George Lucas", "producer": "Gary Kurtz, Rick McCallum", "release_date": "1980-05-17"},
        {"episode_nb": 6, "title": "Return of the Jedi", "director": "George Lucas", "producer": "Howard G. Kazanjian, George Lucas, Rick McCallum", "release_date": "1983-05-25"},
        {"episode_nb": 7, "title": "The Force Awakens", "director": "J. J. Abrams", "producer": "Kathleen Kennedy, J. J. Abrams, Bryan Burk", "release_date": "2015-12-11"}
    ]
# Create your views here.
def building_a_table(request):
    try:
        connections_details = psycopg2.connect(
            host="localhost",
            database="yajallal",
            user="yajallal",
            password="yajallal",
            port="5432"
        )
        cur = connections_details.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS ex02_movies (
            title VARCHAR( 64 ) UNIQUE NOT NULL,
            episode_nb INT PRIMARY KEY,
            opening_crawl TEXT,
            director VARCHAR( 32 ) NOT NULL,
            producer VARCHAR( 128 ) NOT NULL,
            release_date DATE NOT NULL DEFAULT CURRENT_DATE
        );""")
        connections_details.commit()
    except Exception as err:
        connections_details.close()
        return HttpResponse(f"<h1 style='font-family: sans-serif'>Error: Unable to connect to the database: {err}</h1>")
    connections_details.close()
    return HttpResponse(f"<h1 style='font-family: sans-serif'>OK</h1>")

def insert_in_tabel(request):
    try:
        connections_details = psycopg2.connect(
            host="localhost",
            database="yajallal",
            user="yajallal",
            password="yajallal",
            port="5432"
        )
        cur = connections_details.cursor()
        for data in DATA:
            cur.execute(f"""INSERT INTO ex02_movies(episode_nb, title, director, producer, release_date) 
                        VALUES('{data['episode_nb']}', '{data['title']}', '{data['director']}', '{data['producer']}', '{data['release_date']}');""")
        connections_details.commit()
    except Exception as err:
        connections_details.close()
        return HttpResponse(f"<h1 style='font-family: sans-serif'>Error: cannot insert to the database: {err}</h1>")
    connections_details.close()
    return HttpResponse(f"<h1 style='font-family: sans-serif'>OK</h1>")

def display(request):
    try:
        connections_details = psycopg2.connect(
                host="localhost",
                database="yajallal",
                user="yajallal",
                password="yajallal",
                port="5432"
            )
        cur = connections_details.cursor()
        cur.execute("TABLE ex02_movies;")
        ls = cur.fetchall()
        
    except:
        return HttpResponse("<h1 style='font-family: sans-serif'>No data available</h1>")
    if len(ls) == 0:
        return HttpResponse("<h1 style='font-family: sans-serif'>No data available</h1>")
    return render(request, 'table.html', {"items": ls})
