import json
import os

#  THE SYSTEM COMPLIANCE REGISTRY (The Automated Judge Matrix)
class AutomatedComplianceJudge:
    def __init__(self, target_schema_path="API_REFERENCE.md"):
        self.target_schema_path = target_schema_path
        print(f"[INIT] AI Compliance Judge deployed against contract rulebook: {target_schema_path}")

    def evaluate_payload_structure(self, raw_data_stream):
        """
        Simulates an automated verification loop processing unstructured incoming payloads.
        Performs data type isolation and syntax boundary compliance monitoring.
        """
        print("\n⚡ [EVENT DETECTED] Incoming stream received. Activating validation filters...")
        
        try:
            # 1. Simulate Event Extraction
            payload = json.loads(raw_data_stream)
            print("   [STAGE 1] Hard syntax parsing verified. Data contract structural integrity intact.")
            
            # 2. Assert Business Boundary Logic 
            product_data = payload.get("productDetails", {})
            stock_level = product_data.get("initialStockLevel")
            
            if stock_level is None:
                return {"status": "REJECTED", "code": 422, "reason": "Missing critical stock metric."}
            
            if stock_level < 0:
                # Automated structural rollback trigger emulation
                return {
                    "status": "REJECTED", 
                    "code": 422, 
                    "reason": f"Logic Boundary Violation: Negative inventory metric detected ({stock_level}). Enforcing rule criteria from QA_TEST_PLANS.md."
                }
            
            # 3. Simulate Event-Driven Action Execution
            print("   [STAGE 2] Logic boundaries cleared. Initializing automatic database write pipeline...")
            return {"status": "APPROVED", "code": 200, "sku_target": product_data.get("skuCode")}
            
        except json.JSONDecodeError as e:
            return {"status": "CRASHED", "code": 400, "reason": f"Syntax Parse Defect: {str(e)}"}

if __name__ == "__main__":
    print("======================================================================")
    print(" STARTING AUTOMATED PIPELINE GOVERNANCE & EVENT TEST SYSTEM        ")
    print("======================================================================")

    # Instantiate our local system testing monitor engine
    judge = AutomatedComplianceJudge()

    # TEST SCENARIO A: Evaluating a non-compliant log submission (Negative bounds)
    bad_stream = '{"requestMetadata": {"operatorId": 4092}, "productDetails": {"skuCode": "SAM-MIL-998A", "initialStockLevel": -25}}'
    evaluation_a = judge.evaluate_payload_structure(bad_stream)
    print(f"  JUDGE DECISION: Status -> {evaluation_a['status']} | Code -> {evaluation_a['code']}")
    print(f"     Diagnostic Logs -> {evaluation_a['reason']}")

    # TEST SCENARIO B: Evaluating a perfectly compliant production transaction event
    good_stream = '{"requestMetadata": {"operatorId": 4092}, "productDetails": {"skuCode": "SAM-MIL-998A", "initialStockLevel": 500}}'
    evaluation_b = judge.evaluate_payload_structure(good_stream)
    print(f"   JUDGE DECISION: Status -> {evaluation_b['status']} | Code -> {evaluation_b['code']}")
    print(f"   Action Trigger  -> Automated synchronization successful for resource: {evaluation_b['sku_target']}")

    print("\n======================================================================")
    print("COMPLIANCE PIPELINE SYSTEM EVALUATION OPERATIONS MATRIX COMPLETE   ")
    print("======================================================================")
