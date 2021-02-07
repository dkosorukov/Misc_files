class Customer:
    def __init__(self, first_name, last_name, tier=('free', 0)):
        self.first_name = first_name
        self.last_name = last_name
        self._tier = tier[0]
        self._cost = tier[1]
           
    def can_access(self, content):
        return content['tier'] == 'free' or content['tier'] == self._tier
    
    # return billion for gien number of months
    def bill_for(self, num_months):
        return self._cost * num_months
    
    # factory method to create premium customer
    @classmethod
    def premium(cls, first_name, last_name):
        return cls(first_name, last_name, tier=('premium', 10))

    # property function to retrun a customer full name 
    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"
        


if __name__ == '__main__':
       
    marco = Customer('Marco', 'Polo')  # Defaults to the free tier
    print(marco.name)  # Marco Polo
    print(marco.can_access({'tier': 'free', 'title': '1812 Overture'}))  # True
    print(marco.can_access({'tier': 'premium', 'title': 'William Tell Overture'}))  # False

    victoria = Customer.premium("Alexandrina", "Victoria")  # Build a customer around the ('premium', 10$/mo) streaming plan.
    print(victoria.can_access({'tier': 'free', 'title': '1812 Overture'}))  # True
    print(victoria.can_access({'tier': 'premium', 'title': 'William Tell Overture'}))  # True
    print(victoria.bill_for(5))  # => 50 (5 months at 10$/mo)
    print(victoria.name)  # Alexandrina Victoria