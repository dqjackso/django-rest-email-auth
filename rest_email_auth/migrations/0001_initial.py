# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-31 23:58
from __future__ import unicode_literals

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
            name='EmailAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('email', models.EmailField(max_length=255, verbose_name='email')),
                ('is_verified', models.BooleanField(default=False, help_text='Boolean indicating if the user has verified ownership of the email address.', verbose_name='is verified')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='email_addresses', related_query_name='email_address', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'email address',
                'verbose_name_plural': 'email addresses',
            },
        ),
    ]
