# Generated by Django 3.2 on 2021-06-28 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='blog',
            field=models.URLField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='description',
            field=models.TextField(blank=True, help_text='소개', null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='github',
            field=models.URLField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, help_text='대표 이미지', null=True, upload_to='profile/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='nickname',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True),
        ),
    ]