# Generated by Django 4.2 on 2023-05-23 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_archivetender_archivefile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='archivefile',
            old_name='file',
            new_name='archive_file',
        ),
        migrations.RenameField(
            model_name='archivefile',
            old_name='tender',
            new_name='archive_tender',
        ),
    ]
