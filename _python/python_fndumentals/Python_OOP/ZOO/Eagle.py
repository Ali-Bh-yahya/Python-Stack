from Animal import Animal

class Eagle(Animal):
    def __init__(self, name, age, health, happiness, fly_skills):
        super().__init__(name, age, health, happiness)
        self.fly_skills = fly_skills

    def display_info(self):
        print(f"name: {self.name} age: {self.age} health: {self.health} happiness: {self.happiness} fly_skills: {self.fly_skills}")

# eagle = Eagle("first_eagle", 32, 40, 22, "so professional")
# eagle.display_info()