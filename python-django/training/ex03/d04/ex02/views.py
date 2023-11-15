from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import NameForm
from django.conf import settings
from datetime import datetime

def get_name(request):
    logfile = open(settings.LOG_FILE, mode='a+')
    logfile.seek(0)
    history = logfile.readlines()
    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            data = form.cleaned_data.get('your_name')
            history.append(data + ' ' + dt_string)
            logfile.write(data + ' ' + dt_string + '\n')
            form = NameForm()
    else:
        form = NameForm()
    return render(request, "name.html", {"form": form, "history": history})

