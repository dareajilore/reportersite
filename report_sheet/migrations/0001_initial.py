# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-09-29 13:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_report', models.FileField(upload_to='uploads/')),
                ('GT11_0000', models.DecimalField(decimal_places=2, max_digits=19)),
                ('GT11_0700', models.DecimalField(decimal_places=2, max_digits=19)),
                ('GT11_1800', models.DecimalField(decimal_places=2, max_digits=19)),
                ('GT11_2400', models.DecimalField(decimal_places=2, max_digits=19)),
                ('UAT_0000', models.DecimalField(decimal_places=2, max_digits=19)),
                ('UAT_0700', models.DecimalField(decimal_places=2, max_digits=19)),
                ('UAT_1800', models.DecimalField(decimal_places=2, max_digits=19)),
                ('UAT_2400', models.DecimalField(decimal_places=2, max_digits=19)),
                ('SST_0000', models.DecimalField(decimal_places=2, max_digits=19)),
                ('SST_0700', models.DecimalField(decimal_places=2, max_digits=19)),
                ('SST_1800', models.DecimalField(decimal_places=2, max_digits=19)),
                ('SST_2400', models.DecimalField(decimal_places=2, max_digits=19)),
                ('floweb_0000', models.DecimalField(decimal_places=2, max_digits=19)),
                ('floweb_2400', models.DecimalField(decimal_places=2, max_digits=19)),
                ('wbh_0000', models.DecimalField(decimal_places=2, max_digits=19)),
                ('wbh_2400', models.DecimalField(decimal_places=2, max_digits=19)),
            ],
        ),
    ]
