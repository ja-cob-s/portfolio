# Generated by Django 2.2.2 on 2019-06-21 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_project_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='github',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='url',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
