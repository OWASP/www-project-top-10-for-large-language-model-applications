import hashlib
import json

class PolicyEngine:
    """
    The Distributor of Truth: Acts as the central authority for the 
    Deterministic Isomorphism Architecture (DIA). 
    Enforces the 'One Law, Two Courts' consensus protocol.
    """
    def __init__(self, canonical_snapshot):
        # The single source of truth for the entire ecosystem
        self.snapshot = canonical_snapshot
        # Cryptographic fingerprint to detect unauthorized snapshot tampering
        self.snapshot_hash = hashlib.sha256(json.dumps(canonical_snapshot, sort_keys=True).encode()).hexdigest()

    def validate_across_engines(self, intent, engine_a, engine_b):
        """
        Consensus Logic: Forces both independent engines to evaluate the 
        exact same snapshot against the agentic intent.
        """
        # Engine A and Engine B must use the central snapshot
        result_a = engine_a.evaluate(intent, self.snapshot)
        result_b = engine_b.evaluate(intent, self.snapshot)
        
        # Consensus Gate
        if result_a == result_b:
            return True, {"consensus": "AbsoluteUnanimity", "snapshot_hash": self.snapshot_hash}
        
        # Fail-Closed behavior if engines diverge
        return False, {"consensus": "DivergenceDetected", "action": "HALT"}
