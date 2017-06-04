from django.db import models
from django.dispatch import receiver
# from django.shortcuts import resolve_url as r
from taggit.managers import TaggableManager
from versatileimagefield.fields import VersatileImageField
from versatileimagefield.image_warmer import VersatileImageFieldWarmer


def post_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/post_photos/<filename>
    return 'post_photos/{0}'.format(filename)


class Post(models.Model):
    title = models.CharField('título', max_length=100, unique=True)
    slug = models.SlugField('url', max_length=100, unique=True)
    body = models.TextField('corpo')
    posted = models.DateField('data', db_index=True, auto_now_add=True)
    category = models.ForeignKey('blog.Category', verbose_name='categoria')
    tags = TaggableManager(blank=True)
    is_published = models.BooleanField('publicado?', default=False,
                                       help_text='Marque está opção apenas quando o post estiver pronto para ser '
                                                 'visualizado pelo público!')
    meta_description = models.TextField('meta descrição')
    cover_photo = VersatileImageField('foto de capa', upload_to=post_directory_path, blank=True, null=True)

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return r('blog:post_detail', {'slug': self.slug})

    class Meta:
        verbose_name = 'postagem'
        verbose_name_plural = 'postagens'


@receiver(models.signals.post_save, sender=Post)
def warm_post_cover_photo_images(sender, instance, **kwargs):
    """Ensures Post cover photo files are created post-save"""
    post_img_warmer = VersatileImageFieldWarmer(
        instance_or_queryset=instance,
        rendition_key_set='blog',
        image_attr='cover_photo'
    )
    num_created, failed_to_create = post_img_warmer.warm()


@receiver(models.signals.post_delete, sender=Post)
def delete_post_cover_photo_files(sender, instance, **kwargs):
    """
    Deletes Post cover photo file renditions on post_delete.
    """
    # Deletes Image Renditions
    instance.cover_photo.delete_all_created_images()
    # Deletes Original Image
    instance.cover_photo.delete(save=False)


class Category(models.Model):
    title = models.CharField('título', max_length=100, db_index=True)
    slug = models.SlugField('url', max_length=100, db_index=True)

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return r('blog:category_detail', None, {'slug': self.slug})

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'
