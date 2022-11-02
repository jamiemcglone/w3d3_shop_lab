import datetime

class Order:

    def __init__(self, customer_name, quantity, toppings, delivery_address):
        self.customer_name = customer_name
        self.quantity = quantity
        self.toppings = toppings
        self.delivery_address = delivery_address
        self.order_date = datetime.datetime.now().replace(second=0, microsecond=0)



