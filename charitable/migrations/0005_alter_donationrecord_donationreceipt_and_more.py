# Generated by Django 4.0.4 on 2022-04-23 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charitable', '0004_rename_interval_volunteergoal_interval'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donationrecord',
            name='donationreceipt',
            field=models.ImageField(blank=True, upload_to='reciepts'),
        ),
        migrations.AlterField(
            model_name='volunteerrecord',
            name='volunteerreceipt',
            field=models.ImageField(blank=True, upload_to='reciepts'),
        ),
    ]
