# Generated by Django 5.0.7 on 2024-08-01 12:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0015_drugs_description_providedservices'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='biodata',
            name='District',
        ),
    ]
