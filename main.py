def on_button_pressed_a():
    Player.change(LedSpriteProperty.X, -1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global Bullet, Enemy, Player
    Bullet = game.create_sprite(Player.get(LedSpriteProperty.X), 3)
    basic.pause(250)
    for index in range(5):
        if Bullet.is_touching(Enemy):
            Enemy.delete()
            game.add_score(1)
            Enemy = game.create_sprite(0, 0)
            Player.delete()
            Bullet.delete()
            Bullet_from_enemy.delete()
            Player = game.create_sprite(2, 4)
        elif Bullet.is_touching(Bullet_from_enemy):
            Bullet_from_enemy.delete()
            Bullet.delete()
        else:
            Bullet.change(LedSpriteProperty.Y, -1)
            basic.pause(250)
    Bullet.delete()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    Player.change(LedSpriteProperty.X, 1)
input.on_button_pressed(Button.B, on_button_pressed_b)

Enemy_fever_3: game.LedSprite = None
Enemy_fever_2: game.LedSprite = None
Enemy_fever_1: game.LedSprite = None
Enemy_fever = 0
Enemy_speed = 0
sprite = 0
Bullet_from_enemy: game.LedSprite = None
Bullet: game.LedSprite = None
Enemy: game.LedSprite = None
Player: game.LedSprite = None
Player = game.create_sprite(2, 4)
Enemy = game.create_sprite(0, 0)

def on_forever():
    global sprite, Enemy_speed, Bullet_from_enemy, Enemy_fever, Enemy_fever_1, Enemy_fever_2, Enemy_fever_3, Player, Enemy
    for index2 in range(4):
        sprite = randint(0, 1)
        if sprite == 0:
            Enemy.change(LedSpriteProperty.X, 1)
            Enemy_speed = randint(0, 2)
            if Enemy_speed == 0:
                basic.pause(100)
            elif Enemy_speed == 1:
                basic.pause(250)
            else:
                basic.pause(500)
        else:
            Bullet_from_enemy = game.create_sprite(Enemy.get(LedSpriteProperty.X), 1)
            basic.pause(500)
            Enemy.change(LedSpriteProperty.X, 1)
            for index3 in range(4):
                Bullet_from_enemy.change(LedSpriteProperty.Y, 1)
                basic.pause(250)
                if Bullet_from_enemy.is_touching(Player):
                    game.game_over()
            Bullet_from_enemy.delete()
        if game.score() == 1:
            basic.show_string("Enemy fever is started")
            Enemy_fever = 3
            Enemy_fever_1 = game.create_sprite(2, 2)
            Enemy_fever_2 = game.create_sprite(1, 2)
            Enemy_fever_3 = game.create_sprite(0, 2)
            for index4 in range(2):
                Enemy_fever_1.change(LedSpriteProperty.Y, 1)
            for index5 in range(2):
                Enemy_fever_1.change(LedSpriteProperty.Y, -1)
            while Bullet.is_touching(Enemy_fever_3):
                Enemy_fever_3.delete()
                Enemy_fever += -1
                game.add_score(3)
            while Bullet.is_touching(Enemy_fever_2):
                Enemy_fever_2.delete()
                Enemy_fever += -1
                game.add_score(3)
            while Bullet.is_touching(Enemy_fever_1):
                Enemy_fever_1.delete()
                Enemy_fever += -1
                game.add_score(3)
            while Enemy_fever_1.is_touching(Player):
                game.game_over()
            while Enemy_fever == 0:
                basic.show_string("Enemy fever is ended")
                Enemy.delete()
                Bullet.delete()
                Player.delete()
                Bullet_from_enemy.delete()
                Player = game.create_sprite(2, 4)
                Enemy = game.create_sprite(0, 0)
    for index6 in range(4):
        sprite = randint(0, 1)
        if sprite == 0:
            Enemy.change(LedSpriteProperty.X, -1)
            Enemy_speed = randint(0, 2)
            if Enemy_speed == 0:
                basic.pause(100)
            elif Enemy_speed == 1:
                basic.pause(250)
            else:
                basic.pause(500)
        else:
            Bullet_from_enemy = game.create_sprite(Enemy.get(LedSpriteProperty.X), 1)
            basic.pause(500)
            Enemy.change(LedSpriteProperty.X, -1)
            for index7 in range(4):
                Bullet_from_enemy.change(LedSpriteProperty.Y, 1)
                basic.pause(250)
                if Bullet_from_enemy.is_touching(Player):
                    game.game_over()
            Bullet_from_enemy.delete()
        if game.score() == 10:
            basic.show_string("Enemy fever is started")
            Enemy_fever = 3
            Enemy_fever_1 = game.create_sprite(2, 2)
            Enemy_fever_2 = game.create_sprite(1, 2)
            Enemy_fever_3 = game.create_sprite(0, 2)
            for index8 in range(4):
                Enemy_fever_1.change(LedSpriteProperty.Y, 1)
            for index9 in range(4):
                Enemy_fever_1.change(LedSpriteProperty.Y, -1)
            if True:
                pass
basic.forever(on_forever)
