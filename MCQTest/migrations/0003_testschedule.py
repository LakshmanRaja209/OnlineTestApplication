# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('MCQTest', '0002_category_short_cut'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestSchedule',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('schedule_date', models.DateTimeField(verbose_name='Date Scheduled')),
                ('category', models.ForeignKey(to='MCQTest.Category')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
