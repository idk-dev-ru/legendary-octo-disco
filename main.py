from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, filename, size, coords):
        super().__init__()
        self.image = transform.scale(image.load(filename), size)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = coords

    def reset(self):
        mw.blit(self.image, self.rect)

class Player(GameSprite):
    def __init__(self, filename, size, coords, speed=5, keys=[K_w, K_s]):
        super().__init__(filename, size, coords)
        self.speed = speed
        self.keys = keys

    def update(self):
        keys = key.get_pressed()
        if keys[self.keys[0]] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[self.keys[1]] and self.rect.y < HEIGHT - self.rect.height:
            self.rect.y += self.speed

class Ball(GameSprite):
    def __init__(self, coords):
        super().__init__('ball.png', (50, 50), coords)
        self.speed = 5

    def update(self):
        pass

WIDTH, HEIGHT = 700, 500
FPS = 60

mw = display.set_mode((WIDTH, HEIGHT))
display.set_caption("Ping Pong")
clock = time.Clock()

player1 = Player('player.png', (30, 100), (0, 0), 5, [K_w, K_s])
player2 = Player('player.png', (30, 100), (WIDTH-30, 0), 5, [K_UP, K_DOWN])

game = True
finish = False

while game:
    if not finish:
        mw.fill((200, 250, 250))
        player1.update()
        player2.update()
        player1.reset()
        player2.reset()

    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
    clock.tick(FPS)
