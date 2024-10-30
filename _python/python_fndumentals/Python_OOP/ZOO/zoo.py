from Lion import Lion
from Eagle import Eagle

class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name
    def add_lion(self,name):
        self.animals.append( name)
    def add_eagle(self, name):
        self.animals.append( name )
    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()
zoo1 = Zoo("Ali's Zoo")
simba = Lion("Simba", 32, 40, 22, 94)
eagle_one = Eagle("Eagle One", 3, 70, 85, "Advanced")
zoo2 = Zoo("Jon's Zoo")
Rajah = Lion("Rajah",22,33,22,90)

zoo1.add_lion(simba)
simba = Lion("Simba", 32, 40, 22, 94)
eagle_one = Eagle("Eagle One", 3, 70, 85, "Advanced")

zoo1.add_eagle(eagle_one)
zoo1.print_all_info()
zoo2.add_lion(Rajah)
zoo2.print_all_info()