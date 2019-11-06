class Account(object):
    ID_COUNT = 1
    def __init__(self, name, **kwargs):
        """docstring for __INIT"""
        self.id = self.ID_COUNT
        self.name = name
        self.__dict__.update(kwargs)
        if hasattr (self, 'value'):
            self.value = 0
        Account.ID_COUNT += 1

    def transfer(self, amount):
        self.value += amount

class Bank(object):
    """The bank"""
    def __init__(self):
        self.account = []
    def add(self, account):
        self.account.append(account)
    def transfer(self, origin, dest, amount):
        """
            @origin: int(id) or str(name) of the first account
            @dest:    int(id) or str(name) of the destination account
            @amount: float(amount) amount to transfer
            @return         True if success, False if an error occured
        """
        # if (check_corrupt(origin)):
        #    fix_account(origin)
        # if (check_corrupt(dest)):
        #    fix_account(dest)
        if (amount > origin.value or amount < 0):
            print("Invalid transfer")
            return False
        origin.value -= amount
        dest.value += amount
        return True
    # def check_corrupt(account):
    #     """docstring for check_corrupt"""
    #     attr = account.dir()
    #     len_attr = len(attr)
    #     if (len_attr % 2 == 0):
    #         return True 
    #     if name not in attr or id not in attr or value not in attr:
    #         return True
    #         corrupt = True
    #     for attribute in attr:
    #         if (attribute.startswith('b')):
    #             return True
    #         if (attribute.startswith('zip')\
    #         or attribute.startswith('addr')):
    #             corrupt = False
    #     return corrupt
            

    def fix_account(self, account):
        """
            fix the corrupted account
            @account: int(id) or str(name) of the account
            @return         True if success, False if an error occured
        """
        return False

