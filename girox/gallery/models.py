from django.db import models
from django.shortcuts import resolve_url as r
from django_extensions.db.models import TimeStampedModel
from taggit.managers import TaggableManager


class Album(TimeStampedModel):
    title = models.CharField('título', max_length=250)
    description = models.TextField('descrição', blank=True, null=True)
    cover_photo = models.ForeignKey('Photo', related_name='+', blank=True,
                                    null=True, verbose_name='foto de capa')
    is_public = models.BooleanField('é público?', default=True)
    date_added = models.DateField('adicionado em', null=True, blank=True)
    tags = TaggableManager(blank=True, help_text=None)
    order = models.PositiveIntegerField('ordem', default=9999)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return r('galleries:album_detail', self.pk)


def album_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/album_photos/<id of album>/<filename>
    return 'album_photos/{0}/{1}'.format(instance.album.id, filename)


class Photo(TimeStampedModel):
    album = models.ForeignKey(Album)
    file = models.ImageField('arquivo', upload_to=album_directory_path)
    description = models.TextField('descrição', blank=True, null=True)
    is_public = models.BooleanField('é pública?', default=True)
    tags = TaggableManager(blank=True, help_text=None)

    def __str__(self):
        return self.file.name

    def get_absolute_url(self):
        return self.file.url

    class Meta:
        verbose_name = 'foto'
        verbose_name_plural = 'fotos'
        ordering = ('album', 'file')
