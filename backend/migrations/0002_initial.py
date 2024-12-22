# Generated by Django 5.1.4 on 2024-12-21 22:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("backend", "0001_initial"),
        ("core", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="client",
            name="organization",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="core.organization",
            ),
        ),
        migrations.AddField(
            model_name="client",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="defaultvalues",
            name="client",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="default_values",
                to="backend.client",
            ),
        ),
        migrations.AddField(
            model_name="defaultvalues",
            name="organization",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="core.organization",
            ),
        ),
        migrations.AddField(
            model_name="defaultvalues",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="filestoragefile",
            name="last_edited_by",
            field=models.ForeignKey(
                blank=True,
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="files_edited",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="filestoragefile",
            name="organization",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="core.organization",
            ),
        ),
        migrations.AddField(
            model_name="filestoragefile",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="invoice",
            name="client_to",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="backend.client",
            ),
        ),
        migrations.AddField(
            model_name="invoice",
            name="organization",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="core.organization",
            ),
        ),
        migrations.AddField(
            model_name="invoice",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="invoice",
            name="items",
            field=models.ManyToManyField(blank=True, to="backend.invoiceitem"),
        ),
        migrations.AddField(
            model_name="invoiceproduct",
            name="organization",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="core.organization",
            ),
        ),
        migrations.AddField(
            model_name="invoiceproduct",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="invoicerecurringprofile",
            name="client_to",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="backend.client",
            ),
        ),
        migrations.AddField(
            model_name="invoicerecurringprofile",
            name="items",
            field=models.ManyToManyField(blank=True, to="backend.invoiceitem"),
        ),
        migrations.AddField(
            model_name="invoicerecurringprofile",
            name="organization",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="core.organization",
            ),
        ),
        migrations.AddField(
            model_name="invoicerecurringprofile",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="invoice",
            name="invoice_recurring_profile",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="generated_invoices",
                to="backend.invoicerecurringprofile",
            ),
        ),
        migrations.AddField(
            model_name="invoicereminder",
            name="invoice",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="invoice_reminders",
                to="backend.invoice",
            ),
        ),
        migrations.AddField(
            model_name="invoiceurl",
            name="created_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="invoiceurl",
            name="invoice",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="invoice_urls",
                to="backend.invoice",
            ),
        ),
        migrations.AddField(
            model_name="monthlyreport",
            name="organization",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="core.organization",
            ),
        ),
        migrations.AddField(
            model_name="monthlyreport",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="monthlyreportrow",
            name="client",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="backend.client",
            ),
        ),
        migrations.AddField(
            model_name="monthlyreport",
            name="items",
            field=models.ManyToManyField(blank=True, to="backend.monthlyreportrow"),
        ),
        migrations.AddField(
            model_name="multifileupload",
            name="files",
            field=models.ManyToManyField(related_name="multi_file_uploads", to="backend.filestoragefile"),
        ),
        migrations.AddField(
            model_name="multifileupload",
            name="organization",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="core.organization",
            ),
        ),
        migrations.AddField(
            model_name="multifileupload",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="receipt",
            name="organization",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="core.organization",
            ),
        ),
        migrations.AddField(
            model_name="receipt",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="receiptdownloadtoken",
            name="file",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="backend.receipt"),
        ),
        migrations.AddField(
            model_name="receiptdownloadtoken",
            name="user",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddConstraint(
            model_name="client",
            constraint=models.CheckConstraint(
                condition=models.Q(
                    models.Q(("organization__isnull", False), ("user__isnull", True)),
                    models.Q(("organization__isnull", True), ("user__isnull", False)),
                    _connector="OR",
                ),
                name="backend_client_check_user_or_organization",
            ),
        ),
        migrations.AddConstraint(
            model_name="defaultvalues",
            constraint=models.CheckConstraint(
                condition=models.Q(
                    models.Q(("organization__isnull", False), ("user__isnull", True)),
                    models.Q(("organization__isnull", True), ("user__isnull", False)),
                    _connector="OR",
                ),
                name="backend_defaultvalues_check_user_or_organization",
            ),
        ),
        migrations.AddConstraint(
            model_name="filestoragefile",
            constraint=models.CheckConstraint(
                condition=models.Q(
                    models.Q(("organization__isnull", False), ("user__isnull", True)),
                    models.Q(("organization__isnull", True), ("user__isnull", False)),
                    _connector="OR",
                ),
                name="backend_filestoragefile_check_user_or_organization",
            ),
        ),
        migrations.AddConstraint(
            model_name="invoiceproduct",
            constraint=models.CheckConstraint(
                condition=models.Q(
                    models.Q(("organization__isnull", False), ("user__isnull", True)),
                    models.Q(("organization__isnull", True), ("user__isnull", False)),
                    _connector="OR",
                ),
                name="backend_invoiceproduct_check_user_or_organization",
            ),
        ),
        migrations.AddConstraint(
            model_name="invoicerecurringprofile",
            constraint=models.CheckConstraint(
                condition=models.Q(
                    models.Q(("organization__isnull", False), ("user__isnull", True)),
                    models.Q(("organization__isnull", True), ("user__isnull", False)),
                    _connector="OR",
                ),
                name="backend_invoicerecurringprofile_check_user_or_organization",
            ),
        ),
        migrations.AddConstraint(
            model_name="invoice",
            constraint=models.CheckConstraint(
                condition=models.Q(
                    models.Q(("organization__isnull", False), ("user__isnull", True)),
                    models.Q(("organization__isnull", True), ("user__isnull", False)),
                    _connector="OR",
                ),
                name="backend_invoice_check_user_or_organization",
            ),
        ),
        migrations.AddConstraint(
            model_name="monthlyreport",
            constraint=models.CheckConstraint(
                condition=models.Q(
                    models.Q(("organization__isnull", False), ("user__isnull", True)),
                    models.Q(("organization__isnull", True), ("user__isnull", False)),
                    _connector="OR",
                ),
                name="backend_monthlyreport_check_user_or_organization",
            ),
        ),
        migrations.AddConstraint(
            model_name="multifileupload",
            constraint=models.CheckConstraint(
                condition=models.Q(
                    models.Q(("organization__isnull", False), ("user__isnull", True)),
                    models.Q(("organization__isnull", True), ("user__isnull", False)),
                    _connector="OR",
                ),
                name="backend_multifileupload_check_user_or_organization",
            ),
        ),
        migrations.AddConstraint(
            model_name="receipt",
            constraint=models.CheckConstraint(
                condition=models.Q(
                    models.Q(("organization__isnull", False), ("user__isnull", True)),
                    models.Q(("organization__isnull", True), ("user__isnull", False)),
                    _connector="OR",
                ),
                name="backend_receipt_check_user_or_organization",
            ),
        ),
    ]
