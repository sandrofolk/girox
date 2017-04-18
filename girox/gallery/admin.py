from django.contrib import admin

from girox.gallery.models import Album, Photo


class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 0
    classes = ['collapse']


class AlbumModelAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('tags',)
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

admin.site.register(Album, AlbumModelAdmin)
