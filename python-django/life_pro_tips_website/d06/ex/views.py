from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.conf import settings
import random

class Display(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'website.html')
    
class DataApi(View):
    def get(self, request, *args, **kwargs):
        names = getattr(settings, 'DEFAULT_NAMES')
        rand_value = random.randint(0, 9)
        return JsonResponse({'name': names[rand_value]})

