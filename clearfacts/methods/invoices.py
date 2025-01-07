import json
import os

from .base import APIMethod
from clearfacts.models.invoices import InvoiceUploaded
from clearfacts.models.base import Errors
from clearfacts.constants.errors import APIError

class InvoiceMethods(APIMethod):

    def upload(self, vat_number: str, file_name: str, invoice_type: str, local_file_path: str):
        """
            Upload an invoice file using the GraphQL mutation.

            :param vat_number: The VAT number for the upload.
            :param file_name: The file name to be used in the upload.
            :param invoice_type: The type of invoice (e.g., "SALE").
            :param local_file_path: The local path to the file to be uploaded.
            :return: The response content from the API.
        """

        if not os.path.exists(local_file_path):
            raise FileNotFoundError(f"File not found at path: {local_file_path}")
        
        mutation = """
            mutation upload($vatnumber: String!, $filename: String!, $invoicetype: InvoiceTypeArgument!) {
                uploadFile(vatnumber: $vatnumber, filename: $filename, invoicetype: $invoicetype) {
                    uuid
                    amountOfPages
                }
            }
        """

        variables = {
            "vatnumber": vat_number,
            "filename": file_name,
            "invoicetype": invoice_type,
        }

        with open(local_file_path, "rb") as file_data:
            status, headers, response = self.api.post(
                data={"query": mutation, "variables": json.dumps(variables)},
                files={
                    "file": (file_name, file_data, "application/pdf")
                }
            )

        if status != 200:
            raise APIError(Errors().parse(response))
        return InvoiceUploaded().parse(response.get("data", {}).get("uploadFile"))