input.onButtonPressed(Button.A, function () {
    Player.change(LedSpriteProperty.X, -1)
})
input.onButtonPressed(Button.AB, function () {
    Bullet = game.createSprite(Player.get(LedSpriteProperty.X), 3)
    basic.pause(250)
    for (let index = 0; index < 5; index++) {
        if (Bullet.isTouching(Enemy)) {
            Enemy.delete()
            Bullet_from_enemy.delete()
            music.playMelody("E G F G A F A G ", 296)
            game.addScore(1)
            Enemy = game.createSprite(0, 0)
            Player.delete()
            Bullet.delete()
            Player = game.createSprite(2, 4)
        } else if (Bullet.isTouching(Bullet_from_enemy)) {
            Bullet_from_enemy.delete()
            Bullet.delete()
        } else {
            Bullet.change(LedSpriteProperty.Y, -1)
            basic.pause(250)
        }
    }
    Bullet.delete()
})
input.onButtonPressed(Button.B, function () {
    Player.change(LedSpriteProperty.X, 1)
})
let Enemy_speed = 0
let sprite = 0
let Bullet_from_enemy: game.LedSprite = null
let Bullet: game.LedSprite = null
let Enemy: game.LedSprite = null
let Player: game.LedSprite = null
Player = game.createSprite(2, 4)
Enemy = game.createSprite(0, 0)
basic.forever(function () {
    for (let index = 0; index < 4; index++) {
        sprite = randint(0, 1)
        if (sprite == 0) {
            Enemy.change(LedSpriteProperty.X, 1)
            Enemy_speed = randint(0, 2)
            if (Enemy_speed == 0) {
                basic.pause(100)
            } else if (Enemy_speed == 1) {
                basic.pause(250)
            } else {
                basic.pause(500)
            }
        } else {
            Bullet_from_enemy = game.createSprite(Enemy.get(LedSpriteProperty.X), 1)
            basic.pause(500)
            Enemy.change(LedSpriteProperty.X, 1)
            for (let index = 0; index < 4; index++) {
                Bullet_from_enemy.change(LedSpriteProperty.Y, 1)
                basic.pause(250)
                if (Bullet_from_enemy.isTouching(Player)) {
                    music.playMelody("E B C5 A B G A F ", 300)
                    music.playMelody("E - - - - - - - ", 103)
                    basic.showString("Made by DanielY121")
                    basic.pause(250)
                    game.gameOver()
                }
            }
            Bullet_from_enemy.delete()
        }
    }
    for (let index = 0; index < 4; index++) {
        sprite = randint(0, 1)
        if (sprite == 0) {
            Enemy.change(LedSpriteProperty.X, -1)
            Enemy_speed = randint(0, 2)
            if (Enemy_speed == 0) {
                basic.pause(100)
            } else if (Enemy_speed == 1) {
                basic.pause(250)
            } else {
                basic.pause(500)
            }
        } else {
            Bullet_from_enemy = game.createSprite(Enemy.get(LedSpriteProperty.X), 1)
            basic.pause(500)
            Enemy.change(LedSpriteProperty.X, -1)
            for (let index = 0; index < 4; index++) {
                Bullet_from_enemy.change(LedSpriteProperty.Y, 1)
                basic.pause(250)
                if (Bullet_from_enemy.isTouching(Player)) {
                    music.playMelody("E B C5 A B G A F ", 300)
                    music.playMelody("E - - - - - - - ", 103)
                    basic.showString("Made by DanielY121")
                    basic.pause(250)
                    game.gameOver()
                }
            }
            Bullet_from_enemy.delete()
        }
    }
})
