from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.contrib import messages

from girox.event.models import Event, Subscription
from girox.event.forms import SubscriptionForm
from girox.event.mixins import EmailCreateView

list_event = ListView.as_view(model=Event)

subscription_new = EmailCreateView.as_view(model=Subscription,
                                           form_class=SubscriptionForm,
                                           email_subject='Confirmação de inscrição')

subscription_detail = DetailView.as_view(model=Subscription)


def subscription_regulation(request, event):
    if request.method == 'POST':
        cpf = request.POST.get('cpf')
        if Subscription.objects.filter(event=event, cpf=cpf).exists():
            return HttpResponseRedirect(static('pdf/Termo_de_Responsabilidade.pdf'))
        else:
            messages.error(request, 'CPF não inscrito no evento!')
    return render(request, template_name='event/subscription_regulation.html')
