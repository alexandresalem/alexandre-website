# Generated by Django 3.0.3 on 2020-04-07 02:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gamef1', '0008_auto_20200406_2127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='f1model',
            name='f1text',
        ),
    ]
