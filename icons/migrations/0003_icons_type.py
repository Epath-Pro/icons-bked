# Generated by Django 3.2.5 on 2021-08-02 13:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('icons', '0002_auto_20210802_1920'),
    ]

    operations = [
        migrations.AddField(
            model_name='icons',
            name='type',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]