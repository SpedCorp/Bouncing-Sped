import pygame
import os
import random

# Initialize pygame
pygame.init()

# Get screen dimensions
infoObject = pygame.display.Info()
SCREEN_WIDTH, SCREEN_HEIGHT = infoObject.current_w, infoObject.current_h

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.NOFRAME)
pygame.display.set_caption("Bouncing Images")

# Load images from 'photos' folder
image_folder = "Images"
images = [os.path.join(image_folder, f) for f in os.listdir(image_folder) if f.lower().endswith(('png', 'jpg', 'jpeg', 'gif'))]

if not images:
    raise Exception("No images found in the 'photos' folder.")

# Class for bouncing images
class BouncingImage:
    def __init__(self, img_path):
        self.image = pygame.image.load(img_path)
        self.image = pygame.transform.scale(self.image, (100, 100))  # Resize for better visibility
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randint(0, SCREEN_HEIGHT - self.rect.height)
        self.speed_x = random.choice([-3, 3])
        self.speed_y = random.choice([-3, 3])

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.left <= 0 or self.rect.right >= SCREEN_WIDTH:
            self.speed_x = -self.speed_x
            return True  # Signal to spawn a new image
        if self.rect.top <= 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.speed_y = -self.speed_y
            return True  # Signal to spawn a new image
        return False

# Initial bouncing image
bouncing_images = [BouncingImage(random.choice(images))]

# Main loop
running = True
clock = pygame.time.Clock()
while running:
    screen.fill((0, 0, 0))  # Clear the screen

    for event in pygame.event.get():
        if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
            running = False

    # Move and draw images
    for img in bouncing_images[:]:
        if img.move():  # If an image hits a wall, add a new one
            bouncing_images.append(BouncingImage(random.choice(images)))
        screen.blit(img.image, img.rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
