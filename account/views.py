from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            form.save()

            return redirect('/login', {"cur_email": email})
    else:
        form = RegisterForm()
    return render(request, "register/register.html", {"form": form})

@login_required
def account_center(request):
    
    cur_user = request.user

    return render(request, 'account_center.html', {'user':cur_user})


