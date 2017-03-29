from django.views.generic.base import TemplateView

from girox.event.models import Event


class HomePageView(TemplateView):

    template_name = "frontend/index.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['event_list'] = Event.objects.all()[:5]
        return context


# from django.views.generic import TemplateView
#
#
# home = TemplateView.as_view(
#     template_name='frontend/index.html'
# )
