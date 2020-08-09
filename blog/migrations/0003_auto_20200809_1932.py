# Generated by Django 2.2.15 on 2020-08-09 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200809_1920'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='summary',
        ),
        migrations.AddField(
            model_name='blog',
            name='body',
            field=models.TextField(default='Hope you like it'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog',
            name='pub_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=225),
        ),
    ]
