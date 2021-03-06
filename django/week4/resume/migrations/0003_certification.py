# Generated by Django 2.0.2 on 2018-02-10 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0002_qualification'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('date_obtained', models.DateField()),
                ('status', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'ordering': ['-date_obtained'],
            },
        ),
    ]
