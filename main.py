import pygame

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Game")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Load an image
player_image = pygame.image.load('player.png')
player_rect = player_image.get_rect()
image_x = 0
image_y = 0
image_speed = 5

# Load a sound
sound = pygame.mixer.Sound('sound.wav')

# Set up fonts
font = pygame.font.SysFont('arial', 55)

# Run the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if player_rect.collidepoint(event.pos):
                sound.play()

    # Get the keys pressed
    keys = pygame.key.get_pressed()

    # Update the image's position
    if keys[pygame.K_LEFT]:
        image_x -= image_speed
    if keys[pygame.K_RIGHT]:
        image_x += image_speed
    if keys[pygame.K_UP]:
        image_y -= image_speed
    if keys[pygame.K_DOWN]:
        image_y += image_speed

    # Update the image rectangle position
    player_rect.topleft = (image_x, image_y)

    # Fill the screen with black
    screen.fill(BLACK)

    # Draw the image
    screen.blit(player_image, (image_x, image_y))

    # Display text
    text = font.render('Hello, Pygame!', True, WHITE)
    screen.blit(text, (250, 500))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)
