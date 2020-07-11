# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-04 20:50
from __future__ import unicode_literals

import modernomad.core.models
from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0074_auto_20190304_2038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(help_text='Should be 500x325px or a 1 to 0.65 ratio. If it is not this size, it will automatically be resized.', upload_to=modernomad.core.models.resource_img_upload_to),
        ),
    ]
