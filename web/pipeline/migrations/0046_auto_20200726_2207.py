# Generated by Django 2.2.13 on 2020-07-26 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pipeline', '0045_auto_20200724_2237'),
    ]

    operations = [
        migrations.AddField(
            model_name='community',
            name='percent_10_2',
            field=models.FloatField(blank=True, help_text='portion (0-1) of area with 25/5 speeds (calc. by road length)', null=True),
        ),
        migrations.AddField(
            model_name='community',
            name='percent_5_1',
            field=models.FloatField(blank=True, help_text='portion (0-1) of area with 25/5 speeds (calc. by road length)', null=True),
        ),
    ]