# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20160310_1607'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='text',
            field=models.TextField(default=b''),
            preserve_default=True,
        ),
    ]
