# Invoice API

A FastAPI application that returns invoice data in JSON format.

## Features

The API returns JSON data containing the following fields:
- `INVOICENUMBER`: Invoice number
- `DOCDATE`: Document date
- `VENDORNUMBER`: Vendor number
- `DELIVERYADDRESS`: Delivery address
- `VENDORNAME`: Vendor name
- `PURCHASEORDER`: Purchase order number

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python main.py
```

The API will be available at `http://localhost:8000`

## API Endpoints

- `GET /` - Welcome message
- `GET /invoices` - Get all invoices
- `GET /invoices/{invoice_number}` - Get specific invoice by invoice number
- `GET /invoices/vendor/{vendor_number}` - Get all invoices for a specific vendor

## Interactive API Documentation

Once the server is running, you can access:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Example Response

```json
{
  "INVOICENUMBER": "INV-2024-001",
  "DOCDATE": "2024-01-15",
  "VENDORNUMBER": "VEND-001",
  "DELIVERYADDRESS": "123 Main Street, New York, NY 10001",
  "VENDORNAME": "ABC Supply Company",
  "PURCHASEORDER": "PO-2024-001"
}
```
