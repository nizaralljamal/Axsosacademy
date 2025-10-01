from zoo import zoo


ibrahem_zoo = zoo("ibrahem_zoo")
ibrahem_zoo.add_animal("Tiger", 10, 100, 100, "unique", "tiger")
ibrahem_zoo.add_animal("Lion", 10, 100, 100, "unique", "lion")
ibrahem_zoo.add_animal("Bear", 10, 100, 100, "unique", "Bear")
ibrahem_zoo.print_all_info()   

ibrahem_zoo.animals[0].food("shawarm")
print()
ibrahem_zoo.animals[1].food("meat")
print()
ibrahem_zoo.animals[2].food("fish")

ibrahem_zoo.print_all_info()
    
