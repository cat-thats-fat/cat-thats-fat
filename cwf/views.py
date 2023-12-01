from .static.cwf.cheapweedfinder import get_data
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def cwf(request):
    return render(request, 'cwf/cwf.html')

@login_required
def backBTN(request):
    return redirect('home')

@login_required
def cwfdata(request):
    data = get_data()
    
    maryjs = data["MaryJ's"]
    inspired = data["Inspired"]
    seventen = data["710"]
    giggles = data["Giggles"]

    context = {
        'maryjs': maryjs,
        'inspired': inspired,
        'seventen': seventen,
        'giggles': giggles,
    }

    return render(request, 'cwf/cwf.html', context)