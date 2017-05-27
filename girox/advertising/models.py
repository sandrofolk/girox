from django.db import models
from django.dispatch import receiver
from versatileimagefield.fields import VersatileImageField
from versatileimagefield.image_warmer import VersatileImageFieldWarmer


def advertiser_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/advertisers/<id of Advertiser>/<filename>
    return 'advertisers/{0}'.format(filename)


class Advertiser(models.Model):
    title = models.CharField('título', max_length=250)
    link = models.CharField(max_length=250)
    banner = VersatileImageField('arquivo', upload_to=advertiser_directory_path, help_text='Imagem com: 300 X 250 pixels')
    order = models.IntegerField('ordem', unique=True)
    is_public = models.BooleanField('é pública?', default=False)
    expiration_date = models.DateField('data de validade')
    observation = models.TextField('observação', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'anunciante'
        verbose_name_plural = 'anunciantes'
        ordering = ('order',)


@receiver(models.signals.post_save, sender=Advertiser)
def warm_Advertiser_banner_images(sender, instance, **kwargs):
    """Ensures Advertiser image files are created post-save"""
    advertiser_img_warmer = VersatileImageFieldWarmer(
        instance_or_queryset=instance,
        rendition_key_set='advertiser',
        image_attr='banner'
    )
    num_created, failed_to_create = advertiser_img_warmer.warm()


@receiver(models.signals.post_delete, sender=Advertiser)
def delete_Advertiser_files(sender, instance, **kwargs):
    """
    Deletes Advertiser file renditions on post_delete.
    """
    # Deletes Image Renditions
    instance.banner.delete_all_created_images()
    # Deletes Original Image
    instance.banner.delete(save=False)
