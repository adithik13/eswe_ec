from transaction import InMemoryDB

# Initialize the in-memory database
inmemoryDB = InMemoryDB()

# Should return None, because "A" doesn’t exist in the DB yet
print(inmemoryDB.get("A"))  # Output: None

# Should throw an error because a transaction is not in progress
try:
    inmemoryDB.put("A", 5)
except Exception as e:
    print(e)  # Output: No active transaction.

# Starts a new transaction
inmemoryDB.begin_transaction()

# Sets value of "A" to 5, but it's not committed yet
inmemoryDB.put("A", 5)

# Should return None, because updates to "A" are not committed yet
print(inmemoryDB.get("A"))  # Output: None

# Update "A"'s value to 6 within the transaction
inmemoryDB.put("A", 6)

# Commits the open transaction
inmemoryDB.commit()

# Should return 6, that was the last value of "A" to be committed
print(inmemoryDB.get("A"))  # Output: 6

# Throws an error, because there is no open transaction
try:
    inmemoryDB.commit()
except Exception as e:
    print(e)  # Output: No active transaction to commit.

# Throws an error because there is no ongoing transaction
try:
    inmemoryDB.rollback()
except Exception as e:
    print(e)  # Output: No active transaction to rollback.

# Should return None because "B" does not exist in the database
print(inmemoryDB.get("B"))  # Output: None

# Starts a new transaction
inmemoryDB.begin_transaction()

# Set key "B"'s value to 10 within the transaction
inmemoryDB.put("B", 10)

# Rollback the transaction - revert any changes made to "B"
inmemoryDB.rollback()

# Should return None because changes to "B" were rolled back
print(inmemoryDB.get("B"))  # Output: None
