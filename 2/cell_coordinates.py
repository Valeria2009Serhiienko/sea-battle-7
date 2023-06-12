'''

cell_list = [
            [[350, 170], [350, 197], [377, 170], [377, 197]],[404, 170, 404, 197, 431, 170, 431, 197],[431, 170, 431, 197, 458, 170, 458, 197],
            
            [485, 170, 485, 197, ],
            [366, 170, 231, 393],
            [420, 170, 447, 197],
            [447, 170, 474, 197],
            [501, 170, 528, 197],
            [555, 170, 582 , 197],
            [609, 170, 636, 197],
            [350, 197, 377, 224],[204, 170, 231, 197],[],[],[],[],[],[],[],[],
            ]       '''


'''
class Ship_1_1(m_settings.Settings):
    def __init__(self, width1 = 25, height1 = 25, x1 = 770, y1 = 180, name1 = 'img/ship/ship_1.png'):
        m_settings.Settings.__init__(self, width = width1, height = height1, x = x1, y = y1, file_name = name1)
        self.load_image()
ship_1_1 = Ship_1_1()

class Ship_1_2(m_settings.Settings):
    def __init__(self, width1 = 25, height1 = 25, x1 = 770, y1 = 230, name1 = 'img/ship/ship_1.png'):
        m_settings.Settings.__init__(self, width = width1, height = height1, x = x1, y = y1, file_name = name1)
        self.load_image()
ship_1_2 = Ship_1_2()

class Ship_1_3(m_settings.Settings):
    def __init__(self, width1 = 25, height1 = 25, x1 = 770, y1 = 280, name1 = 'img/ship/ship_1.png'):
        m_settings.Settings.__init__(self, width = width1, height = height1, x = x1, y = y1, file_name = name1)
        self.load_image()


class Ship_1_4(m_settings.Settings):
    def __init__(self, width1 = 25, height1 = 25, x1 = 770, y1 = 330, name1 = 'img/ship/ship_1.png'):
        m_settings.Settings.__init__(self, width = width1, height = height1, x = x1, y = y1, file_name = name1)
        self.load_image()
ship_1_4 = Ship_1_4()


# 2
class Ship_2_1(m_settings.Settings):
    def __init__(self, width1 = 50, height1 = 25, x1 = 770, y1 = 180, name1 = 'img/ship/ship_2.png'):
        m_settings.Settings.__init__(self, width = width1, height = height1, x = x1, y = y1, file_name = name1)
        self.load_image()
#ship_2_1 = Ship_2_1()

class Ship_2_2(m_settings.Settings):
    def __init__(self, width1 = 50, height1 = 25, x1 = 770, y1 = 230, name1 = 'img/ship/ship_2.png'):
        m_settings.Settings.__init__(self, width = width1, height = height1, x = x1, y = y1, file_name = name1)
        self.load_image()
#ship_2_2 = Ship_2_2()

class Ship_2_3(m_settings.Settings):
    def __init__(self, width1 = 50, height1 = 25, x1 = 770, y1 = 280, name1 = 'img/ship/ship_2.png'):
        m_settings.Settings.__init__(self, width = width1, height = height1, x = x1, y = y1, file_name = name1)
        self.load_image()
#ship_2_3 = Ship_2_3()


# 3 
class Ship_3_1(m_settings.Settings):
    def __init__(self, width1 = 75, height1 = 25, x1 = 770, y1 = 180, name1 = 'img/ship/ship_3.png'):
        m_settings.Settings.__init__(self, width = width1, height = height1, x = x1, y = y1, file_name = name1)
        self.load_image()      
#ship_3_1 = Ship_3_1()

class Ship_3_2(m_settings.Settings):
    def __init__(self, width1 = 75, height1 = 25, x1 = 770, y1 = 230, name1 = 'img/ship/ship_3.png'):
        m_settings.Settings.__init__(self, width = width1, height = height1, x = x1, y = y1, file_name = name1)
        self.load_image()       
#ship_3_2 = Ship_3_2()




        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            turn = event.pos  
            if m_ship.ship_4.X <= turn[0] <= m_ship.ship_4.X + m_ship.ship_4.WIDTH and m_ship.ship_4.Y <= turn[1] <= m_ship.ship_4.Y + m_ship.ship_4.HEIGHT:
                m_ship.ship_4.load_image(check_img= False)
'''