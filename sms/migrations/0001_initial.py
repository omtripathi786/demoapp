# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('course', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Courses',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('roll_number', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('courses', models.ForeignKey(to='sms.Courses')),
            ],
            options={
                'verbose_name_plural': 'Students',
            },
            bases=(models.Model,),
        ),
    ]
