# Generated by Django 4.2 on 2023-05-08 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_subscription_tittle_tender_start_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ImageField(upload_to='tender/')),
                ('tender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.tender')),
            ],
        ),
    ]
