# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='listings',
            field=models.ManyToManyField(to='api.Listing', through='api.Appearance'),
            preserve_default=True,
        ),
    ]
