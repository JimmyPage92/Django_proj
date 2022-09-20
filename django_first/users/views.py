from django.shortcuts import render,redirect
from .forms import UserRegistration
from django.contrib.auth.decorators import login_required




def register(request):
    if request.method == 'POST':
        form = UserRegistration(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistration()

    return render(request,'users/register.html', {'form': form, 'title': 'Registration page'})

@login_required
def profile(request):
    return render(request, 'users/profile.html')