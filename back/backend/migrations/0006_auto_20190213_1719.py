# Generated by Django 2.1.5 on 2019-02-14 01:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_field_field_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='field',
            old_name='type',
            new_name='field_type',
        ),
    ]
