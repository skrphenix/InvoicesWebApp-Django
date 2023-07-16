from rest_framework import serializers

from .models import Invoice, InvoiceDetails


class InvoiceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceDetails
        fields = ("description", "quantity", "unit_price", "price")


class InvoiceSerializer(serializers.ModelSerializer):
    details = InvoiceDetailSerializer(many=True)

    class Meta:
        model = Invoice
        fields = ("date", "invoice_no", "customer_name", "details")

    def create(self, validated_data):
        details_data = validated_data.pop("details")
        invoice = Invoice.objects.create(**validated_data)
        for detail_data in details_data:
            InvoiceDetails.objects.create(invoice=invoice, **detail_data)
        return invoice

    def update(self, instance: "Invoice", validated_data):
        details_data = validated_data.pop('details', [])

        instance.date = validated_data.get("date", instance.date)
        instance.invoice_no = validated_data.get("invoice_no", instance.invoice_no)
        instance.customer_name = validated_data.get("customer_name", instance.customer_name)

        instance.save()
        instance.details.all().delete()
        for detail_data in details_data:
            InvoiceDetails.objects.create(invoice=instance, **detail_data)
        return instance
