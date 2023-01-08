# Fluent interface (method chaining)
class Calcultor:
    def __init__(self):
        self.number1 = 0

    def add(self, number):
        self.number1 = number
        return self

    def subtract(self, number):
        self.number1 = number
        return self

    def to(self, number):
        self.number1 += number
        return self

    def from_(self, number):
        self.number1 -= number
        return self

    def get_result(self):
        return self.number1


# calculator.add(5)
# calculator.get_result()

print(Calcultor().add(5).to(6).get_result())
# print(Calcultor().subtract(5).from_(6).get_result()) # incorrect result, can you fix it?

# other examples
# expect(var1).to_be().be_less_than(var2).by(7)