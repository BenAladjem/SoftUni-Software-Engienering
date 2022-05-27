class BankAccount:
    def __init__(self, name):
        self.name = name
        self.__number_of_card = 12345
        self.exp_date = '2020'
        self.cvv = 569



class ExtendedBankAccount(BankAccount):
    def __init__(self, name, percent_discount):
        super(ExtendedBankAccount, self).__init__(name)
        self.discount = percent_discount



my_account = BankAccount("Ben")
print(my_account._BankAccount__number_of_card)

