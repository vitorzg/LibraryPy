# Generated by Django 5.0.6 on 2024-06-13 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_rename_cliente_id_withdraw_client_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='withdraw',
            name='devolution_at',
            field=models.DateTimeField(null=True),
        ),
    ]
