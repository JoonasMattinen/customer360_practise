# Generated by Django 4.2.6 on 2023-10-31 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer360', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='social_media',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
