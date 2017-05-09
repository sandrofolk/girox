from django.contrib.admin import site, StackedInline, TabularInline, RelatedOnlyFieldListFilter
from django.shortcuts import render

from girox.core.admin import CustomModelAdmin
from girox.event.models import Event, Subscription, EventSponsorsImage, SubscriptionProxy


class SubscriptionInline(StackedInline):
    model = Subscription
    extra = 0


class EventSponsorsImageInline(TabularInline):
    model = EventSponsorsImage
    extra = 0


def print_subscriptions(modeladmin, request, queryset):
    context = {
        'events': queryset
    }
    return render(request, 'event/print_subscriptions.html', context)
print_subscriptions.short_description = "Imprimir as inscrições dos eventos selecionados"


class EventModelAdmin(CustomModelAdmin):
    list_display = ('title', 'date', 'date_limit_subscription')
    search_fields = ('title', 'description')
    filter_horizontal = ('organizers',)
    inlines = [
        EventSponsorsImageInline,
        # SubscriptionInline,
    ]
    actions = [print_subscriptions]


class SubscriptionModelAdmin(CustomModelAdmin):
    list_display = ('id', 'name', 'rg', 'cpf')
    search_fields = ('name', 'rg', 'cpf')


class SubscriptionProxyAdmin(CustomModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name', 'rg', 'cpf', 'email', 'phone', 'address', 'city', 'team')
    change_form_template = "admin/view.html"
    view_on_site = False
    list_filter = (
        ('event', RelatedOnlyFieldListFilter),
    )

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
