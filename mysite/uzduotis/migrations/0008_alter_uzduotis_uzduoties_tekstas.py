# Generated by Django 5.0.1 on 2024-01-29 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uzduotis', '0007_alter_uzduotis_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uzduotis',
            name='uzduoties_tekstas',
            field=models.TextField(verbose_name='Užduotis'),
        ),
    ]
