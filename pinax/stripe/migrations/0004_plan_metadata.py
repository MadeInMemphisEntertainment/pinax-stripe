# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-03 16:33
from __future__ import unicode_literals

from django.db import migrations

import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pinax_stripe', '0003_make_cvc_check_blankable'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='metadata',
            field=jsonfield.fields.JSONField(null=True),
        ),
    ]
