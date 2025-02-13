import os
import random
import pygame

#Edit later to have the images built in to the code with file unix (i think)
Speds_Faces = "Images"
Speds_sp = [Speds_Faces + os.sep + SPED2 for SPED2 in os.listdir(Speds_Faces) if SPED2.endswith(('png', 'jpg', 'jpeg', 'gif'))]
if not Speds_sp:
    raise Exception("THE SPEDS ARE MISSING!!!")

pygame.init()

#Screen Size
Sped_Display = pygame.display.Info()
Sped_Long = Sped_Display.current_w
Sped_High = Sped_Display.current_h

pygame.display.set_caption("Bouncing Speds")
Sped_Win = pygame.display.set_mode((Sped_Long, Sped_High))

