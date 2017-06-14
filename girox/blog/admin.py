from django.conf import settings
from django.contrib.admin import site
from django import forms
from django_summernote.widgets import SummernoteWidget

from girox.authentication.models import MyUser
from girox.blog.models import Post, Category
from girox.core.admin import CustomModelAdmin


class PostModelAuthorChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "%s %s" % (obj.first_name, obj.last_name)


class PostModelAdminForm(forms.ModelForm):
    author = PostModelAuthorChoiceField(queryset=MyUser.objects.filter(is_active=True).all())

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
