# Generated by Django 4.0.3 on 2022-05-13 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NationsInnDb', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='link',
            field=models.CharField(blank=True, max_length=160, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='location',
            field=models.CharField(blank=True, max_length=160, null=True),
        ),
    ]