import json
import os

#  THE ARCHITECTURAL COMPLIANCE CONTRACT (Directly maps to API_REFERENCE.md)
def validate_ims_payload(data):
    """
    Programmatic schema parser checking data boundaries.
    Ensures structural data integrity across system endpoints.
    """
    # 1. Verify existence of primary high-level payload structures
    if "requestMetadata" not in data or "productDetails" not in data:
        raise ValueError("Missing critical primary root objects: 'requestMetadata' or 'productDetails'.")
    
    # 2. Assert structural metrics inside metadata keys
    meta = data["requestMetadata"]
    required_meta = ["originatingSystem", "operatorId", "transactionTimestamp"]
    for key in required_meta:
        if key not in meta:
            raise ValueError(f"Metadata Integrity Breach: Missing key '{key}'.")
            
    if not isinstance(meta["operatorId"], int):
        raise TypeError(f"Type Boundary Error: 'operatorId' must be an Integer. Got {type(meta['operatorId']).__name__}.")

    # 3. Assert structural constraints inside product details keys
    prod = data["productDetails"]
    required_prod = ["skuCode", "itemName", "category", "initialStockLevel", "supplierList"]
    for key in required_prod:
        if key not in prod:
            raise ValueError(f"Product Specification Breach: Missing key '{key}'.")

    if not isinstance(prod["initialStockLevel"], int):
        raise TypeError(f"Type Boundary Error: 'initialStockLevel' must be an Integer.")
        
    if prod["initialStockLevel"] < 0:
        raise ValueError(f"Value Boundary Violation: 'initialStockLevel' cannot be negative. Value checked: {prod['initialStockLevel']}.")

    if not isinstance(prod["supplierList"], list) or len(prod["supplierList"]) == 0:
        raise ValueError("Array Structure Exception: 'supplierList' must be a populated array.")

    return True

def run_test_suite(test_id, scenario_description, raw_json_string):
    print(f"\n [EXECUTION LOG: {test_id}] {scenario_description}")
    try:
        # Step A: String Parsing (Simulating incoming API data pipeline)
        parsed_json = json.loads(raw_json_string)
        
        # Step B: Schema Integrity Check (Simulating interface contract verification)
        validate_ims_payload(parsed_json)
        print(f"  ✔ STATUS: 200 OK. Schema validation successful.")
        print(f"  ✔ SYSTEM METRIC: Verified Product SKU Target -> {parsed_json['productDetails']['skuCode']}")
        
    except json.JSONDecodeError as e:
        print(f"  HTTP 400 Bad Request: Hard Syntax Parse Defect.")
        print(f"     Diagnostic Log: {str(e)}")
    except (ValueError, TypeError) as e:
        print(f"  HTTP 422 Unprocessable Entity: Data Boundary Breach.")
        print(f"     Diagnostic Log: {str(e)}")

if __name__ == "__main__":
    print("======================================================================")
    print("INITIALIZING RUNTIME AUTOMATED INTERFACE VERIFICATION ENGINE       ")
    print("======================================================================")

    # TEST CASE 1: Perfect Production Payload (Happy Path Mapping)
    # Exactly mirrors the success schema documented in your API_REFERENCE.md
    tc_001_payload = """{
      "requestMetadata": {
        "originatingSystem": "Warehouse-Streamlit-UI",
        "operatorId": 4092,
        "transactionTimestamp": "2026-10-01T13:00:00Z"
      },
      "productDetails": {
        "skuCode": "SAM-MIL-998A",
        "itemName": "Tactical Logistical Housing Unit",
        "category": "Storage Infrastructure",
        "initialStockLevel": 150,
        "supplierList": ["Kolkata Logistics Corp", "Delhi Supply Networks"],
        "secondaryNotes": null
      }
    }"""
    run_test_suite("TC-IMS-VAL-001", "Verifying Standard Successful API Registration Request", tc_001_payload)

    # TEST CASE 2: Logical Boundary Breach (Negative Input Injection)
    # Proves the automated tester catches numeric errors documented in QA_TEST_PLANS.md
    tc_002_payload = """{
      "requestMetadata": {
        "originatingSystem": "Warehouse-Streamlit-UI",
        "operatorId": 4092,
        "transactionTimestamp": "2026-10-01T13:00:00Z"
      },
      "productDetails": {
        "skuCode": "SAM-MIL-998A",
        "itemName": "Tactical Logistical Housing Unit",
        "category": "Storage Infrastructure",
        "initialStockLevel": -75,
        "supplierList": ["Kolkata Logistics Corp"],
        "secondaryNotes": null
      }
    }"""
    run_test_suite("TC-IMS-ERR-002", "Injecting Boundary Deviation Exception (Negative Stock Value)", tc_002_payload)

    # TEST CASE 3: Hard Formatting Break (Syntax Trailing Comma Defect)
    # Proves your core project engine detects syntax syntax breaks instantly
    tc_003_payload = """{
      "requestMetadata": {
        "originatingSystem": "Warehouse-Streamlit-UI",
        "operatorId": 4092,
        "transactionTimestamp": "2026-10-01T13:00:00Z"
      },
      "productDetails": {
        "skuCode": "SAM-MIL-998A",
        "initialStockLevel": 150,
      }
    }"""
    run_test_suite("TC-IMS-ERR-003", "Injecting Invalid Trailing Comma Parse Exception", tc_003_payload)

    print("\n======================================================================")
    print("AUTOMATED INTERFACE COMPLIANCE CHECK MATRIX OPERATIONS COMPLETE    ")
    print("======================================================================")
