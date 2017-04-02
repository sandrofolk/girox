from django.contrib import admin
from django.shortcuts import render

from girox.event.models import Event, Subscription


class SubscriptionInline(admin.StackedInline):
    model = Subscription
    extra = 0


def print_subscriptions(modeladmin, request, queryset):
    context = {
        'events': queryset
    }
    return render(request, 'event/print_subscriptions.html', context)
print_subscriptions.short_description = "Imprimir as inscrições dos eventos selecionados"


class EventModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'date', 'date_limit_subscription')
    search_fields = ('title', 'description')
    inlines = [
        SubscriptionInline,
    ]
    actions = [print_subscriptions]


admin.site.register(Event, EventModelAdmin)
# admin.site.register(Subscription)
