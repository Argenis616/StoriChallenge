import uuid

class User:
    def __init__(self, first_name, last_name, email, mobile_phone):
        self.id = str(uuid.uuid4()) 
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.mobile_phone = mobile_phone