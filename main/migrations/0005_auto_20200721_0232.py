# Generated by Django 3.0.4 on 2020-07-20 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_cartitems_specifications'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='labels',
            field=models.CharField(blank=True, choices=[('BestSeller', 'BestSeller'), ('New', 'New'), ('Spicy🔥', 'Spicy🔥')], max_length=25),
        ),
    ]
