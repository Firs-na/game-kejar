from pygame import *
import math

#step 2: buat kelas
class karakter(sprite.Sprite):
    #karakteristik
    def __init__(self, filename, x,y,width,height,player_speed):
        # Call for the class (Sprite) constructor:
        sprite.Sprite.__init__(self)
        # every sprite must store the image property
        self.image = transform.scale(image.load(filename), (width, height))
        self.speed = player_speed
        # every sprite must have the rect property – the rectangle it is fitted in
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    #method
    #draw karakternya ke dalam screen
    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

#kelas untuk karakter dikejar (kontrol)
class karakter_target(karakter):
    #method untuk kontrol
    def control(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 50:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 50:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 5:
            self.rect.y += self.speed
            
#step 3: buat screen
win_width = 500
win_height = 500
screen = display.set_mode((win_width,win_height))
img_background = "back.jpeg"
background = transform.scale(image.load(img_background), (win_width, win_height))
#step 4: upload karakter
#karakter yang ngejar
dog = karakter("anjing tom and jarry.png", 200,100,50,50,8)
#karakter yang dikejar
tom = karakter_target("tom an jerry.png",100,100,50,50,5)

#step 5: buat permainan
fps = time.Clock()
game_start = True
while game_start:
    #tampilin background
    screen.blit(background, (0,0))
    dog.draw()
    tom.draw()
    tom.control() #bergerak
    #peraturan
    for e in event.get():
        #jika kita pencet tombol silang x
        if e.type == QUIT:
            quit()
    
    #kita akan buat karakter kita mengejar
    dx = tom.rect.x - dog.rect.x
    dy = tom.rect.y - dog.rect.y
    distance = math.hypot(dx, dy)
    if distance != 0:
        dx /= distance
        dy /= distance
        dog.rect.x += dx * 5 #5 = speed karakter yg ngejar
        dog.rect.y += dy * 5 #5 = speed karakter yg ngejar
    
    display.update()
    fps.tick(60)