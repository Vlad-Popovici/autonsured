# Generated by Django 2.1.2 on 2018-11-02 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dummy', '0003_programmer'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('name',)},
        ),
    ]
