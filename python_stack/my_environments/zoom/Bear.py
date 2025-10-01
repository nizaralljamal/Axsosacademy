from Animal import Animal
class Bear(Animal):
    def __init__(self,name, age, health_level, happiness_level, tall):
        super().__init__(name, age, health_level, happiness_level)
        self.tall = tall
    
    def food(self,type):

        if type == "banana":
            print("Banana is good for bear")
        else:
            print("Invalid food type")
        super().food()
        return self
    
    def display_info(self):
        super().display_info()
        print(f"Tall: {self.tall}")
