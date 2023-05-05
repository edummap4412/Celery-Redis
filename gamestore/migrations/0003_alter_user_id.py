# Generated by Django 4.2 on 2023-04-07 19:27

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('gamestore', '0002_productlist_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
