import requests

from typing import Dict, Any

_T = Dict[str, Any]
base_url = "http://127.0.0.1:8000/api/invoices/"


def create_invoice(json: _T):
    """
    Create a Invoice if not exists
    """

    resp = requests.post(
        base_url + "create",
        json=json
    )
    print(resp.status_code, resp.json())


def invoices():
    """
    Get list of invoices
    """

    resp = requests.get(base_url)
    resp.raise_for_status()
    return resp.status_code, resp.json()


def get_invoice(invoice_no: str):
    """
    Get a Invoice
    """

    resp = requests.get(
        base_url + "{}/".format(invoice_no)
    )
    resp.raise_for_status()
    return resp.status_code, resp.json()


# Update a Invoice
def update_invoice(invoice_no: str, json: _T):
    """
    Update a Invoice
    """

    resp = requests.put(
        base_url + "update/{}/".format(invoice_no),
        json=json
    )
    resp.raise_for_status()
    return resp.status_code, resp.json()


def delete_invoice(invoice_no: str):
    """
    Delete a Invoice
    """

    resp = requests.delete(
        base_url + "delete/{}/".format(invoice_no)
    )
    resp.raise_for_status()
    return resp.status_code, resp.json()


if __name__ == '__main__':
    print(create_invoice(
        {
            "details": [
                {
                    "description": "item1",
                    "quantity": 1,
                    "unit_price": 1000.00,
                    "price": 2.00
                }
            ],
            "date": "2023-07-13",
            "invoice_no": "no1",
            "customer_name": "skr",
        }
    ))

    print(invoices())

    print(get_invoice("no1"))

    print(update_invoice(
        "no1",
        {
            "details": [
                {
                    "description": "item1",
                    "quantity": 1,
                    "unit_price": 1000.00,
                    "price": 2.00
                }
            ],
            "date": "2023-07-13",
            "invoice_no": "no1",
            "customer_name": "john",
        }
    ))

    print(invoices())

    print(delete_invoice("no1"))

    print(get_invoice("no1"))
