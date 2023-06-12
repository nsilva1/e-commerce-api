from enum import Enum

class Roles(str, Enum):
    admin = "admin"
    support = "support"
    staff = "staff"
    customer = "customer"
    super_admin = "super_admin"

class OrderStatus(str, Enum):
    pending = "pending"
    processing = "processing"
    shipped = "shipped"
    delivered = "delivered"
    cancelled = "cancelled"
    returned = "returned"
    

class PaymentMethod(str, Enum):
    paystack = "paystack"
    flutterwave = "flutterwave"
    interswitch = "interswitch"
    bank_transfer = "bank_transfer"
    cash_on_delivery = "cash_on_delivery"
    bitcoin = "bitcoin"
    ethereum = "ethereum"
    dogecoin = "dogecoin"


class PaymentStatus(str, Enum):
    pending = "pending"
    processing = "processing"
    paid = "paid"
    failed = "failed"
    cancelled = "cancelled"
    refunded = "refunded"


class DeliveryStatus(str, Enum):
    pending = "pending"
    processing = "processing"
    shipped = "shipped"
    delivered = "delivered"
    cancelled = "cancelled"
    returned = "returned"


class DeliveryChannel(str, Enum):
    pickup = "pickup"
    courier = "courier"
    post = "post"
    drone = "drone"


class DeliveryType(str, Enum):
    standard = "standard"
    express = "express"
    same_day = "same_day"
    next_day = "next_day"


class DeliveryProvider(str, Enum):
    dhl = "dhl"
    ups = "ups"
    ni_post = "ni_post"
    net_electronics = "net_electronics"


class AddressType(str, Enum):
    billing = "billing"
    shipping = "shipping"
    both = "both"


class AccessCode(str, Enum):
    admin = "qwerty"
    super_admin = "qwerty123"