# Generated by Django 2.1.2 on 2018-10-19 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autonsured', '0003_getquote_contact_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='getquote',
            name='contact_phone',
            field=models.IntegerField(default='1213131'),
        ),
    ]
