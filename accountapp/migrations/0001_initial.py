# Generated by Django 3.1.3 on 2021-06-28 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('username', models.CharField(max_length=150, unique=True)),
                ('is_superuser', models.IntegerField(blank=True, null=True)),
                ('realname', models.CharField(max_length=128)),
                ('phone', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=256)),
                ('date_of_birth', models.DateField()),
                ('date_joined', models.DateTimeField()),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_staff', models.IntegerField(blank=True, null=True)),
                ('is_active', models.IntegerField(blank=True, null=True)),
                ('first_name', models.CharField(blank=True, max_length=30, null=True)),
                ('last_name', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'db_table': 'auth_user',
            },
        ),
    ]
