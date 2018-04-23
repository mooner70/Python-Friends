# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-04-20 22:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friendsapp', '0002_user_firend_of'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='firend_of',
        ),
        migrations.AddField(
            model_name='user',
            name='friend_of',
            field=models.ManyToManyField(related_name='_user_friend_of_+', to='friendsapp.User'),
        ),
    ]