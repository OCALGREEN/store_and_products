
class Store:
    def __init__(self, name, list_of_products):
        self.name = name
        self.list_of_products = list_of_products

    def add_product(self, new_product):
        return self.list_of_products.append(new_product)


















class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price 
        self.category = category 

    def update_price(self, percent_change, is_increased):
        if is_increased == True:
            return self.price + (self.price * percent_change)
        else:
            return self.price - (self.price * percent_change)

    def print_info(self):
        return print(f"Product Name: {self.name} Product Category: {self.category} Product Price: {self.price}")
