from django.views.generic import ListView, DetailView

from girox.event.models import Event, Subscription
from girox.event.forms import SubscriptionForm
from girox.event.mixins import EmailCreateView

list = ListView.as_view(model=Event)

subscription_new = EmailCreateView.as_view(model=Subscription,
                                           form_class=SubscriptionForm,
                                           email_subject='Confirmação de inscrição')

subscription_detail = DetailView.as_view(model=Subscription)
