from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Literal
from datetime import date
import uvicorn

# for testing the RPA 
app = FastAPI(title="Invoice API", description="API that returns invoice data in JSON format")

class InvoiceData(BaseModel):
    INVOICENUMBER: str
    DOCDATE: date
    VENDORNUMBER: str
    DELIVERYADDRESS: str
    VENDORNAME: str
    PURCHASEORDER: str

class ProcessData(BaseModel):
    document_type: Literal["PO", "Invoice", "PurchaseBill"]
    count: int
    id: str
    endpoint: str

# Sample data
sample_invoices = [
    InvoiceData(
        INVOICENUMBER="INV-2024-001",
        DOCDATE=date(2024, 1, 15),
        VENDORNUMBER="VEND-001",
        DELIVERYADDRESS="123 Main Street, New York, NY 10001",
        VENDORNAME="ABC Supply Company",
        PURCHASEORDER="PO-2024-001"
    ),
    InvoiceData(
        INVOICENUMBER="INV-2024-002",
        DOCDATE=date(2024, 1, 16),
        VENDORNUMBER="VEND-002",
        DELIVERYADDRESS="456 Oak Avenue, Los Angeles, CA 90210",
        VENDORNAME="XYZ Manufacturing Inc",
        PURCHASEORDER="PO-2024-002"
    ),
    InvoiceData(
        INVOICENUMBER="INV-2024-003",
        DOCDATE=date(2024, 1, 17),
        VENDORNUMBER="VEND-003",
        DELIVERYADDRESS="789 Pine Road, Chicago, IL 60601",
        VENDORNAME="Global Tech Solutions",
        PURCHASEORDER="PO-2024-003"
    )
]

# Sample process data
sample_processes = [
    ProcessData(
        document_type="PurchaseBill",
        count=1,
        id="PROC-003",
        endpoint="/processes/type/PurchaseBill"
    ),
    ProcessData(
        document_type="Invoice",
        count=0,
        id="PROC-005",
        endpoint="/processes/type/Invoice"
    )
]

endpoints = [
    "/",
    "/invoices",
    "/invoices/{invoice_number}",
    "/invoices/vendor/{vendor_number}",
    "/processes",
    "/processes/{process_id}",
    "/processes/type/{document_type}"
]

@app.get("/")
async def root():
    return {"message": "Welcome to the Invoice API"}

@app.get("/invoices", response_model=List[InvoiceData])
async def get_invoices():
    """Get all invoices"""
    return sample_invoices

@app.get("/invoices/{invoice_number}", response_model=InvoiceData)
async def get_invoice(invoice_number: str):
    """Get a specific invoice by invoice number"""
    for invoice in sample_invoices:
        if invoice.INVOICENUMBER == invoice_number:
            return invoice
    return {"error": "Invoice not found"}

@app.get("/invoices/vendor/{vendor_number}", response_model=List[InvoiceData])
async def get_invoices_by_vendor(vendor_number: str):
    """Get all invoices for a specific vendor"""
    vendor_invoices = [invoice for invoice in sample_invoices if invoice.VENDORNUMBER == vendor_number]
    return vendor_invoices

@app.get("/processes", response_model=List[ProcessData])
async def get_processes():
    """Get all processes"""
    return sample_processes
    return endpoints

@app.get("/processes/{process_id}", response_model=ProcessData)
async def get_process(process_id: str):
    """Get a specific process by ID"""
    for process in sample_processes:
        if process.id == process_id:
            return process
    return {"error": "Process not found"}

@app.get("/processes/type/{document_type}", response_model=List[ProcessData])
async def get_processes_by_type(document_type: str):
    """Get all processes of a specific type (PO, Invoice, or PurchaseBill)"""
    if document_type not in ["PO", "Invoice", "PurchaseBill"]:
        return {"error": "Invalid process name. Must be one of: PO, Invoice, PurchaseBill"}
    
    filtered_processes = [process for process in sample_processes if process.document_type == document_type]
    return filtered_processes

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)