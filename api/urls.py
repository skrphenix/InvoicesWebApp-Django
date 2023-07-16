from django.urls import path

from . import views

sub_path = "invoices/"

urlpatterns = [
    path("", views.api_overview),
    path(sub_path, views.invoices),
    path(sub_path + "<str:invoice_no>/", views.get_invoice),
    path(sub_path + "create", views.create_invoice),
    path(sub_path + "update/<str:invoice_no>/", views.update_invoice),
    path(sub_path + "delete/<str:invoice_no>/", views.delete_invoice),
]
