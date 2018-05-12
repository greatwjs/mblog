# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0002_playinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='classinfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('class1', models.CharField(max_length=20)),
                ('score', models.CharField(max_length=20)),
            ],
        ),
    ]
