# Generated by Django 4.2 on 2023-06-08 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_tender_tittle_ar'),
    ]

    operations = [
        migrations.AddField(
            model_name='tender',
            name='city',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='tender',
            name='type_name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
