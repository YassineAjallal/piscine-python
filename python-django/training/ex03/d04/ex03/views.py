from django.shortcuts import render

def table_color(request):
    context_info = { "nb_lines": range(50),
                    "colors": ['black', 'red', 'blue', 'green']}
    return (render(request, 'tables.html', context=context_info))
