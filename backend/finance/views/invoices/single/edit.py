from datetime import datetime

from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

from core.types.requests import WebRequest
from backend.decorators import web_require_scopes
from backend.finance.models import Invoice, Client, InvoiceItem
from core.types.htmx import HtmxHttpRequest


# RELATED PATH FILES : \frontend\templates\pages\invoices\dashboard\_fetch_body.html, \backend\urls.py


# Function that takes an invoice object and makes a dict of its attributes
def invoice_get_existing_data(invoice_obj):
    stored_data = {
        "from_name": invoice_obj.self_name,
        "from_company": invoice_obj.self_company,
        "from_address": invoice_obj.self_address,
        "from_city": invoice_obj.self_city,
        "from_county": invoice_obj.self_county,
        "from_country": invoice_obj.self_country,
        "from_date_issued": invoice_obj.date_issued,
        "from_date_due": invoice_obj.date_due,
        "issue_date": invoice_obj.date_issued,
        "due_date": invoice_obj.date_due,
        "invoice_object": invoice_obj,
        "currency_symbol": invoice_obj.get_currency_symbol(),
        "rows": invoice_obj.items.all(),
        "account_holder_name": invoice_obj.account_holder_name,
        "sort_code": invoice_obj.sort_code,
        "account_number": invoice_obj.account_number,
        "reference": invoice_obj.reference,
        "logo": invoice_obj.logo,
    }
    if invoice_obj.client_to:
        stored_data["to_name"] = invoice_obj.client_to.name
        stored_data["to_company"] = invoice_obj.client_to.company
        stored_data["to_email"] = invoice_obj.client_to.email
        stored_data["is_representative"] = invoice_obj.client_to.is_representative
        # stored_data["to_address"] = invoice_obj.client_to.address
        # stored_data["to_city"] = invoice_obj.client_to.city
        # stored_data["to_county"] = invoice_obj.client_to.county
        # stored_data["to_country"] = invoice_obj.client_to.country
    else:
        stored_data["to_name"] = invoice_obj.client_name
        stored_data["to_company"] = invoice_obj.client_company
        stored_data["to_email"] = invoice_obj.client_email
        stored_data["to_address"] = invoice_obj.client_address
        stored_data["to_city"] = invoice_obj.client_city
        stored_data["to_county"] = invoice_obj.client_county
        stored_data["to_country"] = invoice_obj.client_country
        stored_data["is_representative"] = invoice_obj.client_is_representative

    if invoice_obj.client_to:
        stored_data["existing_client"] = invoice_obj.client_to

    return stored_data


# gets invoice object from invoice id, convert obj to dict, and renders edit.html while passing the stored invoice values to frontend
def invoice_edit_page_get(request, invoice_id):
    try:
        invoice = Invoice.objects.get(id=invoice_id)

        if not invoice.has_access(request.user):
            messages.error(request, "You are not permitted to edit this invoice")
            return redirect("finance:invoices:single:dashboard")
    except Invoice.DoesNotExist:
        messages.error(request, "Invoice not found")
        return redirect("finance:invoices:single:dashboard")

    # use to populate fields with existing data in edit_from_destination.html AND edit_to_destination.html
    data_to_populate = invoice_get_existing_data(invoice)
    return render(request, "pages/invoices/single/edit/edit.html", data_to_populate)


# when user changes/modifies any of the fields with new information (during edit invoice)
@require_http_methods(["POST"])
def edit_invoice(request: WebRequest, invoice_id):
    try:
        invoice = Invoice.objects.get(id=invoice_id)
    except Invoice.DoesNotExist:
        return JsonResponse({"message": "Invoice not found"}, status=404)

    if not invoice.has_access(request.user):
        return JsonResponse(
            {"message": "You do not have permission to edit this invoice"},
            status=403,
        )

    attributes_to_update = {
        "date_due": datetime.strptime(request.POST.get("date_due"), "%Y-%m-%d").date(),  # type: ignore[arg-type]
        "date_issued": request.POST.get("date_issued"),
        "self_name": request.POST.get("from_name"),
        "self_company": request.POST.get("from_company"),
        "self_address": request.POST.get("from_address"),
        "self_city": request.POST.get("from_city"),
        "self_county": request.POST.get("from_county"),
        "self_country": request.POST.get("from_country"),
        "notes": request.POST.get("notes"),
        "vat_number": request.POST.get("vat_number"),
        "reference": request.POST.get("reference"),
        "sort_code": request.POST.get("sort_code"),
        "account_number": request.POST.get("account_number"),
        "account_holder_name": request.POST.get("account_holder_name"),
    }

    client_to_id = request.POST.get("selected_client")
    try:
        client_to_obj = Client.filter_by_owner(request.actor).get(id=client_to_id)
    except (Client.DoesNotExist, ValueError):
        client_to_obj = None

    client_attrs = {
        "client_name": request.POST.get("to_name"),
        "client_company": request.POST.get("to_company"),
        "client_email": request.POST.get("to_email"),
        "client_address": request.POST.get("to_address"),
        "client_city": request.POST.get("to_city"),
        "client_county": request.POST.get("to_county"),
        "client_country": request.POST.get("to_country"),
    }

    if client_to_obj:
        invoice.client_to = client_to_obj

        for att in client_attrs.keys():
            setattr(invoice, att, None)
    else:
        attributes_to_update.update(
            {
                "client_name": request.POST.get("to_name"),
                "client_company": request.POST.get("to_company"),
                "client_email": request.POST.get("to_email"),
                "client_address": request.POST.get("to_address"),
                "client_city": request.POST.get("to_city"),
                "client_county": request.POST.get("to_county"),
                "client_country": request.POST.get("to_country"),
                "client_is_representative": True if request.POST.get("is_representative") == "on" else False,  # type: ignore[dict-item]
                "client_to": None,
            }
        )

    for column_name, new_value in attributes_to_update.items():
        setattr(invoice, column_name, new_value)

    invoice_items = [
        InvoiceItem.objects.create(name=row[0], description=row[1], hours=row[2], price_per_hour=row[3])
        for row in zip(
            request.POST.getlist("service_name[]"),
            request.POST.getlist("service_description[]"),
            request.POST.getlist("hours[]"),
            request.POST.getlist("price_per_hour[]"),
        )
    ]

    if invoice_items:
        invoice.items.set(invoice_items)

    invoice.save()

    messages.success(request, "Invoice edited")

    if request.htmx:
        return render(request, "base/toasts.html")

    return invoice_edit_page_get(request, invoice_id)


# decorator & view function for rendering page and updating invoice items in the backend
@require_http_methods(["GET", "POST"])
@web_require_scopes("invoices:write", False, False, "finance:invoices:single:dashboard")
def edit_invoice_page(request: WebRequest, invoice_id):
    if request.method == "POST":
        return edit_invoice(request, invoice_id)
    return invoice_edit_page_get(request, invoice_id)
