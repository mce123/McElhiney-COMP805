# Generated by Django 2.0.2 on 2018-02-16 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0004_auto_20180216_0615'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='profile_statement',
            field=models.TextField(blank=True, null=True),
        ),
    ]
