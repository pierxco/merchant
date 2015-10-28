# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0002_alter_pincharge_and_pinrefund_success_default'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pincharge',
            name='ip_address',
            field=models.GenericIPAddressField(),
        ),
        migrations.AlterField(
            model_name='worldpayresponse',
            name='ip_address',
            field=models.GenericIPAddressField(null=True, blank=True),
        ),
    ]
