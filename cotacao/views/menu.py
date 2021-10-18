from django.views.generic import TemplateView


class CoinsTemplateView(TemplateView):
    template_name = 'dashboard/coins.html'