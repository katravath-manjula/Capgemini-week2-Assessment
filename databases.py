# Define an abstract class `IDatabaseOperations` with methods `insert()`, `update()`, and `delete()`. Implement this in `SQLDatabase` and `NoSQLDatabase`.
from abc import ABC, abstractmethod

class IDatabaseOperations(ABC):
    @abstractmethod
    def insert(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def delete(self):
        pass

class SQLDatabase(IDatabaseOperations):
    def __init__(self, data):  
        self.data = data

    def insert(self):
        print(f"SQL Database: Data '{self.data}' has been inserted.")

    def update(self):
        print(f"SQL Database: Data '{self.data}' has been updated.")

    def delete(self):
        print(f"SQL Database: Data '{self.data}' has been deleted.")

class NoSQLDatabase(IDatabaseOperations):
    def __init__(self, data):  
        self.data = data

    def insert(self):
        print(f"NoSQL Database: Data '{self.data}' has been inserted.")

    def update(self):
        print(f"NoSQL Database: Data '{self.data}' has been updated.")

    def delete(self):
        print(f"NoSQL Database: Data '{self.data}' has been deleted.")

print("Testing NoSQL Database:")
nosql_db = NoSQLDatabase("user data")
nosql_db.insert()
nosql_db.delete()
nosql_db.update()

print("\nTesting SQL Database:")
sql_db = SQLDatabase("customer records")
sql_db.insert()
sql_db.delete()
sql_db.update()
