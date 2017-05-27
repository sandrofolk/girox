from django.contrib.admin import site
from girox.core.admin import CustomModelAdmin
from girox.advertising.models import Advertiser


class AdvertiserModelAdmin(CustomModelAdmin):
    list_display = ('title_tags', 'link_tags', 'admin_thumbnail')

    def admin_thumbnail(self, obj):
        return u'<img src="%s" />' % obj.banner.crop['300x250'].url

    admin_thumbnail.short_description = 'Thumbnail'
    admin_thumbnail.allow_tags = True

    def link_tags(self, obj):
        return u'<a href="{0}">{0}</a>'.format(obj.link)

    link_tags.short_description = 'Link'
    link_tags.allow_tags = True

    def title_tags(self, obj):
        return obj.title

    title_tags.short_description = 'Título'
    title_tags.allow_tags = True


site.register(Advertiser, AdvertiserModelAdmin)