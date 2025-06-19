
class Team:
    def __init__(self,name):
        self.name = name
        self.players = []

    def add_player(self,player):
        self.players.append(player.name)

    def __del__(self):
        print(f"{self.name} Team has been Destory")

    def get_player(self):
        print(f"\n ------ {self.name} Team ------ \n")
        for player in self.players:
            print(f"{player} Player")

class Player:
    def __init__(self,name):
        self.name = name

# Test Case
p1 = Player("Muneeb")
p2 = Player("Ablaj")
p3 = Player("Zawyar")

t1 = Team("Circket")
t1.add_player(p1)
t1.add_player(p2)
t1.add_player(p3)
del t1