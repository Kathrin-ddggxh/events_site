from django.views.generic import TemplateView


class Index(TemplateView):
    """ renders home page """
    template_name = 'home/index.html'