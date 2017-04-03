from django.views.generic import TemplateView

from girox.event.models import Event


class HomePageView(TemplateView):

    template_name = "frontend/index.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['event_list'] = Event.objects.all()[:5]
        return context

contact = TemplateView.as_view(
    template_name='frontend/contact.html'
)

# home = TemplateView.as_view(
#     template_name='frontend/index.html'
# )

# coming_soon = TemplateView.as_view(
#     template_name='frontend/coming_soon.html'
# )
