from django.shortcuts import render
from .models import Post
from django.http import JsonResponse
from .forms import PostForm
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def post(request):
    form = PostForm()
    return render(request, 'post.html', {'form': form, 'cur_size': Post.objects.count()})

def createMes(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = Post(text=form.cleaned_data['text'], authorname=request.user.username)
            new_post.save()
            request.user.post.add(new_post)
            #return HttpResponse('Message created!')
    
    
def getMessage(request):
    message = Post.objects.all()
    #print(message[3].author.id)
    return JsonResponse({"message":list(message.values())})