# Generated by Django 2.2.6 on 2019-10-06 22:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mpage', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='modeltestdb',
            old_name='cf1',
            new_name='ch1',
        ),
        migrations.RenameField(
            model_name='modeltestdb',
            old_name='cf2',
            new_name='ch2',
        ),
    ]
