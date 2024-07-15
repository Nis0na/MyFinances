# Generated by Django 5.0.4 on 2024-06-10 16:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("backend", "0035_client_contact_method"),
    ]

    operations = [
        migrations.CreateModel(
            name="APIAuthToken",
            fields=[
                ("key", models.CharField(max_length=40, primary_key=True, serialize=False, verbose_name="Key")),
                ("created", models.DateTimeField(auto_now_add=True, verbose_name="Created")),
                ("user", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
