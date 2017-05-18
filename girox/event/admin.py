import csv

from django.contrib.admin import site, StackedInline, TabularInline, RelatedOnlyFieldListFilter
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django import forms
from django.contrib.admin import ACTION_CHECKBOX_NAME
from django.template.loader import get_template
from django.template import Context

from girox.core.admin import CustomModelAdmin
from girox.event.models import Event, Subscription, EventSponsorsImage, SubscriptionProxy


class SubscriptionInline(StackedInline):
    model = Subscription
    extra = 0


class EventSponsorsImageInline(TabularInline):
    model = EventSponsorsImage
    extra = 0


def export_subscriptions_emails(modeladmin, request, queryset):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="emails_dos_inscritos.csv"'

    writer = csv.writer(response)
    for event in queryset:
        writer.writerow([event.title, ])
        for subscription in event.subscription_set.all():
            writer.writerow([subscription.email])

    return response
export_subscriptions_emails.short_description = "Exportar e-mails dos inscritos dos eventos selecionados"


def print_subscriptions(modeladmin, request, queryset):
    context = {
        'events': queryset
    }
    return render(request, 'event/print_subscriptions.html', context)
print_subscriptions.short_description = "Imprimir as inscrições dos eventos selecionados"


from django.core.mail import EmailMultiAlternatives


class SendMailForm(forms.Form):
    _selected_action = forms.CharField(widget=forms.MultipleHiddenInput)
    subject = forms.CharField()
    message_text = forms.CharField(widget=forms.Textarea)
    message_html = forms.CharField(widget=forms.Textarea)


def send_mail(modeladmin, request, queryset):
    form = None

    if 'send' in request.POST:
        form = SendMailForm(request.POST)

        if form.is_valid():
            from_email = 'contato@girox.com.br'
            to = []

            subject = form.cleaned_data['subject']
            message_text = form.cleaned_data['message_text']
            message_html = form.cleaned_data['message_html']

            text_template = get_template('frontend/base_email.txt')
            html_template = get_template('frontend/base_email.html')
            d = Context({'subject': subject, 'message_text': message_text, 'message_html': message_html})
            text_content = text_template.render(d)
            html_content = html_template.render(d)

            for event in queryset:
                for subscription in event.subscription_set.all():
                    to += [subscription.email]

            msg = EmailMultiAlternatives(subject=subject, body=text_content, from_email=from_email, to=[from_email], bcc=to)
            msg.attach_alternative(html_content, "text/html")
            msg.send()

            modeladmin.message_user(request, "E-mails enviados com sucesso!")
            return HttpResponseRedirect(request.get_full_path())

    if not form:
        form = SendMailForm(initial={'_selected_action': request.POST.getlist(ACTION_CHECKBOX_NAME)})

    return render(request, 'event/send_mail.html', {'events': queryset,
                                                    'send_mail_form': form,
                                                    })
send_mail.short_description = "Enviar e-mail para os inscritos dos eventos selecionados"


class EventModelAdmin(CustomModelAdmin):
    list_display = ('title', 'date', 'date_limit_subscription')
    search_fields = ('title', 'description')
    filter_horizontal = ('organizers',)
    inlines = [
        EventSponsorsImageInline,
        # SubscriptionInline,
    ]
    actions = [print_subscriptions, export_subscriptions_emails]


class SubscriptionModelAdmin(CustomModelAdmin):
    list_display = ('id', 'name', 'rg', 'cpf')
    search_fields = ('name', 'rg', 'cpf')


def print_subscriptions_list(modeladmin, request, queryset):
    context = {
        'subscriptions': queryset
    }
    return render(request, 'event/print_subscriptions_list.html', context)
print_subscriptions_list.short_description = "Imprimir os participantes selecionados"


class SubscriptionProxyAdmin(CustomModelAdmin):
    list_display = ('id', 'name', 'rg', 'cpf')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name', 'rg', 'cpf', 'email', 'phone', 'address', 'city', 'team')
    change_form_template = "admin/view.html"
    view_on_site = False
    list_filter = (
        ('event', RelatedOnlyFieldListFilter),
    )
    actions = [print_subscriptions_list,]

    def get_queryset(self, request):
        qs = super(SubscriptionProxyAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(event__organizers=request.user)

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def get_actions(self, request):
        actions = super(SubscriptionProxyAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = []
        for field in self.model._meta.fields:
            readonly_fields.append(field.name)

        return readonly_fields

    def save_model(self, request, obj, form, change):
        pass

    def delete_model(self, request, obj):
        pass

    def save_related(self, request, form, formsets, change):
        pass


site.register(Event, EventModelAdmin)
site.register(Subscription, SubscriptionModelAdmin)
site.register(SubscriptionProxy, SubscriptionProxyAdmin)
