# Generated by Django 4.0.6 on 2022-07-18 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_bid_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='bid',
            name='source',
            field=models.IntegerField(default=1, max_length=5),
            preserve_default=False,
        ),
    ]
