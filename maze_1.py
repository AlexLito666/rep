from pygame import *
'''Необходимые классы''' 

#Игровая сцена:
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Maze")
background = transform.scale(image.load("background1.jpg"), (700, 500))
 
#Персонажи игры:

 
game = True
clock = time.Clock()
FPS = 60
 
#музыка
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()
 
while game:
   for e in event.get():
       if e.type == QUIT:
           game = False
  
   window.blit(background,(0, 0))
  
 
   display.update()
   clock.tick(FPS)
