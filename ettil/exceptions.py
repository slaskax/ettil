class ConflictError(Exception):
    def __init__(self):
        super().__init__(
            "This page has been edited since you last read its content."
        )
