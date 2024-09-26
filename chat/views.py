from django.shortcuts import render, redirect
from .models import Room, Message

# Create your views here.
def index(request):
    return render(request, 'index.html')

def room(request, room):
    return render(request, 'room.html')

def checkview(request):
    
    if request.method == 'POST':

        room = request.POST.get('room_name')
        username = request.POST.get('username')

        if Room.objects.filter(name=room).exists():

            return redirect('/'+room+'?username='+username)
        
        else:

            new_room = Room.objects.create(name=room)
            new_room.save()

            return redirect('/'+room+'?username='+username)

