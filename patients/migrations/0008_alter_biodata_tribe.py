# Generated by Django 5.0.7 on 2024-07-29 11:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0007_tribes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biodata',
            name='tribe',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='patients.tribes'),
        ),
    ]
