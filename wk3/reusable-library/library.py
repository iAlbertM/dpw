class Item(object):
    def __init__(self):
        self.__name = self.request.GET['item_name']
        self.__original_price = 0.00
        self.__discount = 0
        self.__qty = 1
        self.get_discount_amount()
        self.get_discount_price()
        self.get_discount_savings()
        self.discount_amount = 0
        self.discount_price = 0
        self.savings = 0

    @property
    def name(self):
        return self.__name

    @property
    def original_price(self):
        return self.__original_price

    @property
    def discount(self):
        return self.__discount

    @property
    def qty(self):
        return self.__qty

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @original_price.setter
    def original_price(self, new_original_price):
        self.__original_price = new_original_price

    @discount.setter
    def discount(self, new_discount):
        self.__discount = new_discount

    @qty.setter
    def qty(self, new_qty):
        self.__qty = new_qty

    def get_discount_amount(self):
        self.__discount_amount = ((self.discount / 100) * self.original_price)
        return self.__discount_amount

    def get_discount_price(self):
        self.__discount_price = self.__original_price - self.__discount_amount
        return self.__discount_price

    def get_discount_savings(self):
        self.__savings = self.__original_price  - self.__discount_price
        return self.__savings

