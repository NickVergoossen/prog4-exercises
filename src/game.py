import pygame
import random

WIDTH = 800
HEIGHT = 600


class Bullet:
    def __init__(self, x, y):
        # De positie van de speler
        self.x = x
        self.y = y
        # De verplaatsing van een kogel op de Y-as
        self.y_change = -5

    def update(self):
        # We passen enkel de Y-positie aan, omdat de kogel enkel verticaal
        # beweegt
        self.y += self.y_change

    def blit(self, screen, img):
        screen.blit(img, (self.x, self.y))

class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.y_change = +2

    def update(self):
        self.y += self.y_change
        if self.y >= HEIGHT:
            self.x = random.randint(0, WIDTH)
            self.y = 0

    def blit(self, screen, img):
        screen.blit(img, (self.x, self.y))

pygame.init()

# Maak een venster aan met de opgegeven resolutie
screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

# Laad de "sprites" (afbeeldingen) in
player_img = pygame.image.load("./foto's/ship.png").convert_alpha()
bullet_img = pygame.image.load("./foto's/bullet.png").convert_alpha()
enemy_img = pygame.image.load("./foto's/enemyship.png").convert_alpha()

# De positie van de speler
player_x = WIDTH / 2
player_y = 500

# De verplaatsing van de speler op de X-as
player_xchange = 0
PLAYER_SPEED = 5

# De posities van alle kogels als een lijst van X- en Y-coordinaten
bullets = []

# Positie van de vijand, en verplaatsing van de vijand
enemies = []
nieuwe_enemy = Enemy(random.randint(0, WIDTH),  0)
enemies.append(nieuwe_enemy)
nieuwe_enemy = Enemy(random.randint(0, WIDTH),  0)

enemies.append(nieuwe_enemy)

# Een variabele die we op False kunnen zetten om uit de while-lus te geraken
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Als de speler op de spatiebalk drukt,
                # maak dan een nieuwe lijst aan met de X- en Y-coordinaat
                # van de nieuwe kogel
                nieuwe_kogel = Bullet(x=player_x, y=player_y)
                # Voeg deze lijst toe aan de lijst van kogels
                bullets.append(nieuwe_kogel)
            if event.key == pygame.K_LEFT:
                # Als de speler op het linkerpijltje drukt
                # stel dan de verplaatsing van de speler in naar links
                player_xchange -= PLAYER_SPEED
            if event.key == pygame.K_RIGHT:
                # Als de speler op het rechterpijltje drukt
                # stel dan de verplaatsing van de speler in naar rechts
                player_xchange += PLAYER_SPEED
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                # Als de speler het linkerpijltje loslaat
                # stel dan de verplaatsingsnelheid in op 0
                player_xchange = 0
            elif event.key == pygame.K_RIGHT:
                # Als de speler het rechterpijltje loslaat
                # stel dan de verplaatsingsnelheid in op 0
                player_xchange = 0

    # Verplaats de speler
    player_x += player_xchange
    for enemy in enemies:
        enemy.update()


    # Verplaats de kogels door voor ieder element
    # de update() functie uit te voeren.
    for bullet in bullets:
        bullet.update()

    # Veeg het scherm uit
    screen.fill("black")

    # Teken de speler
    screen.blit(player_img, (player_x, player_y))

    # Teken de vijand
    for enemy in enemies:
        enemy.blit(screen, enemy_img)

    # Teken alle kogels in de lijst
    for bullet in bullets:
        bullet.blit(screen, bullet_img)

    # Update het scherm
    pygame.display.flip()

    # Wacht zodanig dat we maximal 60 FPS halen
    clock.tick(60)