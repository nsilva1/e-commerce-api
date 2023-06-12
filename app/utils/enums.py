from enum import Enum

class Roles(str, Enum):
    admin = "admin"
    support = "support"
    staff = "staff"
    customer = "customer"
