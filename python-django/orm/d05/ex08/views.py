from django.shortcuts import render
from django.http import HttpResponse
import psycopg2

# Create your views here.
def init(request):
    try:   
        connection = psycopg2.connect(
            host="localhost",
            database="yajallal",
            user="yajallal",
            password="yajallal",
            port="5432"
        )
        cur = connection.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS ex08_planets (
                id SERIAL PRIMARY KEY,
                name VARCHAR( 64 ) UNIQUE NOT NULL,
                climate VARCHAR,
                diameter INTEGER,
                orbital_period INTEGER,
                population BIGINT,
                rotation_period INTEGER,
                surface_water REAL,
                terrain VARCHAR( 128 )
                );""")
        cur.execute("""CREATE TABLE IF NOT EXISTS ex08_people (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR( 64 ) UNIQUE NOT NULL,
                    birth_year VARCHAR( 32 ),
                    gender VARCHAR( 32 ),
                    eye_color VARCHAR( 32 ),
                    hair_color VARCHAR( 32 ),
                    height INTEGER,
                    mass REAL,
                    homeworld VARCHAR( 68 ),
                    CONSTRAINT fk_ex08_planets
                        FOREIGN KEY(homeworld) 
                            REFERENCES ex08_planets(name)
        )""")
        connection.commit()
        connection.close()
    except Exception as err:
        connection.close()
        return HttpResponse(f'<h1 style="font-family: sans-serif">Error: {err}</h1>')
    return HttpResponse(f'<h1 style="font-family: sans-serif">OK</h1>')

def populate(request):
    try:
        connection = psycopg2.connect(
            host="localhost",
            database="yajallal",
            user="yajallal",
            password="yajallal",
            port="5432"
        )
        cur = connection.cursor()
        planets_csv = open('/Users/yajallal/Desktop/piscine-python/python-django/orm/d05/ex08/static/csv/planets.csv')
        cur.copy_from(planets_csv, 'ex08_planets', null='NULL', columns=('name', 'climate', 'diameter', 'orbital_period', 'population', 'rotation_period', 'surface_water', 'terrain'))
        planets_csv.close()
        people_csv = open('/Users/yajallal/Desktop/piscine-python/python-django/orm/d05/ex08/static/csv/people.csv')
        cur.copy_from(people_csv, 'ex08_people', null='NULL', columns=('name', 'birth_year', 'gender', 'eye_color', 'hair_color', 'height', 'mass', 'homeworld'))
        people_csv.close()
        connection.commit()
        connection.close()
    except Exception as err:
        connection.close()
        return HttpResponse(f'<h1 style="font-family: sans-serif">Error: {err}</h1>')
    return HttpResponse(f'<h1 style="font-family: sans-serif">OK</h1>')

def display(request):
    try:
        connection = psycopg2.connect(
            host="localhost",
            database="yajallal",
            user="yajallal",
            password="yajallal",
            port="5432"
        )
        cur = connection.cursor()
        cur.execute("""SELECT ex08_people.name, ex08_people.homeworld, ex08_planets.climate
			FROM ex08_planets
			JOIN ex08_people ON ex08_planets.name = ex08_people.homeworld
			WHERE position('windy' in ex08_planets.climate)>0;""")
        result = cur.fetchall()
        connection.close()
        if (len(result) == 0):
            return HttpResponse(f'<h1 style="font-family: sans-serif">No data available</h1>')
    except Exception as err:
        connection.close()
        return HttpResponse(f'<h1 style="font-family: sans-serif">No data available</h1>')
    return render(request, 'people.html', {"results": result})