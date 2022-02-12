#создай игру "Лабиринт"!
from pygame import *
'''Необходимые классы'''

#класс-родитель для спрайтов
class GameSprite(sprite.Sprite):
   #конструктор класса
   def __init__(self, player_image, player_x, player_y, player_speed):
       super().__init__()
       # каждый спрайт должен хранить свойство image - изображение
       self.image = transform.scale(image.load(player_image), (65, 65))
       self.speed = player_speed
       # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
 
   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        # вместо x и y указываем self.rect.x и self.rect.y
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= 5
        if keys_pressed[K_RIGHT] and self.rect.x < 595:
            self.rect.x += 5
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= 5
        if keys_pressed[K_DOWN] and self.rect.y < 395:
            self.rect.y += 5


class Enemy(GameSprite):
    def update(self):
        if self.rect.x <= 400:
            self.direction = "right"
        if self.rect.x >= 600:
            self.direction = "left"

        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y,  wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

#Игровая сцена:
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Maze")
background = transform.scale(image.load("background1.jpg"), (win_width, win_height))
#Персонажи игры:
game = True
clock = time.Clock()
FPS = 60
#музыка
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()
 
player = Player("hero.png", 10, 400, 2)
enemy = Enemy("cyborg.png", 600,300,2)
gold = GameSprite("treasure.png", 600,400,2)

wall1 = Wall(255, 0, 0, 100, 80, 20, 400)
wall2 = Wall(255, 0, 0, 120, 100, 200, 20)
wall3 = Wall(255, 0, 0, 360, 80, 20, 400)

money = mixer.Sound('money.ogg')
kick = mixer.Sound('kick.ogg')

font.init()
font = font.Font(None, 70)
win = font.render('YOU WIN!', True, (255, 215, 0))
lose = font.render('YOU LOSE!', True, (180, 0, 0))

finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
  
    if finish != True:
        window.blit(background,(0, 0))
        wall1.draw_wall()
        wall2.draw_wall()
        wall3.draw_wall()
        player.reset()
        enemy.reset()
        gold.reset()
        player.update()
        enemy.update()
    
        if sprite.collide_rect(player, enemy) or sprite.collide_rect(player, wall1) or sprite.collide_rect(player, wall2)or sprite.collide_rect(player, wall3):
           finish = True
           window.blit(lose, (200, 200))
           kick.play()
 
       #Ситуация "Выигрыш"l
        if sprite.collide_rect(player, gold):
            finish = True
            window.blit(win, (200, 200))
            money.play()

    display.update()
    clock.tick(FPS)
