from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Invoice
from .serializers import InvoiceSerializer


@api_view(["GET"])
def api_overview(request):
    sub_path = "/invoices/"

    return Response({
        "GET: Invoices List": sub_path,
        "GET: Get a Invoice": sub_path + "<str:invoice_no>/",
        "POST: Create a Invoice": sub_path + "create/",
        "PUT: Update a Invoice": sub_path + "update/<str:invoice_no>/",
        "DELETE: Delete a Invoice": sub_path + "delete/<str:invoice_no>/"
    })


@api_view(["GET"])
def invoices(request):
    invoice_list = Invoice.objects.all()
    return Response(
        InvoiceSerializer(invoice_list, many=True).data
    )


@api_view(["GET"])
def get_invoice(request, invoice_no: str):
    try:
        invoice = Invoice.objects.get(invoice_no=invoice_no)
    except:
        return

    return Response(
        InvoiceSerializer(invoice, many=False).data
    )


@api_view(["POST"])
def create_invoice(request):
    serializer = InvoiceSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, 400)

    serializer.save()
    return Response(serializer.data)


@api_view(["PUT"])
def update_invoice(request, invoice_no: str):
    invoice = Invoice.objects.get(invoice_no=invoice_no)
    serializer = InvoiceSerializer(instance=invoice, data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, 400)

    serializer.save()
    return Response(serializer.data)


@api_view(["DELETE"])
def delete_invoice(request, invoice_no: str):
    invoice = Invoice.objects.get(invoice_no=invoice_no)
    invoice.delete()

    return Response(f"Invoice: {invoice_no} has been deleted successfully")
