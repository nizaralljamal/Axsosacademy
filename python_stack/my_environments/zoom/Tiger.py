from Animal import Animal
class Tiger(Animal):
    def __init__(self,name, age, health_level, happiness_level, type):
        super().__init__(name, age, health_level, happiness_level)
        self.type= type
        
    def food(self,type):
        if type == "shawarm":
            print("Shawarm is good for tiger")
            
        else:
            print("Invalid food type for tiger")
        super().food()
        return self
    def display_info(self):
        super().display_info()
        print(f"Type: {self.type}")
        
