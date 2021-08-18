from django.shortcuts import render, redirect
from .models import Post
from django.http import JsonResponse, HttpResponse
from .forms import PostForm, ChatRoomForm
from django.contrib.auth.decorators import login_required
from .models import Chatroom


# Create your views here.
@login_required
def post(request):
    if request.method == 'POST':
        form = ChatRoomForm(request.POST)

        if form.is_valid():
            room_name = form.cleaned_data['name']

            if not Chatroom.objects.filter(room_name=room_name):
                new_room = Chatroom(room_name=room_name, creator=request.user.username)
                new_room.save()
                request.user.chatroom.add(new_room)
               
            post_form = PostForm()
            return render(request, 'chatroom.html', {'form': post_form, 'cur_size': Post.objects.count(), 'room_name': room_name, 'cur_user':request.user.username})
                 
    form = ChatRoomForm()
    return render(request, 'post.html', {'form': form})

@login_required
def chatroom(request):
   
    pass

    #return render(request, 'chatroom.html', {'form': form, 'cur_size': Post.objects.count()})

def createMes(request):
    if request.method == "POST":
        roomname = request.POST.get('roomname')
        room = Chatroom.objects.get(room_name=roomname)
        new_post = Post(text=request.POST.get('text'), authorname=request.user.username, roomname=roomname, room=room)
        new_post.save()
        request.user.post_auth.add(new_post)   
        #return HttpResponse('Message created!')
    

def getMessage(request):
    message = Post.objects.all()
    #print(message[3].author.id)
    return JsonResponse({"message":list(message.values())})