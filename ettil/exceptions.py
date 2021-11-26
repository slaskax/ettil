class WriteError(Exception):
    def __init__(self, cause, message):
        self.cause = cause
        self.message = message
        super().__init__(message)

class ConflictError(WriteError):
    def __init__(self):
        super().__init__(
            'conflict',
            'This page has been edited since you last read its content.'
        )
