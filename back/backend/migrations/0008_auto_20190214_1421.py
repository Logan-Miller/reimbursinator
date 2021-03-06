# Generated by Django 2.1.5 on 2019-02-14 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_merge_20190213_2318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='field',
            name='data_decimal',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9),
        ),
        migrations.AlterField(
            model_name='field',
            name='number',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='section',
            name='auto_submit',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='section',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='section',
            name='required',
            field=models.BooleanField(default=False),
        ),
    ]
