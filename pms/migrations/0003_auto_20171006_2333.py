# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-06 17:33
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20171003_1611'),
        ('pms', '0002_auto_20171006_1116'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='author', to='core.Profile'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='issue',
            name='priority',
            field=models.IntegerField(choices=[(2, 'HIGH'), (0, 'LOW'), (1, 'NORMAL'), (3, 'URGENT')], default=0),
        ),
        migrations.AlterField(
            model_name='issue',
            name='status',
            field=models.IntegerField(choices=[(3, 'AWAITING_QA'), (1, 'IN_PROGRESS'), (0, 'NEW'), (2, 'ON_HOLD'), (4, 'QA_VERIFIED')], default=0),
        ),
        migrations.AlterField(
            model_name='issue',
            name='tracker',
            field=models.IntegerField(choices=[(0, 'BUG'), (1, 'FEATURE'), (2, 'SUPPORT')], default=0),
        ),
    ]
