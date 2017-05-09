from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.contrib.admin.models import LogEntry


admin.site.site_header = _('GiroX / Esportes')
admin.site.site_title = _('GiroX')
admin.site.index_title = 'Início'


class CustomModelAdmin(admin.ModelAdmin):
    save_on_top = True


class LogEntryModelAdmin(CustomModelAdmin):
    list_filter = ('user',)
    date_hierarchy = 'action_time'


admin.site.register(LogEntry, LogEntryModelAdmin)
