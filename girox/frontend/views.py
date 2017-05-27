from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.contrib import messages
import datetime

from girox.advertising.models import Advertiser
from girox.event.models import Event
from girox.frontend.forms import ContactForm
from girox.gallery.models import Album


class HomePageView(TemplateView):

    template_name = "frontend/index.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['event_list'] = Event.objects.filter(date__gte=datetime.datetime.now()).all()[:5]
        context['album_list'] = Album.objects.all()[:5]
        context['advertiser_list'] = Advertiser.objects.all()
        return context


class ContactView(FormView):
    template_name = 'frontend/contact.html'
    form_class = ContactForm
    success_url = '/contato/sucesso/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super(ContactView, self).form_valid(form)

contact_success = TemplateView.as_view(
    template_name='frontend/contact_success.html'
)

plans = TemplateView.as_view(
    template_name='frontend/plans.html'
)

# home = TemplateView.as_view(
#     template_name='frontend/index.html'
# )

# coming_soon = TemplateView.as_view(
#     template_name='frontend/coming_soon.html'
# )
