class HttpNotFoundError(Exception):
    """Exception raised for HTTP 404 Not Found errors."""
    
    def __init__(self, message: str):
        super().__init__(self.message)
        self.status_code = 404
        self.name = "NotFound"
        self.message = message