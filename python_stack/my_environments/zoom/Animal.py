class Animal:
    def __init__(self, name, age, health_level, happiness_level):
        self.name = name
        self.age = age
        self.health = health_level
        self.happiness = happiness_level
        
    
    def food(self):
        self.health += 10
        self.happiness += 10    
        if self.health > 100:
            print("Health is full")
        else:
            print("Health is not full")
            
        if self.happiness > 100:
            print("Happiness is happy")
        else:
            print("Happiness is not happy")
            
            
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Health: {self.health}")
        print(f"Happiness: {self.happiness}")