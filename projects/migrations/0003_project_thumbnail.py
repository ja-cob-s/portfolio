# Generated by Django 2.2.2 on 2019-06-21 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20190621_2209'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='thumbnail',
            field=models.CharField(default='#', max_length=100),
            preserve_default=False,
        ),
    ]