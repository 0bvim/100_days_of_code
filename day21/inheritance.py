class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale")


class Fish(Animal):
    def __init__(self):
        super().__init__()
    
    def breathe(self):
        super().breath()
        print("doing this undewater")

    def swim(self):
        print("moving in water.")

nemo = Fish()
nemo.swim()
nemo.breath()
