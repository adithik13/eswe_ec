class InMemoryDB:
    def __init__(self):
        self.main_state = {}  # Committed data
        self.transaction_buffer = None  # Uncommitted changes

    def begin_transaction(self):
        if self.transaction_buffer is not None:
            raise Exception("Transaction already in progress.")
        self.transaction_buffer = {}

    def put(self, key, value):
        if self.transaction_buffer is None:
            raise Exception("No active transaction.")
        self.transaction_buffer[key] = value

    def get(self, key):
        if self.transaction_buffer is None:  # No active transaction
            return self.main_state.get(key)
        return self.main_state.get(key)  # Ignore transaction buffer

    def commit(self):
        if self.transaction_buffer is None:
            raise Exception("No active transaction to commit.")
        self.main_state.update(self.transaction_buffer)
        self.transaction_buffer = None

    def rollback(self):
        if self.transaction_buffer is None:
            raise Exception("No active transaction to rollback.")
        self.transaction_buffer = None
