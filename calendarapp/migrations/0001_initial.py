# Generated by Django 3.1.3 on 2021-07-04 16:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('o_day', models.IntegerField()),
                ('remain', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('o_year', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='YMD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('o_time', models.TimeField(blank=True, null=True)),
                ('create_time', models.DateTimeField(auto_now=True, null=True)),
                ('f_day', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='calendarapp.day')),
                ('f_person', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Month',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('o_month', models.IntegerField(blank=True, null=True)),
                ('f_year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calendarapp.year')),
            ],
        ),
        migrations.AddField(
            model_name='day',
            name='f_month',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='calendarapp.month'),
        ),
        migrations.AddField(
            model_name='day',
            name='f_ymd',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='calendarapp.ymd'),
        ),
    ]
