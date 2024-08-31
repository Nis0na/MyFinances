import logging
from datetime import datetime

import stripe
from django.db.models.signals import pre_delete, post_save
from django.dispatch import receiver
from django.utils.timezone import make_aware

from backend.models import Invoice, User
from billing.models import BillingUsage

# from backend.models import FileStorageFile, MultiFileUpload, _private_storage, StorageUsage, PlanFeature

logger = logging.getLogger(__name__)


@receiver(post_save, sender=BillingUsage)
def usage_occurred(sender, instance: BillingUsage, created, **kwargs):
    if not created or instance.processed:
        return

    if instance.event_type != "usage":
        return  # may add storage at a later point

    if not instance.user:
        print("CANNOT HANDLE ORGS AT THE MOMENT!")
        return  # todo: cannot handle organisations at the moment

    stripe_customer_id = instance.user.stripe_customer_id

    if not stripe_customer_id:
        print(f"No stripe customer id for user {instance.user.id}")
        return  # todo

    meter_event = stripe.billing.MeterEvent.create(
        event_name=instance.event_name, payload={"value": instance.quantity, f"stripe_customer_id": stripe_customer_id}
    )

    if meter_event.created:
        instance.stripe_unique_usage_identifier = meter_event.identifier
        instance.set_processed(datetime.fromtimestamp(meter_event.created))

    return


@receiver(post_save, sender=Invoice)
def created_invoice(sender, instance: Invoice, created, **kwargs):
    if not created:
        return

    BillingUsage.objects.create(
        owner=instance.owner,
        event_name="invoices_created",
    )
    return
