from django.shortcuts import render
import psycopg2
from django.http import HttpResponse




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
        cur.execute("""CREATE TABLE IF NOT EXISTS ex00_movies (
            title VARCHAR( 64 ) UNIQUE NOT NULL,
            episode_nb INT PRIMARY KEY,
            opening_crawl TEXT,
            director VARCHAR( 32 ) NOT NULL,
            producer VARCHAR( 128 ) NOT NULL,
            release_date DATE NOT NULL DEFAULT CURRENT_DATE
        );""")
    except Exception as err:
        return HttpResponse(f"<h1 style='font-family: sans-serif'>Error: Unable to connect to the database {err}</h1>")
    return HttpResponse(f"<h1 style='font-family: sans-serif'>ok</h1>")

