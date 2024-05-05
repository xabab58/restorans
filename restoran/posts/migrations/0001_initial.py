# Generated by Django 2.2.19 on 2024-05-04 16:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('last_name', models.CharField(max_length=10)),
                ('patronymic', models.CharField(max_length=10)),
                ('tabel', models.IntegerField(default=9999, validators=[django.core.validators.MaxValueValidator(9999)])),
            ],
        ),
        migrations.CreateModel(
            name='restorans',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('image', models.ImageField(blank=True, null=True, upload_to='pictures/')),
            ],
        ),
    ]
