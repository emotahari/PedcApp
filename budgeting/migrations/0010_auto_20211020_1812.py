# Generated by Django 3.2.4 on 2021-10-20 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('budgeting', '0009_currentasset_currentassetstype_currentliabilities_currentliabilitiestype_noncurrentasset_noncurrenta'),
    ]

    operations = [
        migrations.RenameField(
            model_name='noncurrentasset',
            old_name='currentAssetType',
            new_name='nCurrentAssetType',
        ),
        migrations.RenameField(
            model_name='noncurrentassetstype',
            old_name='currentAssetName',
            new_name='nCurrentAssetName',
        ),
    ]