from django.contrib.admin import site
from django import forms
from django_summernote.widgets import SummernoteWidget

from girox.blog.models import Post, Category
from girox.core.admin import CustomModelAdmin


class PostModelAdminForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'body': SummernoteWidget(),
        }


class PostModelAdmin(CustomModelAdmin):
    form = PostModelAdminForm
    exclude = ['posted']
    prepopulated_fields = {'slug': ('title',)}


class CategoryModelAdmin(CustomModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


site.register(Post, PostModelAdmin)
site.register(Category, CategoryModelAdmin)
