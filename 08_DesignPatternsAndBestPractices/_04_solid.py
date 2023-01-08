# SRP - keep functions and classes simple i.e. with a single purpose
# ... prefer many classes with dedicated purpose over one (god object antipattern).

# Simple example
# ... before SRP
# class Game:
#     def start_game(self): pass
#     def player_move(self): pass
#     def read_info_from_file(self): pass


# ... after SRP
class Game:
    def start_game(self): pass

class Player:
    def move(self): pass

class FileHandler:
    def read_info_from_file(self): pass


def process():
    # read from file - extract data, compare
    # with open('file.csv', 'w') as f:
    #     pass
    #     pass
    #     pass
    # data = get_data_fromfile()

    # perform data cleaning
    # perform data transformation
    # send data to external service
    # ... requests.post(url, data ... )
    # save to database
    with open('file.csv', 'w') as f:
        pass
        pass
        pass
    # send an emai about processing status (success / failure)


# Another Example

class PaymentTypeException(Exception):
    pass


class StringUtil:
    def reverse_string(self, string):
        return string[::-1]


class CreditCard:
    def __init__(self, name_on_card, exp_date):
        self.name_on_card = name_on_card
        self.exp_date = exp_date


class Order:
    # items = []
    # quantities = []
    # prices = []
    # status = "open"

    def __init__(self):
        self.items = []
        self.quantities = []
        self.prices = []
        self.status = "open"

    def add_item(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)    # 5
        self.prices.append(price)           # 1.99

    def get_total_price(self):
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
        return total

    # Pay() violates SRP, because Order should not handle it's own payments
    # ... just like Order should not handle reverse_string()
    # def pay(self, payment_type, security_code):
    #     if payment_type == "debit":
    #         print("Processing debit payment type")
    #         print(f"Verifying security code: {security_code}")
    #         # ...
    #         self.status = "paid"
    #     elif payment_type == "credit":
    #         print("Processing debit payment type")
    #         print(f"Verifying security code: {security_code}")
    #         # ...
    #         self.status = "paid"
    #     else:
    #         raise PaymentTypeException(f"Unknown payment type {payment_type}")

    # def reverse_string(self, string):
    #     return string[::-1]


class PaymentProcessor:
    def pay_credit(self, order_obj, security_code):
        print("Processing debit payment type")
        print(f"Verifying security code: {security_code}")
        # ...
        order_obj.status = "paid"

    def pay_debit(self, order_obj, security_code):
        print("Processing debit payment type")
        print(f"Verifying security code: {security_code}")
        # ...
        order_obj.status = "paid"

    # def pay_paypal(self, order_obj, security_code):
    #     print("Processing debit payment type")
    #     print(f"Verifying security code: {security_code}")
    #     # ...
    #     order_obj.status = "paid"


# OCP - try to not change existing classes (... and functions) when adding new functionality
# ... let's add a new payment type - Paypal
from abc import ABC, abstractmethod


class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, order_obj, security_code):
        pass


class DebitPaymentProcessor(PaymentProcessor):
    def pay(self, order_obj, security_code):
        print("Processing debit payment type")
        print(f"Verifying security code: {security_code}")
        # ...
        order_obj.status = "paid"


class CreditPaymentProcessor(PaymentProcessor):
    def pay(self, order_obj, security_code):
        print("Processing debit payment type")
        print(f"Verifying security code: {security_code}")
        # ...
        order_obj.status = "paid"


class PaypalPaymentProcessor(PaymentProcessor):
    def pay(self, order_obj, email):
        print("Processing debit payment type")
        print(f"Verifying email: {email}")
        # ...
        order_obj.status = "paid"


# ... other examples
class FileProcessor:
    def process_csv(self): pass
    def process_json(self): pass
    def process_xml(self): pass

class CsvProcessor: pass
class JsonProcessor: pass
class XmlProcessor: pass


# LSP - parent classes should be interchangeable with child classes
# ... add a new payment processor and observe that PaypalPaymentProcessor and CryptoPaymentProcessor
# ... have different pay method than parent class: PaymentProcessor
class CryptoPaymentProcessor(PaymentProcessor):
    def pay(self, order_obj, wallet_id):
        print("Processing debit payment type")
        print(f"Verifying wallet: {wallet_id}")
        # ...
        order_obj.status = "paid"


# ... to solve it, we move the verification logic and encapsulate it into objects
class Verifyer(ABC):
    @abstractmethod
    def verify(self): pass


class PayPalVerifyer(Verifyer):
    def __init__(self, email):
        self.__email = email

    def verify(self):
        print(f'Verifying email: {self.__email}')


class PaymentProcessorEnhanced(ABC):
    @abstractmethod
    def pay(self, order_obj, verification_handler: Verifyer):
        pass


class CreditPaymentProcessorEnhanced(PaymentProcessorEnhanced):
    def pay(self, order_obj, verification_handler):
        print("Processing debit payment type")
        verification_handler.verify()
        # ...
        order_obj.status = "paid"


# ISP - your interfaces should be small
class FileHandler(ABC):
    @abstractmethod
    def write(self): pass

    @abstractmethod
    def read(self): pass

# ... situation: you want to read from one database and write to another.
class FileReadHandler(ABC):
    @abstractmethod
    def read(self): pass

    @abstractmethod
    def read_with_timeout(self): pass

class FileWriteHandler(ABC):
    @abstractmethod
    def write(self): pass

    @abstractmethod
    def append(self): pass




# DIP - your code (your classes) should depend on abstract types, so that you could pass any concrete child type
# class PaymentFlow:
#     def __init__(self, payment_processor: CreditPaymentProcessor, order: Order, verifyer: Verifyer):
#         payment_processor.pay(order, "", verifyer)

class PaymentFlow:
    def __init__(self, payment_processor: PaymentProcessor, order): # payment_type
        # if payment_type == 'debit':
        #     payment_processor.pay_debit()
        payment_processor.pay(order, "")

# ... we can see how well this principle relates to polymorphism
PaymentFlow(PaypalPaymentProcessor(), Order())
PaymentFlow(CreditPaymentProcessor(), Order())


# ... another small example
# ... DIP ties together many concepts: abstraction, inheritance, composition, dependency inversion ... dependency injection (will see latter)
class Address(ABC):
    pass

class ShippingAddress(Address):
    pass

class BillingAddress(Address):
    pass

class Person:
    def __init__(self, age: int, name: str, address: Address):
        self.age = age
        self.name = name
        self.address = address

Person(22, "Jaone", ShippingAddress())
Person(23, "Joana", BillingAddress())



# ... runner code
if __name__ == '__main__':
    order = Order()
    order.add_item("Mouse", 1, 50)
    order.add_item("NMVe", 2, 120)
    order.add_item("Keyboard", 1, 20)

    print(order.get_total_price())
    # order.pay("debit", "0294944")

    PaypalPaymentProcessor().pay(order, "info.something@gmail.com")


    PaymentFlow(CreditPaymentProcessor(), Order())
    PaymentFlow(PaypalPaymentProcessor(), Order())
    PaymentFlow(CreditPaymentProcessor(), Order())