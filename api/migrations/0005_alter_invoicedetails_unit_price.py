# Generated by Django 4.2.3 on 2023-07-14 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_invoicedetails_unit_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoicedetails',
            name='unit_price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
