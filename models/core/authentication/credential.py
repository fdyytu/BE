class Credential:
    """User credentials."""
    def __init__(self, username, password_hash):
        self.username = username
        self.password_hash = password_hash