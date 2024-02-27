from django.views.generic import TemplateView


class Home(TemplateView):
    """View for basic home page"""

    template_name = 'base.html'