import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the game window
screen_width, screen_height = 800, 600  # You can adjust these dimensions as needed
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Planes, Trains, and Automobiles - The Game")

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Allows the game window to close
            pygame.quit()
            sys.exit()

    # Fill the screen with a color (e.g., white)
    screen.fill((255, 255, 255))

    # Update the display
    pygame.display.flip()  # Refreshes the screen