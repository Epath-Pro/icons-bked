# Generated by Django 3.2.5 on 2021-08-02 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Icons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('code', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=200)),
                ('created', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
