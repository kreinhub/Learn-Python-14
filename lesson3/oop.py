class Product:
    def __init__(self, name, price, stock=0, discount=0, max_discount=20):
        self.name = name.strip()
        if len(self.name) < 2:
            raise ValueError('Product name should have at least 2 symbols')
        self.price = abs(float(price))
        self.stock = abs(int(stock))
        self.discount = abs(float(discount))
        self.max_disount = abs(float(max_discount))
        if self.max_disount > 99:
            raise ValueError('Maximal discount is too big')
        if self.discount > self.max_disount:
            self.discount = self.max_disount
        
    def discounted(self):
        return self.price - (self.price * self.discount / 100)

    def sell(self, items_count=1):
        if items_count > self.stock:
            raise ValueError('Out of stock')
        # Здесь мы можем как-то взаимодействовать с учетной/бухгалтерской системой
        self.stock -= items_count
    
    def get_color(self):
        raise NotImplementedError

    def __repr__(self):
        return f'<Product name: {self.name}, price: {self.price}, stock: {self.stock}>'


class Phone(Product):
    def __init__(self, name, price, color, stock=0, discount=0, max_discount=20):
        super().__init__(name, price, stock, discount, max_discount)
        self.color = color
    
    def get_color(self):
        return f'Body color is {self.color}'

    def get_memory_size(self):
        pass

    def __repr__(self):
        return f'<Phone name: {self.name}, price: {self.price}, stock: {self.stock}>'

class Sofa(Product):
    def __init__(self, name, price, color, texture, stock=0, discount=0, max_discount=20):
        super().__init__(name, price, stock, discount, max_discount)
        self.color = color
        self.texture = texture
    
    def get_color(self):
        return f"The upholstery color: {self.color}, texture type: {self.texture}"        

    def __repr__(self):
        return f'<Phone name: {self.name}, price: {self.price}, stock: {self.stock}>'

my_phone = Phone('iPhone', 60000, 'Black')
# print(my_phone)
# print(my_phone.color)
print(my_phone.get_color())

sofa1 = Sofa('Big sofa', 25312.4, 'Yellow', 'Suede')
# print(sofa1)
# print(sofa1.color)
# print(sofa1.texture)
print(sofa1.get_color())


