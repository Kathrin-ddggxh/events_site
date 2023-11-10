from django.contrib.auth.forms import UserCreationForm
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
# from django.views import generic
from django.views.generic.edit import CreateView

# source: https://learndjango.com/tutorials/django-signup-tutorial#:~:text=from%20django.contrib.auth.forms%20import%20UserCreationForm%0Afrom%20django.urls%20import%20reverse_lazy%0Afrom%20django.views%20import%20generic%0A%0A%0Aclass%20SignUpView(generic.CreateView)%3A%0A%20%20%20%20form_class%20%3D%20UserCreationForm%0A%20%20%20%20success_url%20%3D%20reverse_lazy(%22login%22)%0A%20%20%20%20template_name%20%3D%20%22registration/signup.html%22  # noqa
class SignUpView(SuccessMessageMixin, CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("home")
    template_name = "users/signup.html"
    success_message = "Registration was successful"