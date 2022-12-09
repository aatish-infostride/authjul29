from pyexpat.errors import messages
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from authapp.models import User
from .forms import register_form, login_form

# Create your views here.

def register(request):
    if request.method == 'POST':

        form = register_form(request.POST)

        if form.is_valid():

            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']

            data = User(username = username, email=email, password1=password1, password2=password2)
            data.save()

    else:
        form = register_form()

    return render(request, 'register.html', {'form':form})



def login(request):
    if request.method == 'POST':

        form = login_form(request.POST)

        if form.is_valid():

            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            checkbox = request.POST.get['remember_me']
        
            check_user = User.objects.filter(username=username, password1=password1)

            if checkbox and check_user :
                request.session['user'] = username
                request.session.set_expiry(864000)
                return redirect('home')

            if check_user:
                request.session['user'] = username
                return redirect('home')    

        else:
            messages.error(request, 'check your username or password')


    else:
        form = login_form()

    form = login_form()

    return render(request, 'login.html', {'form':form})




