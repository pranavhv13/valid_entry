# Generated by Django 5.1.1 on 2024-10-07 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0008_remove_formconfig_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='formconfig',
            name='form_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
