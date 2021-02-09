''' A high level framewrok for an online shopping'''

from product import Product
from review import Review

class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        
        self.reviews = []
    
    def buy_product(self, product): 
        if product.availability:
            print(f'{self} is buying {product}.')
            product.availability = False
        else:
            print(f'{product} is no longer available.')
    
    def sell_product(self, name, description, price):
        product = Product(name, description, self, price, availability=True)
        print(f'{product} is on the market.')
        return product
                                            
    def write_review(self, content, product):
        review =  Review(content, self, product)
        self.reviews.append(review)
        product.reviews.append(review)
        return review
    
    def __str__(self):
        return f'user: {self.name}'


if __name__ == '__main__':
    brianna = User(1, 'Brianna')
    mary = User(2, 'Mary')

    keyboard = brianna.sell_product('Keyboard', 'A nice mechanical keyboard', 100)
    print(keyboard.availability)  # => True
    mary.buy_product(keyboard)
    print(keyboard.availability)  # => False
    mk_review = mary.write_review('This is the best keyboard ever!', keyboard)
    print(mk_review)
    print(mk_review in mary.reviews)
    print(mk_review in keyboard.reviews)  # => True        