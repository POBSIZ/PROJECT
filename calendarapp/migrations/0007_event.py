# Generated by Django 3.2 on 2021-07-09 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendarapp', '0006_merge_0004_auto_20210708_0341_0005_auto_20210706_0411'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]
