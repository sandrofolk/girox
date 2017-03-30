from django.contrib import admin

from girox.event.models import Event, Subscription


class SubscriptionInline(admin.TabularInline):
    model = Subscription
    extra = 0


class EventModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title', 'description')
    inlines = [
        SubscriptionInline,
    ]


admin.site.register(Event, EventModelAdmin)
admin.site.register(Subscription)
