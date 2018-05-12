# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='playinfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('playno', models.CharField(max_length=20)),
                ('playname', models.CharField(max_length=20)),
                ('class1', models.CharField(max_length=5)),
                ('xiangmu', models.CharField(max_length=5)),
                ('mingci', models.CharField(max_length=5)),
            ],
        ),
    ]
