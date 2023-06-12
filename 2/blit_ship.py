import pygame
import modules.main_modules.settings as m_settings
import modules.main_modules.data_base as m_data
pygame.init()

# 4
class Ship_4(m_settings.Settings):
    def __init__(self, width1 = 100, height1 = 25, x1 = 770, y1 = 180,
                
                list_ship_4 = m_data.list_x[3], 
                list_ship_3 = m_data.list_x[2], 
                list_ship_2 = m_data.list_x[1], 
                list_ship_1 = m_data.list_x[0], 
                name1 = 'img/ship/ship_4.png',

                direction_x1 = 0, direction_y1 = 0,):
        m_settings.Settings.__init__(self, width = width1, height = height1, x = x1, y = y1, 
                file_name = name1, direction_x= direction_x1, direction_y= direction_y1)
        self.load_image()   
        self.ROTATE = False

        self.LIST_SHIP_4 = list_ship_4
        self.LIST_SHIP_3 = list_ship_3
        self.LIST_SHIP_2 = list_ship_2
        self.LIST_SHIP_1 = list_ship_1

    def rotate(self, number_X, number_Y):
        for cell in m_data.list_cells:
            if self.ROTATE:
                if self.Y <= 395 + cell.HEIGHT and 400 + cell.HEIGHT:
                    self.X = 375 
                    self.Y = 414 + self.LIST_SHIP_4 
        
    def collision_ship_4(self):
        for cell in m_data.list_cells:
                            
            if self.X >= 350 and self.X <= 350 + cell.WIDTH:
                if self.Y <= 170 + cell.HEIGHT and 375 + cell.HEIGHT:
                    self.X = 350 + self.LIST_SHIP_4 
                    self.Y = 171

                    if self.ROTATE:
                        if self.Y <= 170 + cell.HEIGHT and 375 + cell.HEIGHT:
                            self.X = 351 
                            self.Y = 171 + self.LIST_SHIP_4 
                    
                elif self.Y <= 195 + cell.HEIGHT and 375 + cell.HEIGHT:
                    self.X = 350 + self.LIST_SHIP_4
                    self.Y = 198 

                    if self.ROTATE:
                        if self.Y <= 195 + cell.HEIGHT and 375 + cell.HEIGHT:
                            self.X = 351 
                            self.Y = 198 + self.LIST_SHIP_4 

                elif self.Y <= 220 + cell.HEIGHT and 375 + cell.HEIGHT:
                    self.X = 350 + self.LIST_SHIP_4
                    self.Y = 225

                    if self.ROTATE:
                        if self.Y <= 220 + cell.HEIGHT and 375 + cell.HEIGHT:
                            self.X = 351 
                            self.Y = 225 + self.LIST_SHIP_4 

                elif self.Y <= 245 + cell.HEIGHT and 375 + cell.HEIGHT:
                    self.X = 350 + self.LIST_SHIP_4
                    self.Y = 252

                    if self.ROTATE:
                        if self.Y <= 245 + cell.HEIGHT and 375 + cell.HEIGHT:
                            self.X = 351 
                            self.Y = 252 + self.LIST_SHIP_4 

                elif self.Y <= 270 + cell.HEIGHT and 375 + cell.HEIGHT:
                    self.X = 350 + self.LIST_SHIP_4
                    self.Y = 279

                    if self.ROTATE:
                        if self.Y <= 270 + cell.HEIGHT and 375 + cell.HEIGHT:
                            self.X = 351 
                            self.Y = 279 + self.LIST_SHIP_4 

                elif self.Y <= 295 + cell.HEIGHT and 375 + cell.HEIGHT:
                    self.X = 350 + self.LIST_SHIP_4
                    self.Y = 306

                    if self.ROTATE:
                        if self.Y <= 295 + cell.HEIGHT and 375 + cell.HEIGHT:
                            self.X = 351 
                            self.Y = 306 + self.LIST_SHIP_4 

                elif self.Y <= 320 + cell.HEIGHT and 375 + cell.HEIGHT:
                    self.X = 350 + self.LIST_SHIP_4
                    self.Y = 333

                    if self.ROTATE:
                        if self.Y <= 320 + cell.HEIGHT and 375 + cell.HEIGHT:
                            self.X = 351 
                            self.Y = 333 + self.LIST_SHIP_4 
                    
                elif  self.Y <= 345 + cell.HEIGHT and 375 + cell.HEIGHT:
                    self.X = 350 + self.LIST_SHIP_4
                    self.Y = 360

                    if self.ROTATE:
                        if self.Y <= 345 + cell.HEIGHT and 375 + cell.HEIGHT:
                            self.X = 351 
                            self.Y = 360 + self.LIST_SHIP_4 
                            
                elif  self.Y <= 370 + cell.HEIGHT and 375 + cell.HEIGHT:
                    self.X = 350 + self.LIST_SHIP_4
                    self.Y = 387

                    if self.ROTATE:
                        if  self.Y <= 370 + cell.HEIGHT and 375 + cell.HEIGHT:
                            self.X = 351 
                            self.Y = 387 + self.LIST_SHIP_4 
                            
                elif  self.Y <= 395 + cell.HEIGHT and 375 + cell.HEIGHT:
                    self.X = 350 + self.LIST_SHIP_4
                    self.Y = 414

                    if self.ROTATE:
                        if  self.Y <= 395 + cell.HEIGHT and 375 + cell.HEIGHT:
                            self.X = 351 
                            self.Y = 414 + self.LIST_SHIP_4 
            # друга клітинка 
            if self.X >= 375 and self.X <= 375 + cell.WIDTH:
                if self.Y <= 170 + cell.HEIGHT and 400 + cell.HEIGHT:
                    self.X = 375 + self.LIST_SHIP_4 + 2
                    self.Y = 171

                    if self.ROTATE:
                        if self.Y <= 170 + cell.HEIGHT and 400 + cell.HEIGHT:
                            self.X = 375
                            self.Y = 171 + self.LIST_SHIP_4 
                ##
                elif self.Y <= 195 + cell.HEIGHT and 400 + cell.HEIGHT:
                    self.X = 375 + self.LIST_SHIP_4 
                    self.Y = 198

                    if self.ROTATE:
                        if self.Y <= 195 + cell.HEIGHT and 400 + cell.HEIGHT:
                            self.X = 375
                            self.Y = 198 + self.LIST_SHIP_4 

                ##
                elif self.Y <= 220 + cell.HEIGHT and 400 + cell.HEIGHT:
                    self.X = 375 + self.LIST_SHIP_4  
                    self.Y = 225

                    if self.ROTATE:
                        if self.Y <= 220 + cell.HEIGHT and 400 + cell.HEIGHT:
                            self.X = 375 
                            self.Y = 225 + self.LIST_SHIP_4 + 2
                ##
                elif self.Y <= 245 + cell.HEIGHT and 400 + cell.HEIGHT:
                    self.X = 375 + self.LIST_SHIP_4 + 2 
                    self.Y = 252

                    if self.ROTATE:
                        if self.Y <= 245 + cell.HEIGHT and 400 + cell.HEIGHT:
                            self.X = 375 
                            self.Y = 252 + self.LIST_SHIP_4 + 2
                ##          
                elif self.Y <= 270 + cell.HEIGHT and 400 + cell.HEIGHT:
                    self.X = 375 + self.LIST_SHIP_4 + 2  
                    self.Y = 279
                    
                    if self.ROTATE:
                        if self.Y <= 270 + cell.HEIGHT and 400 + cell.HEIGHT:
                            self.X = 375 
                            self.Y = 279 + self.LIST_SHIP_4 + 2
                ## 
                elif  self.Y <= 295 + cell.HEIGHT and 400 + cell.HEIGHT:
                    self.X = 375 + self.LIST_SHIP_4 + 2  
                    self.Y = 306

                    if self.ROTATE:
                        if self.Y <= 295 + cell.HEIGHT and 400 + cell.HEIGHT:
                            self.X = 375 
                            self.Y = 306 + self.LIST_SHIP_4 + 2
                ##
                elif self.Y <= 320 + cell.HEIGHT and 400 + cell.HEIGHT:
                    self.X = 375 + self.LIST_SHIP_4 + 2  
                    self.Y = 333

                    if self.ROTATE:
                        if self.Y <= 320 + cell.HEIGHT and 400 + cell.HEIGHT:
                            self.X = 375 
                            self.Y = 333 + self.LIST_SHIP_4 + 2
                ##
                elif  self.Y <= 345 + cell.HEIGHT and 400 + cell.HEIGHT:
                    self.X = 375 + self.LIST_SHIP_4 + 2  
                    self.Y = 360
                
                    if self.ROTATE:
                        if self.Y <= 345 + cell.HEIGHT and 400 + cell.HEIGHT:
                            self.X = 375 
                            self.Y = 360 + self.LIST_SHIP_4 + 2
                ##
                elif self.Y <= 370 + cell.HEIGHT and 400 + cell.HEIGHT:
                    self.X = 375 + self.LIST_SHIP_4 + 2 
                    self.Y = 387

                    if self.ROTATE:
                        if self.Y <= 370 + cell.HEIGHT and 400 + cell.HEIGHT:
                            self.X = 375 
                            self.Y = 387 + self.LIST_SHIP_4 + 2
                ##
                elif  self.Y <= 395 + cell.HEIGHT and 400 + cell.HEIGHT:
                    self.X = 375 + self.LIST_SHIP_4 + 2  
                    self.Y = 414  

                    if self.ROTATE:
                        if self.Y <= 395 + cell.HEIGHT and 400 + cell.HEIGHT:
                            self.X = 375 
                            self.Y = 414 + self.LIST_SHIP_4 + 2
                            
            # третя клітинка 
            if self.X >= 400 and self.X <= 400 + cell.WIDTH:
                if self.Y <= 170 + cell.HEIGHT and 425 + cell.HEIGHT:
                    self.X = 400 + self.LIST_SHIP_4 + 4 
                    self.Y = 171

                    if self.ROTATE:
                        if self.Y <= 395 + cell.HEIGHT and 400 + cell.HEIGHT:
                            self.X = 375 
                            self.Y = 414 + self.LIST_SHIP_4 + 2

                # третя клітинка
                elif self.Y <= 195 + cell.HEIGHT and 425 + cell.HEIGHT:
                    self.X = 400 + self.LIST_SHIP_4 + 4
                    self.Y = 198

                elif self.Y <= 220 + cell.HEIGHT and 425 + cell.HEIGHT:
                    self.X = 400 + self.LIST_SHIP_4 + 4 
                    self.Y = 225

                elif self.Y <= 245 + cell.HEIGHT and 425 + cell.HEIGHT:
                    self.X = 400 + self.LIST_SHIP_4 + 4 
                    self.Y = 252

                elif self.Y <= 270 + cell.HEIGHT and 425 + cell.HEIGHT:
                    self.X = 400 + self.LIST_SHIP_4 + 4 
                    self.Y = 279

                elif  self.Y <= 295 + cell.HEIGHT and 425 + cell.HEIGHT:
                    self.X = 400 + self.LIST_SHIP_4 + 4 
                    self.Y = 306

                elif self.Y <= 320 + cell.HEIGHT and 425 + cell.HEIGHT:
                    self.X = 400 + self.LIST_SHIP_4 + 4 
                    self.Y = 333
                    
                elif  self.Y <= 345 + cell.HEIGHT and 425 + cell.HEIGHT:
                    self.X = 400 + self.LIST_SHIP_4 + 4 
                    self.Y = 360
                
                elif self.Y <= 370 + cell.HEIGHT and 425 + cell.HEIGHT:
                    self.X = 400 + self.LIST_SHIP_4 + 4
                    self.Y = 387

                elif  self.Y <= 395 + cell.HEIGHT and 425 + cell.HEIGHT:
                    self.X = 400 + self.LIST_SHIP_4 + 4 
                    self.Y = 414                    
            # четверта клітинка
            if self.X >= 425 and self.X <= 425 + cell.WIDTH:
                if self.Y <= 170 + cell.HEIGHT and 450 + cell.HEIGHT:
                    self.X = 425 + self.LIST_SHIP_4 + 6
                    self.Y = 171

                elif self.Y <= 195 + cell.HEIGHT and 450 + cell.HEIGHT:
                    self.X = 425 + self.LIST_SHIP_4 + 6
                    self.Y = 198

                elif self.Y <= 220 + cell.HEIGHT and 450 + cell.HEIGHT:
                    self.X = 425 + self.LIST_SHIP_4 + 6
                    self.Y = 225

                elif self.Y <= 245 + cell.HEIGHT and 450 + cell.HEIGHT:
                    self.X = 425 + self.LIST_SHIP_4 + 6
                    self.Y = 252

                elif self.Y <= 270 + cell.HEIGHT and 450 + cell.HEIGHT:
                    self.X = 425 + self.LIST_SHIP_4 + 6
                    self.Y = 279

                elif self.Y <= 295 + cell.HEIGHT and 450 + cell.HEIGHT:
                    self.X = 425 + self.LIST_SHIP_4 + 6
                    self.Y = 306

                elif self.Y <= 320 + cell.HEIGHT and 450 + cell.HEIGHT:
                    self.X = 425 + self.LIST_SHIP_4 + 6
                    self.Y = 333
                    
                elif self.Y <= 345 + cell.HEIGHT and 450 + cell.HEIGHT:
                    self.X = 425 + self.LIST_SHIP_4 + 6
                    self.Y = 360
                
                elif self.Y <= 370 + cell.HEIGHT and 450 + cell.HEIGHT:
                    self.X = 425 + self.LIST_SHIP_4 + 6
                    self.Y = 387

                elif  self.Y <= 395 + cell.HEIGHT and 450 + cell.HEIGHT:
                    self.X = 425 + self.LIST_SHIP_4 + 6
                    self.Y = 414
                    

            # пʼята клітинка
            if self.X >= 450 and self.X <= 450 + cell.WIDTH:
                if self.Y <= 170 + cell.HEIGHT and 475 + cell.HEIGHT:
                    self.X = 450 + self.LIST_SHIP_4 + 8
                    self.Y = 171

                elif self.Y <= 195 + cell.HEIGHT and 475 + cell.HEIGHT:
                    self.X = 450 + self.LIST_SHIP_4 + 8 
                    self.Y = 198

                elif self.Y <= 220 + cell.HEIGHT and 475 + cell.HEIGHT:
                    self.X = 450 + self.LIST_SHIP_4 + 8 
                    self.Y = 225

                elif self.Y <= 245 + cell.HEIGHT and 475 + cell.HEIGHT:
                    self.X = 450 + self.LIST_SHIP_4 + 8 
                    self.Y = 252

                elif self.Y <= 270 + cell.HEIGHT and 475 + cell.HEIGHT:
                    self.X = 450 + self.LIST_SHIP_4 + 8 
                    self.Y = 279

                elif  self.Y <= 295 + cell.HEIGHT and 475 + cell.HEIGHT:
                    self.X = 450 + self.LIST_SHIP_4 + 8 
                    self.Y = 306

                elif  self.Y <= 320 + cell.HEIGHT and 475 + cell.HEIGHT:
                    self.X = 450 + self.LIST_SHIP_4 + 8
                    self.Y = 333
                    
                elif  self.Y <= 345 + cell.HEIGHT and 475 + cell.HEIGHT:
                    self.X = 450 + self.LIST_SHIP_4 + 8 
                    self.Y = 360
                
                elif  self.Y <= 370 + cell.HEIGHT and 475 + cell.HEIGHT:
                    self.X = 450 + self.LIST_SHIP_4 + 8 
                    self.Y = 387

                elif  self.Y <= 395 + cell.HEIGHT and 475 + cell.HEIGHT:
                    self.X = 450 + self.LIST_SHIP_4 + 8 
                    self.Y = 414
            # шоста клітинка
            if self.X >= 475 and self.X <= 475 + cell.WIDTH:
                if self.Y <= 170 + cell.HEIGHT and 500 + cell.HEIGHT:
                    self.X = 475 + self.LIST_SHIP_4 + 10
                    self.Y = 171

                if self.ROTATE:
                    if self.Y <= 170 + cell.HEIGHT and 500 + cell.HEIGHT:
                        self.X = 475 
                        self.Y = 171 + self.LIST_SHIP_4

                ##
                elif self.Y <= 195 + cell.HEIGHT and 500 + cell.HEIGHT:
                    self.X = 475 + self.LIST_SHIP_4 + 10 
                    self.Y = 198

                if self.ROTATE:
                    if self.Y <= 195 + cell.HEIGHT and 500 + cell.HEIGHT:
                        self.X = 475 
                        self.Y = 198 + self.LIST_SHIP_4

                ##
                elif self.Y <= 220 + cell.HEIGHT and 500 + cell.HEIGHT:
                    self.X = 475 + self.LIST_SHIP_4 + 10 
                    self.Y = 225

                if self.ROTATE:
                    if self.Y <= 220 + cell.HEIGHT and 500 + cell.HEIGHT:
                        self.X = 475 
                        self.Y = 225 + self.LIST_SHIP_4

                ##
                elif self.Y <= 245 + cell.HEIGHT and 500 + cell.HEIGHT:
                    self.X = 475 + self.LIST_SHIP_4 + 10 
                    self.Y = 252

                if self.ROTATE:
                    if self.Y <= 245 + cell.HEIGHT and 500 + cell.HEIGHT:
                        self.X = 475 
                        self.Y = 252 + self.LIST_SHIP_4

                ##
                elif self.Y <= 270 + cell.HEIGHT and 500 + cell.HEIGHT:
                    self.X = 475 + self.LIST_SHIP_4 + 10 
                    self.Y = 279

                if self.ROTATE:
                    if self.Y <= 270 + cell.HEIGHT and 500 + cell.HEIGHT:
                        self.X = 475 
                        self.Y = 279 + self.LIST_SHIP_4

                ##
                elif  self.Y <= 295 + cell.HEIGHT and 500 + cell.HEIGHT:
                    self.X = 475 + self.LIST_SHIP_4 + 10 
                    self.Y = 306

                if self.ROTATE:
                    if self.Y <= 295 + cell.HEIGHT and 500 + cell.HEIGHT:
                        self.X = 475 
                        self.Y = 306 + self.LIST_SHIP_4

                ##
                elif  self.Y <= 320 + cell.HEIGHT and 500 + cell.HEIGHT:
                    self.X = 475 + self.LIST_SHIP_4 + 10 
                    self.Y = 333

                if self.ROTATE:
                    if self.Y <= 320 + cell.HEIGHT and 500 + cell.HEIGHT:
                        self.X = 475 
                        self.Y = 333 + self.LIST_SHIP_4
                    
                ##
                elif  self.Y <= 345 + cell.HEIGHT and 500 + cell.HEIGHT:
                    self.X = 475 + self.LIST_SHIP_4 + 10 
                    self.Y = 360

                if self.ROTATE:
                    if self.Y <= 345 + cell.HEIGHT and 500 + cell.HEIGHT:
                        self.X = 475 
                        self.Y = 360 + self.LIST_SHIP_4
                
                ##
                elif  self.Y <= 370 + cell.HEIGHT and 500 + cell.HEIGHT:
                    self.X = 475 + self.LIST_SHIP_4 + 10
                    self.Y = 387

                if self.ROTATE:
                    if self.Y <= 370 + cell.HEIGHT and 500 + cell.HEIGHT:
                        self.X = 475 
                        self.Y = 387 + self.LIST_SHIP_4

                ##
                elif  self.Y <= 395 + cell.HEIGHT and 500 + cell.HEIGHT:
                    self.X = 475 + self.LIST_SHIP_4 + 10 
                    self.Y = 414

                if self.ROTATE:
                    if self.Y <= 395 + cell.HEIGHT and 500 + cell.HEIGHT:
                        self.X = 475 
                        self.Y = 414 + self.LIST_SHIP_4

            # сьома клітинка 
            if self.X >= 500 and self.X <= 500 + cell.WIDTH:
                if self.Y <= 170 + cell.HEIGHT and 525 + cell.HEIGHT:
                    self.X = 500 + self.LIST_SHIP_4 + 12
                    self.Y = 171

                if self.ROTATE:
                    if self.Y <= 170 + cell.HEIGHT and 525 + cell.HEIGHT:
                        self.X = 500 
                        self.Y = 171 + self.LIST_SHIP_4
                        
                ##
                elif self.Y <= 195 + cell.HEIGHT and 525 + cell.HEIGHT:
                  self.X = 500 + self.LIST_SHIP_4 + 12
                  self.Y = 198

                if self.ROTATE:
                    if self.Y <= 195 + cell.HEIGHT and 525 + cell.HEIGHT:
                        self.X = 500 
                        self.Y = 198 + self.LIST_SHIP_4

                ##
                elif self.Y <= 220 + cell.HEIGHT and 525 + cell.HEIGHT:
                    self.X = 500 + self.LIST_SHIP_4 + 12
                    self.Y = 225

                if self.ROTATE:
                    if self.Y <= 220 + cell.HEIGHT and 525 + cell.HEIGHT:
                        self.X = 500 
                        self.Y = 225 + self.LIST_SHIP_4

                ##
                elif self.Y <= 245 + cell.HEIGHT and 525 + cell.HEIGHT:
                    self.X = 500 + self.LIST_SHIP_4 + 12
                    self.Y = 252

                if self.ROTATE:
                    if self.Y <= 245 + cell.HEIGHT and 525 + cell.HEIGHT:
                        self.X = 500 
                        self.Y = 252 + self.LIST_SHIP_4

                ##
                elif self.Y <= 270 + cell.HEIGHT and 525 + cell.HEIGHT:
                    self.X = 500 + self.LIST_SHIP_4 + 12
                    self.Y = 279

                if self.ROTATE:
                    if self.Y <= 270 + cell.HEIGHT and 525 + cell.HEIGHT:
                        self.X = 500 
                        self.Y = 279 + self.LIST_SHIP_4

                ##
                elif  self.Y <= 295 + cell.HEIGHT and 525 + cell.HEIGHT:
                    self.X = 500 + self.LIST_SHIP_4 + 12
                    self.Y = 306

                if self.ROTATE:
                    if self.Y <= 295 + cell.HEIGHT and 525 + cell.HEIGHT:
                        self.X = 500 
                        self.Y = 306 + self.LIST_SHIP_4

                ##
                elif  self.Y <= 320 + cell.HEIGHT and 525 + cell.HEIGHT:
                    self.X = 500 + self.LIST_SHIP_4 + 12
                    self.Y = 333

                if self.ROTATE:
                    if self.Y <= 320 + cell.HEIGHT and 525 + cell.HEIGHT:
                        self.X = 500 
                        self.Y = 333 + self.LIST_SHIP_4
                    
                ##
                elif  self.Y <= 345 + cell.HEIGHT and 525 + cell.HEIGHT:
                    self.X = 500 + self.LIST_SHIP_4 + 12
                    self.Y = 360

                if self.ROTATE:
                    if self.Y <= 345 + cell.HEIGHT and 525 + cell.HEIGHT:
                        self.X = 500 
                        self.Y = 360 + self.LIST_SHIP_4
                
                ##
                elif  self.Y <= 370 + cell.HEIGHT and 525 + cell.HEIGHT:
                    self.X = 500 + self.LIST_SHIP_4 + 12
                    self.Y = 387

                if self.ROTATE:
                    if self.Y <= 370 + cell.HEIGHT and 525 + cell.HEIGHT:
                        self.X = 500 
                        self.Y = 387 + self.LIST_SHIP_4

                ##
                elif  self.Y <= 395 + cell.HEIGHT and 525 + cell.HEIGHT:
                    self.X = 500 + self.LIST_SHIP_4 + 12
                    self.Y = 414

                if self.ROTATE:
                    if self.Y <= 395 + cell.HEIGHT and 525 + cell.HEIGHT:
                        self.X = 500 
                        self.Y = 414 + self.LIST_SHIP_4
            

            # восьма клітнка
            if self.X >= 525 and self.X <= 525 + cell.WIDTH:
                if self.Y <= 170 + cell.HEIGHT and 550 + cell.HEIGHT:
                    self.X = 500 + self.LIST_SHIP_4 + 14 
                    self.Y = 171

                if self.ROTATE:
                    if self.Y <= 170 + cell.HEIGHT and 550 + cell.HEIGHT:
                        self.X = 500 
                        self.Y = 171 + self.LIST_SHIP_4
                
                ##
                elif self.Y <= 195 + cell.HEIGHT and 550 + cell.HEIGHT:
                   self.X = 500 + self.LIST_SHIP_4 + 14 
                   self.Y = 198

                if self.ROTATE:
                    if self.Y <= 195 + cell.HEIGHT and 550 + cell.HEIGHT:
                        self.X = 500 
                        self.Y = 198 + self.LIST_SHIP_4
                
                ##
                elif self.Y <= 220 + cell.HEIGHT and 550 + cell.HEIGHT:
                    self.X = 500 + self.LIST_SHIP_4 + 14
                    self.Y = 225

                if self.ROTATE:
                    if self.Y <= 220 + cell.HEIGHT and 550 + cell.HEIGHT:
                        self.X = 500 
                        self.Y = 225 + self.LIST_SHIP_4

                ##
                elif self.Y <= 245 + cell.HEIGHT and 550 + cell.HEIGHT:
                    self.X = 500 + self.LIST_SHIP_4 + 14 
                    self.Y = 252

                if self.ROTATE:
                    if self.Y <= 245 + cell.HEIGHT and 550 + cell.HEIGHT:
                        self.X = 500 
                        self.Y = 252 + self.LIST_SHIP_4
                
                ##
                elif  self.Y <= 270 + cell.HEIGHT and 550 + cell.HEIGHT:
                    self.X = 500 + self.LIST_SHIP_4 + 14 
                    self.Y = 279

                if self.ROTATE:
                    if self.Y <= 270 + cell.HEIGHT and 550 + cell.HEIGHT:
                        self.X = 500 
                        self.Y = 279 + self.LIST_SHIP_4
                
                ##
                elif  self.Y <= 295 + cell.HEIGHT and 550 + cell.HEIGHT:
                    self.X = 500 + self.LIST_SHIP_4 + 14 
                    self.Y = 306

                if self.ROTATE:
                    if self.Y <= 295 + cell.HEIGHT and 550 + cell.HEIGHT:
                        self.X = 500 
                        self.Y = 306 + self.LIST_SHIP_4

                ##
                elif  self.Y <= 320 + cell.HEIGHT and 550 + cell.HEIGHT:
                    self.X = 500 + self.LIST_SHIP_4 + 14 
                    self.Y = 333

                if self.ROTATE:
                    if self.Y <= 320 + cell.HEIGHT and 550 + cell.HEIGHT:
                        self.X = 500 
                        self.Y = 333 + self.LIST_SHIP_4

                ##
                elif self.Y <= 345 + cell.HEIGHT and 550 + cell.HEIGHT:
                    self.X = 500 + self.LIST_SHIP_4 + 14
                    self.Y = 360

                if self.ROTATE:
                    if self.Y <= 345 + cell.HEIGHT and 550 + cell.HEIGHT:
                        self.X = 500 
                        self.Y = 360 + self.LIST_SHIP_4

                ##
                elif  self.Y <= 370 + cell.HEIGHT and 550 + cell.HEIGHT:
                    self.X = 500 + self.LIST_SHIP_4 + 14 
                    self.Y = 387

                if self.ROTATE:
                    if self.Y <= 370 + cell.HEIGHT and 550 + cell.HEIGHT:
                        self.X = 500 
                        self.Y = 387 + self.LIST_SHIP_4

                ##
                elif  self.Y <= 395 + cell.HEIGHT and 550 + cell.HEIGHT:
                    self.X = 500 + self.LIST_SHIP_4 + 14 
                    self.Y = 414

                if self.ROTATE:
                    if self.Y <= 395 + cell.HEIGHT and 550 + cell.HEIGHT:
                        self.X = 500 
                        self.Y = 414 + self.LIST_SHIP_4
            # девʼята клітинка
            if self.X >= 550 and self.X <= 550 + cell.WIDTH:
                if self.Y <= 170 + cell.HEIGHT and 575 + cell.HEIGHT:
                    self.X = 500 + self.LIST_SHIP_4 + 16
                    self.Y = 171

                if self.ROTATE:
                    if self.Y <= 170 + cell.HEIGHT and 575 + cell.HEIGHT:
                        self.X = 500 
                        self.Y = 171 + self.LIST_SHIP_4

                ## 
                elif self.Y <= 195 + cell.HEIGHT and 575 + cell.HEIGHT:
                  self.X = 500 + self.LIST_SHIP_4 + 16
                  self.Y = 198

                if self.ROTATE:
                    if self.Y <= 195 + cell.HEIGHT and 575 + cell.HEIGHT:
                        self.X = 500 
                        self.Y = 198 + self.LIST_SHIP_4
            
                ##
                elif self.Y <= 220 + cell.HEIGHT and 575 + cell.HEIGHT:
                    self.X = 500 + self.LIST_SHIP_4 + 16
                    self.Y = 225

                if self.ROTATE:
                    if self.Y <= 220 + cell.HEIGHT and 575 + cell.HEIGHT:
                        self.X = 500 
                        self.Y = 225 + self.LIST_SHIP_4
                
                ##
                elif self.Y <= 245 + cell.HEIGHT and 575 + cell.HEIGHT:
                    self.X = 500 + self.LIST_SHIP_4 + 16
                    self.Y = 252

                if self.ROTATE:
                    if self.Y <= 245 + cell.HEIGHT and 575 + cell.HEIGHT:
                        self.X = 500 
                        self.Y = 252 + self.LIST_SHIP_4
            
                ##
                elif self.Y <= 270 + cell.HEIGHT and 575 + cell.HEIGHT:
                    self.X = 500 + self.LIST_SHIP_4 + 16
                    self.Y = 279

                if self.ROTATE:
                    if self.Y <= 270 + cell.HEIGHT and 575 + cell.HEIGHT:
                        self.X = 500 
                        self.Y = 279 + self.LIST_SHIP_4
                
                ##
                elif self.Y <= 295 + cell.HEIGHT and 575 + cell.HEIGHT:
                    self.X = 500 + self.LIST_SHIP_4 + 16 
                    self.Y = 306

                if self.ROTATE:
                    if self.Y <= 295 + cell.HEIGHT and 575 + cell.HEIGHT:
                        self.X = 500 
                        self.Y = 306 + self.LIST_SHIP_4

                ##
                elif self.Y <= 320 + cell.HEIGHT and 575 + cell.HEIGHT:
                    self.X = 500 + self.LIST_SHIP_4 + 16 
                    self.Y = 333

                if self.ROTATE:
                    if self.Y <= 320 + cell.HEIGHT and 575 + cell.HEIGHT:
                        self.X = 500 
                        self.Y = 333 + self.LIST_SHIP_4
                     
                ##
                elif  self.Y <= 345 + cell.HEIGHT and 575 + cell.HEIGHT:
                    self.X = 500 + self.LIST_SHIP_4 + 16 
                    self.Y = 360

                if self.ROTATE:
                    if self.Y <= 345 + cell.HEIGHT and 575 + cell.HEIGHT:
                        self.X = 500 
                        self.Y = 360 + self.LIST_SHIP_4 

                ##
                elif  self.Y <= 370 + cell.HEIGHT and 575 + cell.HEIGHT:
                    self.X = 500 + self.LIST_SHIP_4 + 16 
                    self.Y = 387

                if self.ROTATE:
                    if self.Y <= 370 + cell.HEIGHT and 575 + cell.HEIGHT:
                        self.X = 500 
                        self.Y = 387 + self.LIST_SHIP_4 
                
                ##
                elif  self.Y <= 395 + cell.HEIGHT and 575 + cell.HEIGHT:
                    self.X = 500 + self.LIST_SHIP_4 + 16
                    self.Y = 414

                if self.ROTATE:
                    if self.Y <= 395 + cell.HEIGHT and 575 + cell.HEIGHT:
                        self.X = 500 
                        self.Y = 414 + self.LIST_SHIP_4 
            # десята клітинка
            if self.X >= 575 and self.X <= 575 + cell.WIDTH:
                if self.Y <= 170 + cell.HEIGHT and 525 + cell.HEIGHT:
                    self.X = 500 + self.LIST_SHIP_4 + 18 
                    self.Y = 171

                    if self.ROTATE:
                        if self.Y <= 170 + cell.HEIGHT and 525 + cell.HEIGHT:
                            self.X = 500 
                            self.Y = 171 + self.LIST_SHIP_4 
                
                ##
                elif self.Y <= 195 + cell.HEIGHT and 525 + cell.HEIGHT:
                   self.X = 500 + self.LIST_SHIP_4 + 18 
                   self.Y = 198

                if self.ROTATE:
                    if self.Y <= 195 + cell.HEIGHT and 525 + cell.HEIGHT:
                        self.X = 500
                        self.Y = 198 + self.LIST_SHIP_4 
                
                ##
                elif  self.Y <= 220 + cell.HEIGHT and 525 + cell.HEIGHT:
                    self.X = 500 + self.LIST_SHIP_4 + 18 
                    self.Y = 225

                if self.ROTATE:
                    if self.Y <= 220 + cell.HEIGHT and 525 + cell.HEIGHT:
                        self.X = 500 
                        self.Y = 225 + self.LIST_SHIP_4 
                
                ##
                elif  self.Y <= 245 + cell.HEIGHT and 525 + cell.HEIGHT:
                    self.X = 500 + self.LIST_SHIP_4 + 18 
                    self.Y = 252

                if self.ROTATE:
                    if  self.Y <= 245 + cell.HEIGHT and 525 + cell.HEIGHT:
                        self.X = 500
                        self.Y = 252 + self.LIST_SHIP_4 
                    
                ##
                elif  self.Y <= 270 + cell.HEIGHT and 525 + cell.HEIGHT:
                    self.X = 500 + self.LIST_SHIP_4 + 18 
                    self.Y = 279

                if self.ROTATE:
                    if  self.Y <= 270 + cell.HEIGHT and 525 + cell.HEIGHT:
                        self.X = 500 
                        self.Y = 279 + self.LIST_SHIP_4 

                ##
                elif  self.Y <= 295 + cell.HEIGHT and 525 + cell.HEIGHT:
                    self.X = 500 + self.LIST_SHIP_4 + 18 
                    self.Y = 306

                if self.ROTATE:
                    if  self.Y <= 295 + cell.HEIGHT and 525 + cell.HEIGHT:
                        self.X = 500
                        self.Y = 306 + self.LIST_SHIP_4 

                ##  
                elif  self.Y <= 320 + cell.HEIGHT and 525 + cell.HEIGHT:
                    self.X = 500 + self.LIST_SHIP_4 + 18 
                    self.Y = 333

                if self.ROTATE:
                    if self.Y <= 320 + cell.HEIGHT and 525 + cell.HEIGHT:
                        self.X = 500 
                        self.Y = 333 + self.LIST_SHIP_4 

                ##
                elif self.Y <= 345 + cell.HEIGHT and 525 + cell.HEIGHT:
                    self.X = 500 + self.LIST_SHIP_4 + 18 
                    self.Y = 360

                if self.ROTATE:
                    if self.Y <= 345 + cell.HEIGHT and 525 + cell.HEIGHT:
                        self.X = 500 
                        self.Y = 360 + self.LIST_SHIP_4 

                ##
                elif self.Y <= 370 + cell.HEIGHT and 525 + cell.HEIGHT:
                    self.X = 500 + self.LIST_SHIP_4 + 18 
                    self.Y = 387
                    
                if self.ROTATE:
                    if self.Y <= 370 + cell.HEIGHT and 525 + cell.HEIGHT:
                        self.X = 500
                        self.Y = 387 + self.LIST_SHIP_4 

                ##    
                elif self.Y <= 395 + cell.HEIGHT and 525 + cell.HEIGHT:
                    self.X = 500 + self.LIST_SHIP_4 + 18 
                    self.Y = 414
                    
                if self.ROTATE:
                    if self.Y <= 395 + cell.HEIGHT and 525 + cell.HEIGHT:
                        self.X = 500 
                        self.Y = 414 + self.LIST_SHIP_4 
                            

                            
    def vertical_turn(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] == True:
            self.load_image(check_img= False)
            self.ROTATE = True
            #self.X = 350 + 1
            #self.Y = 176

    def horizontal_turn(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] == True:
            if self.ROTATE == True:
                self.load_image(check_img= True) 
                self.ROTATE = False

ship_4 = Ship_4()

# 3
ship_3_1 = Ship_4(width1= 75, list_ship_4= m_data.list_x[2], y1= 180, name1= 'img/ship/ship_3.png')
ship_3_2 = Ship_4(width1= 75, list_ship_4= m_data.list_x[2], y1= 230, name1= 'img/ship/ship_3.png')

# 2
ship_2_1 = Ship_4(width1= 50, list_ship_4= m_data.list_x[1], y1= 180, name1= 'img/ship/ship_2.png')
ship_2_2 = Ship_4(width1= 50, list_ship_4= m_data.list_x[1], y1= 230, name1= 'img/ship/ship_2.png')
ship_2_3 = Ship_4(width1= 50, list_ship_4= m_data.list_x[1], y1= 280, name1= 'img/ship/ship_2.png')

# 1
ship_1_1 = Ship_4(width1= 25, list_ship_4= m_data.list_x[0], y1= 180, name1= 'img/ship/ship_1.png')
ship_1_2 = Ship_4(width1= 25, list_ship_4= m_data.list_x[0], y1= 230, name1= 'img/ship/ship_1.png')
ship_1_3 = Ship_4(width1= 25, list_ship_4= m_data.list_x[0], y1= 280, name1= 'img/ship/ship_1.png')
ship_1_4 = Ship_4(width1= 25, list_ship_4= m_data.list_x[0], y1= 330, name1= 'img/ship/ship_1.png')


#   def vertical_turn(self):
#       keys = pygame.key.get_pressed()
#       if keys[pygame.K_RIGHT] == True:
#           self.load_image(check_img= False) 

#   def horizontal_turn(self):
#       keys = pygame.key.get_pressed()
#       if keys[pygame.K_LEFT] == True:
#           self.load_image(check_img= 10) 

#
#ifself.LIST_SHIP_4y == m_data.list_x[2] or self.LIST_SHIP_4 == m_data.list_x[1] or self.LIST_SHIP_4 == m_data.list_x[0]:
#    self.X = 525 + self.LIST_SHIP_4 + 14 
#    self.Y = 171
# cell.HEIGHT + cell.WIDTH
