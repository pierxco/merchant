# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pincharge',
            name='success',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='pinrefund',
            name='success',
            field=models.BooleanField(default=False),
        ),
    ]
