# Generated by Django 4.0.6 on 2022-07-18 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_bid_status_alter_bid_source'),
    ]

    operations = [
        migrations.AddField(
            model_name='bid',
            name='product',
            field=models.CharField(default='Androgard', max_length=50),
            preserve_default=False,
        ),
    ]