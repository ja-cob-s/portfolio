# Generated by Django 2.2.2 on 2019-06-22 04:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20190622_0225'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='created_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]