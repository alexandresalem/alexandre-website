# Generated by Django 3.0.4 on 2020-04-25 01:33

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamef1', '0012_auto_20200412_2245'),
    ]

    operations = [
        migrations.AddField(
            model_name='formula',
            name='imagephoto',
            field=models.ImageField(default=1, storage=django.core.files.storage.FileSystemStorage(location='/media/gamef1'), upload_to=''),
            preserve_default=False,
        ),
    ]
