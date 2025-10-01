class Parent:
    def method_a(self):
        print("invoking PARENT method_a!")

class Child(Parent):
    pass

dad = Parent()
son = Child()
  # يطبع: invoking PARENT method_a!
son.method_a()