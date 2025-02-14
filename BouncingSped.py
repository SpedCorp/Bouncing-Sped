import os
import random
import pygame

# Edit later to have the images built in to the code with file unix (i think)
Speds_Faces = "Images"
Speds_sp = [os.path.join(Speds_Faces, f) for f in os.listdir(Speds_Faces) if f.lower().endswith(('png', 'jpg', 'jpeg', 'gif', 'webp'))]
if not Speds_sp:
    raise Exception("THE SPEDS ARE MISSING!!!")
pygame.init()
# Screen Size
Sped_Display = pygame.display.Info()
Sped_Long = Sped_Display.current_w
Sped_High = Sped_Display.current_h
pygame.display.set_caption("Bouncing Speds")
Sped_Win = pygame.display.set_mode((Sped_Long, Sped_High))
class Sped:
    def __init__(self, SPED2):
        self.image = pygame.image.load(SPED2)
        self.image = pygame.transform.scale(self.image, (300, 300))  # Resize for better visibility
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, Sped_Long - self.rect.width)
        self.rect.y = random.randint(0, Sped_High - self.rect.height)
        self.speed_x = random.choice([-3, 3])
        self.speed_y = random.choice([-3, 3])
    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.left <= 0 or self.rect.right >= Sped_Long:
            self.speed_x = -self.speed_x
            self.swap_image()
        if self.rect.top <= 0 or self.rect.bottom >= Sped_High:
            self.speed_y = -self.speed_y
            self.swap_image()
    def swap_image(self):
        new_image_path = random.choice(Speds_sp)
        self.image = pygame.image.load(new_image_path)
        self.image = pygame.transform.scale(self.image, (300, 300))

# Initialize a single Sped object
sped = Sped(random.choice(Speds_sp))

# Game Loop
running = True
clock = pygame.time.Clock()
while running:
    Sped_Win.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
            running = False
    sped.move()
    Sped_Win.blit(sped.image, sped.rect)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()