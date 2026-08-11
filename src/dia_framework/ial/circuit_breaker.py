import logging

logger = logging.getLogger("DIA_CircuitBreaker")

class CircuitBreaker:
    @staticmethod
    def trip(reason):
        logger.error(f"HALT: Execution suspended due to: {reason}")
        return {
            "status": "HALT",
            "message": "Policy violation detected.",
            "enforcement": "FailClosed"
        }
