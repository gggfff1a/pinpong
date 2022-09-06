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
