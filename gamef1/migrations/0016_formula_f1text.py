# Generated by Django 3.0.4 on 2020-04-29 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamef1', '0015_auto_20200428_2009'),
    ]

    operations = [
        migrations.AddField(
            model_name='formula',
            name='f1text',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]
