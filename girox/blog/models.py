from django.db import models
# from django.shortcuts import resolve_url as r
from taggit.managers import TaggableManager


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

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return r('blog:post_detail', {'slug': self.slug})

    class Meta:
        verbose_name = 'postagem'
        verbose_name_plural = 'postagens'


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
