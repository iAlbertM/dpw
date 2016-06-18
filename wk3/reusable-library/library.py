from __future__ import division


# creating an Item class
class SaleItem(object):
    # initializing the Item class
    def __init__(self, item, price, discount, qty):
        self.item = item
        self.price = price
        self.discount = discount
        self.qty = qty
        self.discount_amount = 0
        self.discount_price = 0.00
        self.discount_saving = 0.00

    def get_discount_amount(self, discount):
        self.discount_amount = (discount / 100 ) * self.price
        return self.discount_amount
    
    def get_discount_price(self):
        self.discount_price = self.price - self.discount_amount
        return self.discount_price
    
    def get_discount_saving(self):
        self.discount_saving = self.price - self.discount_price
        return self.discount_saving
