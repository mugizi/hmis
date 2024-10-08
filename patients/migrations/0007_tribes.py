# Generated by Django 5.0.7 on 2024-07-29 10:52

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0006_rename_categoryname_servicecategory_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tribes',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID')),
                ('tribe', models.CharField(default='', max_length=150)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
