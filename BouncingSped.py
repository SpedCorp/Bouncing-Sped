import os
import random
import pygame
import logging
from datetime import datetime

# Edit later to have the images built in to the code with file unix  (i think)
Speds_Faces = "Images"
Speds_sp = [Speds_Faces + os.sep + SPED2 for SPED2 in os.listdir(Speds_Faces) if SPED2.endswith(('png', 'jpg', 'jpeg', 'gif'))]
if not Speds_sp:
    raise Exception("THE SPEDS ARE MISSING!!!")

# Get the directory of this file
current_dir = os.path.dirname(os.path.realpath(__file__))
logs_folder = os.path.join(current_dir, 'logs')  # logs folder in the same dir as script
if not os.path.exists(logs_folder):  
    os.makedirs(logs_folder)
# Add timestamp to log file name
log_file_name = f'{datetime.now().strftime("%Y%m%d-%H%M%S")}.log'  # like '20221231-235959.log'

# Create the logger
logger = logging.getLogger('Pygame Application')
logger.setLevel(logging.DEBUG)

# Create formatter and add it to handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh = logging.FileHandler(os.path.join(logs_folder, log_file_name), mode='w')  # file handler for logs
fh.setLevel(logging.DEBUG)  
fh.setFormatter(formatter)
logger.addHandler(fh)
ch = logging.StreamHandler()  # console handler (optional)
ch.setLevel(logging.ERROR)   
ch.setFormatter(formatter)
logger.addHandler(ch)

def main():
    pygame.init()
    
    Sped_Display = pygame.display.Info()
    Sped_Long = Sped_Display.current_w
    Sped_High = Sped_Display.current_h

    pygame.display.set_caption("Bouncing Speds")
    Sped_Win = pygame.display.set_mode((Sped_Long, Sped_High))
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        Sped_Win.fill((30, 30, 30))
        pygame.display.flip()

try:
    main()
except Exception as e:
    logger.error("Exception occurred", exc_info=True)
