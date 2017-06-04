from django.views.generic import ListView, DetailView
from django.views.generic.base import ContextMixin

from girox.advertising.models import Advertiser


class AdvertiserViewMixin(ContextMixin):

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(AdvertiserViewMixin, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the advertisers
        context['advertiser_list'] = Advertiser.objects.all()
        return context


class ListViewAdvertiser(ListView, AdvertiserViewMixin):
    pass


class DetailViewAdvertiser(DetailView, AdvertiserViewMixin):
    pass
