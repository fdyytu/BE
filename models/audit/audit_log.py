class AuditLog:
    """Audit log for recording activities."""

    def __init__(self, action: str, user_id: int, timestamp: str):
        self.action = action
        self.user_id = user_id
        self.timestamp = timestamp