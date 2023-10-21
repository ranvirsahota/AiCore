class Player():
    def __init__(self, name, level):
        self.name = name
        self.level = level
    
    def introduce(self):
        print(f'I am {self.name} and I\'m level {self.level}')
    
    # this first paramenter self referes to instance of class
    # In other programming languages it's called this
    def play(this_instance_of_the_class):
        this_instance_of_the_class.level += 1


player = Player('Ranvir', 100)
player.introduce()
player.play()
print('name: ', player.name)
print('level: ', player.level)

player_2 = Player('Tamin', 101)
player_3 = Player('Kiki', 300)
player_3.play()