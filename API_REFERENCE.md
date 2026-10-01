# Enterprise API Protocol Schema & JSON Reference Guide

This reference specifies the strict data schema requirements for interface layers interacting with the inventory network. All communications must conform strictly to the standard **JSON (JavaScript Object Notation)** specifications detailed below.

---

## Interface Endpoint: Product Management Core

### 1. Register New Logistical Stock Asset
- **Endpoint Route:** `/api/v1/inventory/items/create`
- **Network Method:** `POST`
- **Data Content-Type:** `application/json`

#### Strict Request Payload Schema
The payload must supply structured definitions matching explicit typing rules. Trailing commas inside objects or lists will trigger fatal validation alerts.

```json
{
  "requestMetadata": {
    "originatingSystem": "Warehouse-Streamlit-UI",
    "operatorId": 4092,
    "transactionTimestamp": "2026-10-01T11:58:00Z"
  },
  "productDetails": {
    "skuCode": "SAM-MIL-998A",
    "itemName": "Tactical Logistical Housing Unit",
    "category": "Storage Infrastructure",
    "unitDimensions": {
      "weightKg": 42.50,
      "isFragile": false
    },
    "initialStockLevel": 150,
    "supplierList": [
      "Kolkata Logistics Corp",
      "Delhi Supply Networks"
    ],
    "secondaryNotes": null
  }
}
```

#### Successful Response Schema (`HTTP Status 201 Created`)
Returned when data structures pass backend sanity filters, unique constraints, and schema validations.

```json
{
  "transactionStatus": "success",
  "generatedRecordId": 88342,
  "executionMetrics": {
    "dbWriteLatencyMs": 14.2,
    "cacheSynchronized": true
  },
  "payloadData": {
    "skuCode": "SAM-MIL-998A",
    "currentAvailableStock": 150,
    "allocationStatus": "In-Warehouse"
  }
}
```

#### Error Schema Responses

##### Case A: Syntax Parse Defect (`HTTP Status 400 Bad Request`)
Triggered if the payload contains an illegal single quote, missing boundary braces, or an invalid data type block.

```json
{
  "transactionStatus": "failed",
  "errorContext": {
    "errorCode": "ERR_JSON_PARSE_FAILURE",
    "errorReason": "Fatal syntax exception encountered at line 14, column 6. Trailing comma or unescaped token identified.",
    "remediationAction": "Re-run the payload string through a standard strict validator. Ensure all object keys maintain double quotation constraints."
  }
}
```

##### Case B: Schema Type Violation (`HTTP Status 422 Unprocessable Entity`)
Triggered if valid structural JSON violates business data boundaries (e.g., passing a negative value to stock tracking).

```json
{
  "transactionStatus": "failed",
  "errorContext": {
    "errorCode": "ERR_SCHEMA_VALIDATION_FAILED",
    "errorReason": "Field violation: 'initialStockLevel' must present an integer integer value greater than or equal to 0. Received format violates bounds.",
    "remediationAction": "Sanitize field inputs inside the presentation boundary before execution."
  }
}
```
