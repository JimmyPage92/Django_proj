from django.shortcuts import render

from .forms import WelcomeForm


def welcome_user(request):
    if request.method == "POST":
        welcome_form = WelcomeForm(request.POST)
        print(request.POST)
        if welcome_form.is_valid():
            user_name: str = welcome_form.cleaned_data["user_name"]
    else:
        user_name: str = "default"
        welcome_form = WelcomeForm()

    return render(request, "hello_app/welcome-user.html", context={
        "welcome_form": welcome_form,
        "user_name": user_name
    })
