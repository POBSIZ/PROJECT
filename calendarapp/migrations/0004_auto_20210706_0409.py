# Generated by Django 3.1.3 on 2021-07-05 19:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calendarapp', '0003_auto_20210705_0528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day',
            name='f_month',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='calendarapp.month'),
        ),
        migrations.AlterField(
            model_name='day',
            name='f_ymd',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='calendarapp.ymd'),
        ),
    ]