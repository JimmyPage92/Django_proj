from django.urls import path

from . import views

urlpatterns = [
    path("welcome/", views.welcome_user)    # 127.0.0.1/hello_app/welcome/
]