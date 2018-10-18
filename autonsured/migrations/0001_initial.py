# Generated by Django 2.1.2 on 2018-10-18 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GetQuote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_first_name', models.CharField(help_text='This is the help text!', max_length=100)),
                ('contact_middle_name', models.CharField(max_length=100)),
                ('contact_last_name', models.CharField(max_length=100)),
                ('contact_street_address', models.CharField(max_length=250)),
                ('contact_city', models.CharField(choices=[('a', 'New York'), ('b', 'Miami')], max_length=100)),
                ('contact_state', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.CharField(max_length=150)),
                ('body', models.TextField(blank=True)),
            ],
        ),
    ]
