# Generated by Django 2.1.2 on 2018-10-19 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autonsured', '0002_auto_20181018_1721'),
    ]

    operations = [
        migrations.AddField(
            model_name='getquote',
            name='contact_phone',
            field=models.IntegerField(default='1213131', max_length=15),
        ),
    ]
