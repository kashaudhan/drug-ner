# Generated by Django 4.0 on 2021-12-26 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drug', '0002_rename_drug_format_drug_drug_form'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drug',
            name='pack_size',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
