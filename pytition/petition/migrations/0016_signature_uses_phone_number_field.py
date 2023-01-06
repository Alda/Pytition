# Generated by Django 2.2.28 on 2022-08-20 11:27

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('petition', '0015_petitiontemplate_has_share_buttons'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signature',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=20, region=None, verbose_name='Phone number'),
        ),
    ]