from django.shortcuts import render
from .models import Disaster

def disaster_list(request):
    disasters = Disaster.objects.all()
    return render(request, 'disasters/disaster_list.html', {'disasters': disasters})

def disaster_detail(request, pk):
    disaster = Disaster.objects.get(pk=pk)
    return render(request, 'disasters/disaster_detail.html', {'disaster': disaster})
