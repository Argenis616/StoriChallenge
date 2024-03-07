import uuid

class Transaction:
    def __init__(self, date, amount, type, user_id):
        self.id = str(uuid.uuid4())
        self.date = date
        self.amount = amount
        self.type = type
        self.user_id = user_id
