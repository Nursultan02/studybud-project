from django.shortcuts import render
from .models import Room


def home(request):
    context = {'rooms': Room.objects.all()}
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    return render(request, 'base/room.html', {'room': room})
