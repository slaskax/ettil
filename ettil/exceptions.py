'''Various exceptions that ettil can raise.'''

class WriteError(Exception):
    '''Raised when an error is returned from the server when writing.'''

    def __init__(self, cause, message):
        self.cause = cause
        self.message = message
        super().__init__(message)

class ConflictError(WriteError):
    '''Raised when an edit conflict occurs when trying to write.'''

    def __init__(self):
        super().__init__(
            'conflict',
            'This page has been edited since you last read its content.'
        )

class UnmodifiedError(WriteError):
    '''
    Raised when the page contents have not been modified since last edit.

    ETT will refuse to update a page if the new content is the old, so this is
    here you can deal with those cases. For example, to ignore it:
        try:
            ettil.write("example", "test")
        except UnmodifiedError:
            pass
    '''

    def __init__(self):
        super().__init__(
            'unmodified',
            'The page was not saved due to no changes being made.'
        )
