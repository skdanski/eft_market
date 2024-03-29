# Generated by Django 4.1.2 on 2022-12-08 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_product_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('waitingapproval', 'Waiting Approval'), ('active', 'Active'), ('deleted', 'Deleted'), ('closed', 'Bid Closed')], default='active', max_length=50),
        ),
    ]
