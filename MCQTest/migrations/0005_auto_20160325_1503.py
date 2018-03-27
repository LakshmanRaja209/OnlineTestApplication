# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MCQTest', '0004_testschedule_attended'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testschedule',
            name='schedule_date',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
    ]
