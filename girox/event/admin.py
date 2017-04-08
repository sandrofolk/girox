from django.contrib import admin
from django.shortcuts import render

from girox.event.models import Event, Subscription, EventSponsorsImage


class SubscriptionInline(admin.StackedInline):
    model = Subscription
    extra = 0


class EventSponsorsImageInline(admin.TabularInline):
    model = EventSponsorsImage
    extra = 0


def print_subscriptions(modeladmin, request, queryset):
    context = {
        'events': queryset
    }
    return render(request, 'event/print_subscriptions.html', context)
print_subscriptions.short_description = "Imprimir as inscrições dos eventos selecionados"


class EventModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'date_limit_subscription')
    search_fields = ('title', 'description')
    inlines = [
        EventSponsorsImageInline,
        SubscriptionInline,
    ]
    actions = [print_subscriptions]


class SubscriptionModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'rg', 'cpf')
    search_fields = ('name', 'rg', 'cpf')


admin.site.register(Event, EventModelAdmin)
admin.site.register(Subscription, SubscriptionModelAdmin)
