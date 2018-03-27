# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('Quetion_Category', models.CharField(max_length=200, default='General')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('category', models.ForeignKey(to='MCQTest.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('gender', models.CharField(max_length=15)),
                ('phone_number', models.IntegerField(verbose_name='Mobile Number')),
                ('address', models.TextField(verbose_name='Address')),
                ('country', models.CharField(max_length=25)),
                ('state', models.CharField(max_length=25)),
                ('city', models.CharField(max_length=25)),
                ('pin_code', models.IntegerField(verbose_name='Pin_Code')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(to='MCQTest.Question'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='answers',
            name='answer',
            field=models.ForeignKey(to='MCQTest.Choice'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='answers',
            name='question',
            field=models.ForeignKey(to='MCQTest.Question'),
            preserve_default=True,
        ),
    ]
