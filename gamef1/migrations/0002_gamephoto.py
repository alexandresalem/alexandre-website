# Generated by Django 3.0.3 on 2020-02-29 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamef1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GamePhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f1_image', models.ImageField(blank=True, null=True, upload_to='cars/')),
            ],
        ),
    ]