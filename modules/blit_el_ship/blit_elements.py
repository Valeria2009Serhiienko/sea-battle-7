import pygame
import modules.main_modules.settings as m_settings
pygame.init()

class Bg(m_settings.Settings):
    def __init__(self, width1 = 1000, height1 = 700, x1 = 0, y1 = 0, name1 = 'img/bg_elements/background.png'):
        m_settings.Settings.__init__(self, width = width1, height = height1, x = x1, y = y1, file_name = name1)
        self.load_image()
bg = Bg()

class Button_start(m_settings.Settings):
   def __init__(self, width1 = 234, height1 = 60, x1 = 387, y1 = 270, name1 = 'img/bg_elements/button_start.png'):
       m_settings.Settings.__init__(self, width = width1, height = height1, x = x1, y = y1, file_name = name1)
       self.load_image()
start = Button_start()

class Field(m_settings.Settings):
    def __init__(self, width1 = 275, height1 = 274, x1 = 350, y1 = 170, name1 = 'img/cell/field.png'):
        m_settings.Settings.__init__(self, width = width1, height = height1, x = x1, y = y1, file_name = name1)
        self.load_image()
field = Field()

class Button_ready(m_settings.Settings):
    def __init__(self, width1 = 219, height1 = 71, x1 = 370, y1 = 480, name1 = 'img/bg_elements/button_ready.png'):
        m_settings.Settings.__init__(self, width = width1, height = height1, x = x1, y = y1, file_name = name1)
        self.load_image()
ready = Button_ready()

