from Animal import Animal
class Lion(Animal):
    def __init__(self,name, age, health_level, happiness_level, weight):
        super().__init__(name, age, health_level, happiness_level)
        self.weight = weight
    
    
    def food(self,type):
        if type == "flafel":
            print("Flafel is good for lion")
            
        else:
            print("Invalid food type for lion")
        super().food()
        return self

    def display_info(self):
        super().display_info()
        print(f"Weight: {self.weight}")