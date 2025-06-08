class TwoFactor:
    """2FA implementation."""
    def __init__(self, user_id, enabled=False):
        self.user_id = user_id
        self.enabled = enabled