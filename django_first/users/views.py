from django.shortcuts import render,redirect
from .forms import UserRegistration
from django.http import HttpResponse




def register(request):
    if request.method == 'POST':
        form = UserRegistration(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')

            return HttpResponse(f'Account for {username} has been created')
    else:
        form = UserRegistration()

    return render(request,'users/register.html', {'form': form})


