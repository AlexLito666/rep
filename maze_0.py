from pygame import *

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

#создай окно игры
window = display.set_mode((700, 500))
display.set_caption("Догонялки")
#задай фон сцены
background = transform.scale(image.load("background1.jpg"),    (700, 500))

clock = time.Clock()
FPS = 60

player = GameSprite("hero.png", 10, 400, 5)
enemy = GameSprite("cyborg.png", 500, 300, 2)
gold = GameSprite("treasure.png", 600, 400, 0)


game = True
while game:
    for e in event.get():    #обработай событие «клик по кнопке "Закрыть окно"»
        if e.type == QUIT:
            game = False

    window.blit(background,(0, 0))
    player.reset()
 

    display.update()
    clock.tick(FPS)




