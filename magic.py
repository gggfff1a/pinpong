from pygame import *
from random import randint
from time import time as timer

window = display.set_mode((700, 500))
display.set_caption('Шутер')
win_w = 700
win_h = 500
backgroud = transform.scale(image.load('galaxy.jpg'), (win_w, win_h))#изменить картинку

game = True
clock = time.Clock()
FPS = 60

mixer.init()
mixer.music.load('space.ogg')#изменить фоновую музыку
mixer.music.play()
fire_sound = mixer.Sound('fire.ogg')#найти звук отибивания меча рокеткой

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_y, size_x, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_y, size_x))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.plaer_x = player_x
        self.plaer_y = player_y
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
      keys = key.get_pressed()
      if keys[K_w]and self.rect.y > 5:
        self.rect.y -= self.sped
      if keys[K_s]and self.rect.y < win_hait-80:
        self.rect.y -= self.sped
        
    def update_r(self):
      keys = key.get_pressed()
      if keys[K_UP]and self.rect.y > 5:
        self.rect.y -= self.sped
      if keys[K_DAYN]and self.rect.y < win_hait-80:
        self.rect.y -= self.sped
        
        
 rocket1 = Player('rocket.png', 30, 200, 4, 50, 150)
 rocket2 = Player('rocket.png', 520, 200, 4, 50, 150)
 boll = GameSprite('tenis_ball.png', 200, 200, 4, 50, 50)

font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER  1 LOSE!', True, (180, 0, 0))
lose2 = font.render('PLAYER  2 LOSE!', True, (180, 0, 0))

speed_x = 3 
speed_y = 3 

wile game:
    for e in event.get():
        if e.type == QUIT:
            game = false
            
    if finish != True:
        window.fill(back)
        racket1.update_l()
        racket1.update_r()
        ball.rect.x += spee_x
        ball.rect.y += spee_y

        if sprite.collide_rect(racket, ball) or sprite.colide_rect(racket2, ball):
            sped_x *= -1
            sped_y *= -1

        if ball.rect.y > win_height-50 or ball.rect,y < 0:
            speed_y *= -1

        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))
            game_over = true

        if ball.rect.x < win_width:
            finish = True
            window.blit(lose1, (200, 200))
            game_over = true

        racket1.reset()
        racket1.reset()
        ball.reset()
        
   dicplay.update
   clock.tick(FPS)
                
