from django import forms


class WelcomeForm(forms.Form):
    user_name = forms.CharField(label="Your name", max_length=40)
