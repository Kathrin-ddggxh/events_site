from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.views import View

from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.urls import reverse_lazy

from .forms import UserRegisterForm


# source: https://learndjango.com/tutorials/django-signup-tutorial#:~:text=from%20django.contrib.auth.forms%20import%20UserCreationForm%0Afrom%20django.urls%20import%20reverse_lazy%0Afrom%20django.views%20import%20generic%0A%0A%0Aclass%20SignUpView(generic.CreateView)%3A%0A%20%20%20%20form_class%20%3D%20UserCreationForm%0A%20%20%20%20success_url%20%3D%20reverse_lazy(%22login%22)%0A%20%20%20%20template_name%20%3D%20%22registration/signup.html%22  # noqa
class SignUpView(SuccessMessageMixin, CreateView):
    """
    User registration view
    """

    form_class = UserRegisterForm
    success_url = reverse_lazy("home")
    template_name = "users/signup.html"
    success_message = "Registration was successful"


# source: https://www.pythontutorial.net/django-tutorial/django-loginview/#:~:text=class%20MyLoginView(LoginView,get_context_data(form%3Dform))  # noqa
class UserLoginView(LoginView):
    """
    User Login View
    """

    template_name = "users/login.html"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("home")

    def form_invalid(self, form):
        messages.error(self.request, "Invalid username or password")
        return self.render_to_response(self.get_context_data(form=form))


class UserLogoutView(View):
    """
    User logout view
    """
    template_name = "users/logout.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        logout(request)
        return redirect('home')
