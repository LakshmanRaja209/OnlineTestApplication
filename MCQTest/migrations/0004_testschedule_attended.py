# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MCQTest', '0003_testschedule'),
    ]

    operations = [
        migrations.AddField(
            model_name='testschedule',
            name='attended',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
