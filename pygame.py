import pygame
import sys

# Initialisierung von Pygame
pygame.init()

# Fenstergröße und Titel
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Beweglicher Kreis')

# Farben
white = (255, 255, 255)
blue = (0, 0, 255)

# Kreisparameter
radius = 50
x, y = width // 2, height // 2
speed = 5

clock = pygame.time.Clock()

# Haupt-Loop
running = True
while running:
    window.fill(white)  # Hintergrundfarbe

    # Event-Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Bewegung des Kreises basierend auf den Tasteneingaben
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed

    # Begrenzen der Kreisbewegung innerhalb des Fensters
    x = max(radius, min(x, width - radius))
    y = max(radius, min(y, height - radius))

    # Zeichnen des Kreises
    pygame.draw.circle(window, blue, (x, y), radius)

    pygame.display.flip()
    clock.tick(60)  # Begrenzung der Framerate

pygame.quit()
sys.exit()
