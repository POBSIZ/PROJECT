# Generated by Django 3.1.3 on 2021-07-04 20:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calendarapp', '0002_auto_20210705_0412'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='time',
            name='f_day',
        ),
        migrations.AddField(
            model_name='time',
            name='f_ymd',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='calendarapp.ymd'),
        ),
    ]
