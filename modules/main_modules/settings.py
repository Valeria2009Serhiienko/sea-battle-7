import pygame
import modules.main_modules.path_to_file as m_path
pygame.init()

class Settings:
    def __init__(self, width= 0, height= 0, x= 0, y= 0, file_name= None, direction_x = False, direction_y = False):
        self.WIDTH = width
        self.HEIGHT = height

        self.X = x
        self.Y = y

        self.FILE_NAME = file_name
        self.IMG = None

        self.DIRECTION_X = direction_x
        self.DIRECTION_Y = direction_y

    def load_image(self, check_img= True):
        image_load = pygame.image.load(m_path.find_path_to_file(self.FILE_NAME))
        transform_image = pygame.transform.scale(image_load, (self.WIDTH, self.HEIGHT))
        self.IMG = transform_image
        if check_img == False:
            self.IMG = pygame.transform.rotate(transform_image, -90)
        else:
           return pygame.transform.rotate(transform_image, 90)

        
    def blit_sprite(self, screen):
        screen.blit(self.IMG, (self.X, self.Y))  

#if turn_4 == False:
#self.IMG = pygame.transform.rotate(transform_image, -90)
#else:
#    return pygame.transform.rotate(transform_image, 90)
    


            
    