# source: https://learndjango.com/tutorials/django-signup-tutorial#:~:text=from%20django.urls%20import%20path%0A%0Afrom%20.views%20import%20SignUpView%0A%0A%0Aurlpatterns%20%3D%20%5B%0A%20%20%20%20path(%22signup/%22%2C%20SignUpView.as_view()%2C%20name%3D%22signup%22)%2C%0A%5D  # noqa
from django.urls import path

from .views import SignUpView


urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
]