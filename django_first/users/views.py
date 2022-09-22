from django.shortcuts import render,redirect
from .forms import UserRegistration, UserUpdateForm, ProfileUpdateForm
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
    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)


    return render(request, 'users/profile.html', {'user_form': user_form, 'profile_form': profile_form})

