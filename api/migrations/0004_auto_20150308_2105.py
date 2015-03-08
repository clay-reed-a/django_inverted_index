# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20150308_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appearance',
            name='listing',
            field=models.ForeignKey(to='api.Listing'),
        ),
    ]
