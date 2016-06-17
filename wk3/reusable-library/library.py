class Item(object):  # creating an Item class
    def __init__(self):  # initializing the Item class
        # creating the Item class object with some default attributes and methods and default values
        self.__item_name = ''
        self.__original_price = 0
        self.__discount = 0
        self.__qty = 0
        self.__discount_amount = 0
        self.__discount_price = 0
        self.__discount_saving = 0
        self.get_discount_amount()
        self.get_discount_price()
        self.get_discount_saving()

    @property
    def item_name(self):
        return self.__item_name

    @property
    def original_price(self):
        return self.__original_price

    @property
    def discount(self):
        return self.__discount

    @property
    def qty(self):
        return self.__qty

    @property
    def discount_amount(self):
        return self.__discount_amount

    @property
    def discount_price(self):
        return self.__discount_price

    @property
    def discount_saving(self):
        return self.__discount_saving

    @item_name.setter
    def item_name(self, new_item_name):
        self.__item_name = new_item_name

    @original_price.setter
    def original_price(self, new_original_price):
        self.__original_price = new_original_price

    @discount.setter
    def discount(self, new_discount):
        self.__discount = new_discount

    @qty.setter
    def qty(self, new_qty):
        self.__qty = new_qty

    @discount_amount.setter
    def discount_amount(self, new_discount_amount):
        self.__discount_amount = new_discount_amount

    @discount_price.setter
    def discount_price(self, new_discount_price):
        self.__discount_price = new_discount_price

    @discount_saving.setter
    def discount_saving(self, new_discount_saving):
        self.__discount_saving = new_discount_saving

    def get_discount_amount(self):
        self.__discount_amount = ((self.discount / 100) *
                                self.original_price)
        return self.__discount_amount

    def get_discount_price(self):
        self.__discount_price = self.original_price -\
                              self.discount_amount
        return self.__discount_price

    def get_discount_saving(self):
        self.__discount_saving = self.original_price  -\
                       self.discount_price
        return self.__discount_saving

