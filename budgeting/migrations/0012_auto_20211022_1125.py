# Generated by Django 3.2.4 on 2021-10-22 07:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('budgeting', '0011_auto_20211022_1048'),
    ]

    operations = [
        migrations.RenameField(
            model_name='noncurrentliabilities',
            old_name='currentAssetType',
            new_name='nCurrentLbltType',
        ),
        migrations.RenameField(
            model_name='noncurrentliabilitiestype',
            old_name='currentAssetName',
            new_name='nCurrentLbltName',
        ),
    ]
