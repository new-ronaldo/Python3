class Horse():
    def __init__(self,name,color,owner):
        self.name = name
        self.color = color
        self.owner = owner

class Rider():
    def __init__(self,name):
        self.name = name

rider = Rider("Джон")
horse = Horse("Кобыла","Черный",rider)
print(horse.owner.name)
