# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MCQTest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='Short_Cut',
            field=models.CharField(max_length=10, default='GL'),
            preserve_default=True,
        ),
    ]
