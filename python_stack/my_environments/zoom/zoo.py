from Tiger import Tiger
from Lion import Lion
from Bear import Bear



class zoo:
    def __init__(self,zoo_name): 
        self.animals = []
        self.name = zoo_name 
    
    
    def add_animal(self,name,age,health_level,happiness_level,unique,animal_type):
    
        if animal_type == "tiger":
            self.animals.append(Tiger(name, age, health_level, happiness_level, unique))
        elif animal_type == "lion":
            self.animals.append(Lion(name, age, health_level, happiness_level, unique))
        elif animal_type == "Bear":
            self.animals.append(Bear(name, age, health_level, happiness_level, unique))
        else:
            print("Invalid animal type")
        
    
    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()