"""
class Product:
    def __init__(self, name, price, discountProc=25):
        self.name = name
        self.price = price
        self.__discountProc = discountProc

    def getDiscount(self):
        return self.__discountProc

    def setDiscount(self, discount):
        if 0.1 <= discount <= 0.75:
            self.__discountProc = discount * 100
        elif 10 <= discount <= 75:
            self.__discountProc = discount
        else:
            print("Incorrect value!")

    def delDiscount(self):
        del self.__discountProc
        print("It is impossible!")

    def show(self):
        print(f"{self.name}, price with discount "
              f"{self.price*(1-self.getDiscount()/100)} grn")
    def toUSD(self, usdEx):
        return self.price * (1-self.getDiscount()/100) / usdEx

    discountProc = property(fget=getDiscount, fset=setDiscount,
                            fdel=delDiscount, doc="discount properly")

item1 = Product("Lipton", 42, 30)
item1.show()

'''
print(item1.discountProc)
item1.discountProc = 0.25
print(item1.discountProc)
item1.discountProc = 99

print(item1.discountProc)

item2 = Product("Apple", 66, 0.4)
item2.show()
print(item2.discountProc)
'''
print(hasattr(item1, "__discountProc"))
del item1.discountProc
print(hasattr(item1, "_Product__discountProc"))
print(hasattr(item1, "__discountProc"))
print(hasattr(item1, "price"))
help(Product.discountProc)
"""
# DECORATORS
class Product:
    def __init__(self, name, price, discountProc=25):
        self.name = name
        self.price = price
        self.__discountProc = discountProc

    @property
    def discountProc(self):
        return self.__discountProc

    @discountProc.setter
    def discountProc(self, discount):
        if 0.1 <= discount <= 0.75:
            self.__discountProc = discount * 100
        elif 10 <= discount <= 75:
            self.__discountProc = discount
        else:
            print("Incorrect value!")

    @discountProc.deleter
    def discountProc(self):
        del self.__discountProc
        print("It is impossible!")

    def show(self):
        print(f"{self.name}, price with discount "
              f"{self.price*(1-self.getDiscount()/100)} grn")
    def toUSD(self, usdEx):
        return self.price * (1-self.getDiscount()/100) / usdEx


class Square:
    def __init__(self, side):
        self.__side = side

    @property
    def side(self):
        return self.__side

    @side.setter
    def side(self, value):
        if value < 0:
            raise ValueError("The lenght must be positive.")
        self.__side = value

    @property
    def area(self):
        return f"area of square = {self.__side ** 2}"

sq = Square(8)
print(sq.area)

class Person:
    def __init__(self, weight, height):
        if weight <= 0:
            raise ValueError("The weight must be positive.")
        self.__weight = weight

        if height <= 0:
            raise ValueError("The height must be positive.")
        if height > 2.5:
            self.__height = height/100
        else:
            self.__height = height

    @property
    def weight(self):
        return self.weight

    @weight.setter
    def weight(self, weight):
        if weight <= 0:
            raise ValueError("The weight must be positive.")
        self.__weight = weight

    @property
    def height(self):
        return self.height

    @height.setter
    def height(self, height):
        if height <= 0:
            raise ValueError("The height must be positive.")
        if height > 2.5:
            self.__height = height/100
        else:
            self.__height = height

    @property
    def bmi(self):
        bmi = self.__weight / (self.__height ** 2)
        return f"BMI = {bmi}."

person = Person(60, 1.8)
print(person.bmi)
