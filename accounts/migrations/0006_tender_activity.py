# Generated by Django 4.2 on 2023-04-08 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_choice_alter_tender_end_time_remove_tender_sectoer_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tender',
            name='activity',
            field=models.BooleanField(default=True),
        ),
    ]
