from __future__ import division


# an item class designed to have its pricing details calculated
class SaleItem(object):
    """ Data class object """
    # initializing the Item class
    def __init__(self):
        #  data attributes that help distinguish this object from any other
        self.__item = ''
        self.__price = 0
        self.__discount = 0
        self.__qty = 0
        #  attributes that run behind-the-scenes
        self.__discount_decimal = 0
        self.__discount_amount = 0
        self.__discount_price = 0
        self.__discount_qty = 0

    @property
    def item(self):
        return self.__item

    @item.setter
    def item(self, new_item):
        self.__item = new_item

    @property
    def price(self):
        ''' getter '''
        return self.__price

    @price.setter
    def price(self, new_price):
        self.__price = new_price

    @property
    def discount(self):
        ''' getter '''
        return self.__discount

    @discount.setter
    def discount(self, new_discount):
        self.__discount = new_discount

    @property
    def qty(self):
        ''' getter '''
        return self.__qty

    @qty.setter
    def qty(self, new_qty):
        self.__qty= new_qty

    @property
    def discount_decimal(self):
        ''' getter '''
        return self.__discount_decimal

    @discount_decimal.setter
    def discount_decimal(self, new_discount_decimal):
        self.__discount_decimal = new_discount_decimal

    @property
    def discount_amount(self):
        ''' getter '''
        return self.__discount_amount

    @discount_amount.setter
    def discount_amount(self, new_discount_amount):
        self.__discount_amount = new_discount_amount

    @property
    def discount_price(self):
        ''' getter '''
        return self.__discount_price

    @discount_price.setter
    def discount_price(self, new_discount_price):
        self.__discount_price = new_discount_price

    @property
    def discount_qty(self):
        ''' getter '''
        return self.__discount_qty

    @discount_qty.setter
    def discount_qty(self, new_discount_qty):
        self.__discount_qty = new_discount_qty

class PriceChecker(SaleItem):
    """ utility functions to determine the final price of a discounted item """
    def get_discount_decimal(self, x):
        """ method: convert percentage to its float equiv. """
        self.discount_decimal = float(x) / float(100)
        return float(self.discount_decimal)

    def get_discount_amount(self, x, y):
        """ method: find amount that will be discounted from the item's price """
        self.discount_amount = float(x) * float(y)
        return float(self.discount_amount)

    def get_discount_price(self):
        """ method: find the new price with discount applied """
        return float(self.price) - float(self.discount_amount)

    def get_discount_qty(self):
        """ get the price for a select number of an item """
        return float(self.discount_price) * float(self.qty)
