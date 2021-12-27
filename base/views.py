from django.shortcuts import render

rooms = [
    {'id': 1, 'name': 'python'},
    {'id': 2, 'name': 'frontend'},
    {'id': 3, 'name': 'design'},
]

def home(request):
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = None
    for i in rooms:
        if i['id'] == pk:
            room = i
    return render(request, 'base/room.html', {'room': room})
