import pygame
from pygame.locals import KEYDOWN, K_ESCAPE, K_RETURN, K_LEFT, K_RIGHT, K_UP, K_DOWN, QUIT
import time
import random

SIZE = 40
BACKGROUND_COLOR = (88, 140, 56)
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 500

class Apple:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load(r"D:\Pic\apple.png").convert()
        self.x = 110
        self.y = 110

    def draw(self):
        
        self.parent_screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.x = random.randint(0, (WINDOW_WIDTH // SIZE) - 1) * SIZE
        self.y = random.randint(0, (WINDOW_HEIGHT // SIZE) - 1) * SIZE

class Snake:
    def __init__(self, parentscreen):
        self.parentscreen = parentscreen
        self.image = pygame.image.load(r"D:\Pic\snak.jpg").convert()
        self.direction = "down"
        self.length = 0
        self.x = [40]
        self.y = [40]

    def moveleft(self):
        if self.direction != 'right':
            self.direction = 'left'

    def moveright(self):
        if self.direction != 'left':
            self.direction = 'right'

    def moveup(self):
        if self.direction != 'down':
            self.direction = 'up'

    def movedown(self):
        if self.direction != 'up':
            self.direction = 'down'

    def walk(self):
        for i in range(self.length - 1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]

        if self.direction == "left":
            self.x[0] -= SIZE
        if self.direction == "right":
            self.x[0] += SIZE

        if self.direction == "up":
            self.y[0] -= SIZE
        if self.direction == "down":
            self.y[0] += SIZE

        self.draw()

    def draw(self):
        for i in range(max(1, self.length)):
            self.parentscreen.blit(self.image, (self.x[i], self.y[i]))

    def increase_length(self):
        if self.length == 0:
            self.length = 1  
        else:
            self.length += 1
            self.x.append(self.x[-1])
            self.y.append(self.y[-1])

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Snake Game")
        self.surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))  
        self.snake = Snake(self.surface)
        self.apple = Apple(self.surface)

    def reset(self):
        self.snake = Snake(self.surface)
        self.apple = Apple(self.surface)

    def is_collision(self, x1, y1, x2, y2):
        return (x1 < x2 + SIZE and x1 + SIZE > x2 and y1 < y2 + SIZE and y1 + SIZE > y2)

    def play(self):
        self.surface.fill(BACKGROUND_COLOR)
        self.snake.walk()
        self.apple.draw()
        self.display_score()

        
        if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            self.snake.increase_length()
            self.apple.move()  

        
        for i in range(3, self.snake.length):
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                raise Exception("Collision Occurred")

        pygame.display.flip()

    def display_score(self):
        font = pygame.font.SysFont('arial', 30)
        score = font.render(f"Score: {self.snake.length}", True, (200, 200, 200))
        self.surface.blit(score, (650, 10))  

    def show_game_over(self):
        self.surface.fill(BACKGROUND_COLOR) 
        font = pygame.font.SysFont('arial', 30)
        line1 = font.render(f"Game is over! Your score is {self.snake.length}", True, (255, 255, 255))
        self.surface.blit(line1, (200, 200))
        line2 = font.render("To play again press ENTER. To exit press ESCAPE!", True, (255, 255, 255))
        self.surface.blit(line2, (200, 250))
        pygame.display.flip()

    def run(self):
        running = True
        pause = False

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_RETURN:
                        pause = False
                    if not pause:
                        if event.key == K_LEFT:
                            self.snake.moveleft()
                        if event.key == K_RIGHT:
                            self.snake.moveright()
                        if event.key == K_UP:
                            self.snake.moveup()
                        if event.key == K_DOWN:
                            self.snake.movedown()
                elif event.type == QUIT:
                    running = False

            try:
                if not pause:
                    self.play()
            except Exception as e:
                print(f"Error: {e}")
                self.show_game_over()
                pause = True
                self.reset()

            time.sleep(0.1)

if __name__ == '__main__':
    game = Game()
    game.run()