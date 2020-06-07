class Author():
    def __init__(self,name,email,gender):
        self.__name = name
        self.__email=email
        self.__gender=gender
    def getName(self):
        return f'name :{self.__name}'
    def getEmail(self):
        return f'email :{self.__email}'
    def setEmail(self):
        return f'update email: {self.__email}'
    def getGender(self):
        return self.__gender
    def toString(self):
        return f'Author[name={self.__name},email={self.__email},gender={self.__gender}]'

author =Author('Tan Ah Teck','ahTeck@somewhere.com','m')
print(author.toString())

class Book(Author):
    def __init__(self,name,author,price,qty):
        self.__name=name
        self.__author=author
        self.__price=price
        self.__qty=qty

    def getName(self):
        return self.__name
    def getAuthor(self):
        return self.__author
    @property
    def Price(self):
        return self.__price

    @Price.setter
    def Price(self,price):
        self.__price=price
    @property
    def Qty(self):
        return self.__qty
    @Qty.setter
    def Qty(self,qty):
        self.__qty=qty

    def toString(self):
        return f"Book[name={self.__name},Author[name={author.__name},email={author.__email},gender={author.__gender},price={self.__price},qty={self.__qty}]"
book = Book('tan',author,3,4,)
print(book.toString())
