# Generated by Django 2.2.13 on 2020-07-10 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pipeline', '0018_auto_20200710_2203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='fn_community_name',
            field=models.CharField(default='', max_length=127),
        ),
    ]
