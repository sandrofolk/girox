# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-14 20:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('title', models.CharField(max_length=250, verbose_name='título')),
                ('description', models.TextField(blank=True, null=True, verbose_name='descrição')),
                ('is_public', models.BooleanField(default=True, verbose_name='é público?')),
                ('date_added', models.DateField(blank=True, null=True, verbose_name='adicionado em')),
                ('order', models.PositiveIntegerField(default=9999)),
            ],
            options={
                'abstract': False,
                'ordering': ('-modified', '-created'),
                'get_latest_by': 'modified',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('file', models.ImageField(upload_to='album_photos/', verbose_name='arquivo')),
                ('description', models.TextField(blank=True, null=True, verbose_name='descrição')),
                ('is_public', models.BooleanField(default=True, verbose_name='é pública?')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gallery.Album')),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text=None, through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'abstract': False,
                'ordering': ('-modified', '-created'),
                'get_latest_by': 'modified',
            },
        ),
        migrations.AddField(
            model_name='album',
            name='cover_photo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='gallery.Photo'),
        ),
        migrations.AddField(
            model_name='album',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text=None, through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
