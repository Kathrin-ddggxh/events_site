from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# source: https://stackoverflow.com/questions/62935406/how-to-make-a-signup-view-using-class-based-views-in-django#:~:text=from%20django%20import%20forms%0Afrom%20django.contrib.auth.models%20import%20User%0Afrom%20django.contrib.auth.forms%20import%20UserCreationForm%0A%0Aclass%20UserRegisterForm(UserCreationForm)%3A%0A%20%20email%20%3D%20forms.EmailField()%0A%0A%20%20class%20Meta%3A%0A%20%20%20%20%20%20model%20%3D%20User%0A%20%20%20%20%20%20fields%20%3D%20%5B%27username%27%2C%20%27email%27%2C%20%27first_name%27%5D  # noqa
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "first_name"]
