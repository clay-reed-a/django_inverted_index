# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_word_listings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appearance',
            name='listing',
            field=models.ForeignKey(related_name='appearances', to='api.Listing'),
        ),
        migrations.AlterField(
            model_name='appearance',
            name='word',
            field=models.ForeignKey(related_name='appearances', to='api.Word'),
        ),
    ]
