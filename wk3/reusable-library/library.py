from __future__ import division


# an item class designed to have its pricing details calculated
class SaleItem(object):
    # initializing the Item class
    def __init__(self, item, price, discount, qty):
        self.item = item
        self.price = price
        self.discount = discount
        self.qty = qty
        self.discount_amount = 0
        self.discount_price = 0
        self.discount_saving = 0


class PriceChecker(SaleItem):
    # utility functions to determine the final price of a discounted item

    def get_discount_amount(self):
        """ method: find amount that will be discounted from the item's price """
        self.discount_amount = (self.discount / 100) * self.price
        return self.discount_amount

    def get_discount_price(self):
        """ method: find the new price with discount applied """
        self.discount_price = self.price - self.discount_amount
        return self.discount_price

    def get_price_qty(self):
        """ get the price for a select number of itemsslam """