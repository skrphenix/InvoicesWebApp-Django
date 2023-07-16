import unittest
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
    return resp


def invoices():
    """
    Get list of invoices
    """

    resp = requests.get(base_url)
    return resp


def get_invoice(invoice_no: str):
    """
    Get a Invoice
    """

    resp = requests.get(
        base_url + "{}/".format(invoice_no)
    )
    return resp


# Update a Invoice
def update_invoice(invoice_no: str, json: _T):
    """
    Update a Invoice
    """

    resp = requests.put(
        base_url + "update/{}/".format(invoice_no),
        json=json
    )
    return resp


def delete_invoice(invoice_no: str):
    """
    Delete a Invoice
    """

    resp = requests.delete(
        base_url + "delete/{}/".format(invoice_no)
    )
    return resp


class APITestCases(unittest.TestCase):
    def test_create_invoice(self):
        resp = create_invoice(
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
        )

        self.assertTrue(resp.ok)
        print(resp.status_code, resp)

    def test_invoices(self):
        resp = invoices()

        self.assertTrue(resp.ok)
        print(resp.status_code, resp)

    def test_get_invoice(self):
        resp = get_invoice("no1")

        self.assertTrue(resp.ok)
        print(resp.status_code, resp)

    def test_update_invoice(self):
        resp = update_invoice(
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
        )

        self.assertTrue(resp.ok)
        print(resp.status_code, resp)

    def test_delete_invoice(self):
        resp = delete_invoice("no1")

        self.assertTrue(resp.ok)
        print(resp.status_code, resp)


if __name__ == '__main__':
    # Run the tests one by one
    test_suite = unittest.TestSuite()
    methods = [
        "test_create_invoice",
        "test_invoices",
        "test_get_invoice",
        "test_update_invoice",
        "test_delete_invoice"
    ]

    test_suite.addTests([APITestCases(method) for method in methods])

    runner = unittest.TextTestRunner()
    runner.run(test_suite)
