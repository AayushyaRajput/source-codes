import math 
import random
import pygame
from pygame import mixer

pygame.init()

screen = pygame.display.set_mode((800,600))
background = pygame.image.load(r"D:/Pic/background.png")

mixer.music.load(r"D:/Pic/backsound.wav")
mixer.music.play(-1)

pygame.display.set_caption("Space Invader")
icon = pygame.image.load(r"D:/Pic/ufo.png")
pygame.display.set_icon(icon)

playerImg = pygame.image.load("D:/Pic/player.png")
playerX = 370
playerY = 480
playerX_change = 0

num_enemies = 4
enemyImg = [pygame.image.load("D:/Pic/enemy.png")for _ in range(num_enemies)]
enemyX = [random.randint(0,736)for _ in range(num_enemies)]
enemyY = [random.randint(50,150)for _ in range(num_enemies)]
enemyX_change = [4] * num_enemies
enemyY_change = [40] * num_enemies

bulletImg = pygame.image.load(r"D:/Pic/bullet.png")
bulletX = 0
bulletY = 480
bulletY_change = 10
bullet_state = "ready"

score_value = 0

font = pygame.font.Font("freesansbold.ttf", 32)
over_font = pygame.font.Font("freesansbold.ttf", 64)

def score(x,y):
    screen.blit(font.render(f"Score {score_value}",True,(255,255,255)),( x, y ))

def game_over():
    screen.blit(over_font.render("Game Over",True,(255,255,255)),(200,250))

def player(x,y):
    screen.blit(playerImg,(x,y))

def enemy(x,y,i):
    screen.blit(enemyImg[i],(x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg,(x+16,y+10))

def collision(ex,ey,bx,by):
    return math.sqrt((ex - bx)**2 + (ey - by ) **2) < 27  

running = True
while running:
    screen.fill((0,0,0))
    screen.blit(background,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -3
            elif event.key == pygame.K_RIGHT:
                playerX_change = 3
            elif event.key == pygame.K_SPACE and bullet_state == "ready":
                mixer.Sound(r"D:/Pic/laser.wav").play()
                bulletX = playerX
                fire_bullet(bulletX,bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX = max(0, min(playerX + playerX_change,736))

    for i in range(num_enemies):
        if enemyY[i] > 440:
            enemyY = [2000] * num_enemies
            game_over()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i]<=0 or enemyX[i] >= 736:
            enemyX_change[i] *= -1
            enemyY[i] += enemyY_change[i]

        if collision(enemyX[i],enemyY[i],bulletX,bulletY):
            mixer.Sound(r"D:/Pic/explosion.wav").play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0,736)
            enemyY[i] = random.randint(50,150)   

        enemy(enemyX[i],enemyY[i],i)

    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX,bulletY)
        bulletY -= bulletY_change

    player(playerX,playerY)
    score(10,10)
    pygame.display.update()                                      



