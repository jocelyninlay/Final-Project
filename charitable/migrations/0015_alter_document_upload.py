# Generated by Django 4.0.4 on 2022-04-26 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charitable', '0014_remove_donationrecord_donationreceipt_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='upload',
            field=models.ImageField(upload_to='reciepts'),
        ),
    ]