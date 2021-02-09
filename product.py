class Product:
    def __init__(self, name, description, seller, price, availability):
        self.name = name
        self.description = description
        self.price = price
        self.seller = seller
        self.availability = availability
        self.reviews = []
        
    #def available(self):
    #    return self.availability
    
    def __str__(self):
        return f'{self.name} : {self.description} at {self.price} price'
    
        
    