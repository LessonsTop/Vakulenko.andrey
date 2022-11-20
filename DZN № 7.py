class Enemy(Person):
    pass

class Game:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def start_game(self):
        while True:
            if self.player.health <= 0:
                print('enemy win!')
                break
            elif self.enemy.health <= 0:
                print('player win!')
                break
            self.player.attack(self.enemy)
            self.enemy.attack(self.player)

enemy = Enemy(100, 30, 100)
player = Player(100, 35, 100)

game_1 = Game(enemy, player)
game_1.start_game()