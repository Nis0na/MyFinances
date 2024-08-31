# Generated by Django 5.1 on 2024-08-31 10:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("backend", "0056_user_stripe_customer_id"),
        ("billing", "0005_auto_20240830_1655"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="BillingUsage",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("event_name", models.CharField(max_length=100)),
                ("event_type", models.CharField(choices=[("usage", "Metered Usage")], default="usage", max_length=20)),
                ("quantity", models.PositiveSmallIntegerField(default=1)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("processed_at", models.DateTimeField(blank=True, null=True)),
                ("processed", models.BooleanField(default=False)),
                ("stripe_unique_usage_identifier", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "organization",
                    models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to="backend.organization"),
                ),
                (
                    "user",
                    models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
                ),
            ],
            options={
                "abstract": False,
                "constraints": [
                    models.CheckConstraint(
                        condition=models.Q(
                            models.Q(("organization__isnull", False), ("user__isnull", True)),
                            models.Q(("organization__isnull", True), ("user__isnull", False)),
                            _connector="OR",
                        ),
                        name="billing_billingusage_check_user_or_organization",
                    )
                ],
            },
        ),
    ]
