# Generated by Django 4.0.4 on 2022-04-27 21:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('charitable', '0017_emailreminder'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailreminder',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='emailreminder',
            name='your_reminder',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
