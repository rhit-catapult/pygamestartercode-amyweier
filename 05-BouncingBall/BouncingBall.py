import pygame
import sys
import random


# You will implement this module ENTIRELY ON YOUR OWN!

class Ball:
    def __init__(self, screen):
        self.screen = screen
        self.radius = random.randint(10,50)
        self.x = random.randint(0 + self.radius, 600 - self.radius)
        self.y = random.randint(0 + self.radius, 1000 - self.radius)
        self.speed_x = random.randint(5,10)
        self.speedy = random.randint(5,10)

    def move(self):
        self.x = self.x + self.speed_x
        self.y = self.y + self.speedy
        if self.x + self.radius > self.screen.get_width():
            self.speed_x = -self.speed_x
            self.x = -2*self.radius + 2*self.screen.get_width() - self.x
        if self.x - self.radius < 0:
            self.speed_x = -self.speed_x
            self.x = 2*self.radius - self.x
        if self.y + self.radius > self.screen.get_height():
            self.speedy = -self.speedy
            self.y = 2*self.screen.get_height() - 2*self.radius - self.y
        if self.y - self.radius < 0:
            self.speedy = -self.speedy
            self.y = 2*self.radius - self.y

    def draw(self):
        pygame.draw.circle(self.screen, (0, 105, 150), (self.x, self.y), self.radius)


def main():
    pygame.init()
    screen = pygame.display.set_mode((1000, 600))
    pygame.display.set_caption('Bouncing Ball')
    clock = pygame.time.Clock()
    num_balls = 20
    list = []
    for i in range(20):
        list.append(Ball(screen))
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(pygame.Color('gray'))
        for ball in list:
            ball.draw()
            ball.move()



        pygame.display.update()


main()


# Optional challenges (if you finish and want do play a bit more):
#   After you get 1 ball working make a few balls (ball2, ball3, etc) that start in different places.
#   Make each ball a different color
#   Make the screen 1000 x 800 to allow your balls more space (what needs to change?)
#   Make the speed of each ball randomly chosen (1 to 5)
#   After you get that working try making a list of balls to have 100 balls (use a loop)!
#   Use random colors for each ball
