from django.contrib import admin
# from easy_thumbnails.files import get_thumbnailer
from girox.gallery.models import Album, Photo


class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 0
    classes = ['collapse']


class AlbumModelAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('tags',)
    raw_id_fields = ("cover_photo",)
    # inlines = [PhotoInline,]
    # fieldsets = (
    #     (None, {
    #         'fields': ('title', 'description',)
    #     }),
    #     ('Fotos', {
    #         'classes': ('collapse', 'close'),
    #         'fields': ('PhotoInline',)
    #     }),
    # )


class PhotoModelAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'is_public', 'album', 'admin_thumbnail')
    # list_display_links = ('file',)
    list_filter = ('album', 'tags',)

    def admin_thumbnail(self, obj):
        if obj.file:
            # return u'<img src="%s" style="height: 3em;" />' % obj.file.url
            # return u'<img src="%s" style="height: 3em;" />' % get_thumbnailer(obj.file)['mini_photo'].url
            return u'<img src="%s" />' % obj.file.thumbnail['220x220'].url
        else:
            return ''

    admin_thumbnail.short_description = 'Thumbnail'
    admin_thumbnail.allow_tags = True


admin.site.register(Album, AlbumModelAdmin)
admin.site.register(Photo, PhotoModelAdmin)
