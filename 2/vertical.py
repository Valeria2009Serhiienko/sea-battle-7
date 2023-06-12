'''import pygame
import modules.main_modules.settings as m_settings
import modules.main_modules.data_base as m_data

def collision_horizontal(self):
    for cell in m_data.list_cells:
        if self.X >= 350 and self.X <= 350 + cell.WIDTH:
            if self.Y <= 170 + cell.HEIGHT and 375 + cell.HEIGHT and self.ROTATE == True:
                self.X = 350 
                self.Y = 171 + self.LIST_SHIP_4 
                
            elif self.Y <= 195 + cell.HEIGHT and 375 + cell.HEIGHT and self.ROTATE == True:
                self.X = 350 
                self.Y = 198 + self.LIST_SHIP_4 
                 
            elif self.Y <= 220 + cell.HEIGHT and 375 + cell.HEIGHT and self.ROTATE == True:
                self.X = 350 
                self.Y = 225 + self.LIST_SHIP_4

            elif self.Y <= 245 + cell.HEIGHT and 375 + cell.HEIGHT and self.ROTATE == True:
                self.X = 350 
                self.Y = 252 + self.LIST_SHIP_4
                self.rotate(range_Y_1= 245, range_Y_2= 375, number_X= 351, number_Y= 252)
                
            elif self.Y <= 270 + cell.HEIGHT and 375 + cell.HEIGHT and self.ROTATE == True:
                self.X = 350
                self.Y = 279  + self.LIST_SHIP_4
                self.rotate(range_Y_1= 270, range_Y_2= 375, number_X= 351, number_Y= 279)
            elif self.Y <= 295 + cell.HEIGHT and 375 + cell.HEIGHT and self.ROTATE == True:
                self.X = 350 
                self.Y = 306+ self.LIST_SHIP_4
                        
                self.rotate(range_Y_1= 295, range_Y_2= 375, number_X= 351, number_Y= 306)
            elif self.Y <= 320 + cell.HEIGHT and 375 + cell.HEIGHT and self.ROTATE == True:
                self.X = 350
                self.Y = 333 + self.LIST_SHIP_4
                        
                self.rotate(range_Y_1= 320, range_Y_2= 375, number_X= 351, number_Y= 333)
                
            elif  self.Y <= 345 + cell.HEIGHT and 375 + cell.HEIGHT and self.ROTATE == True:
                self.X = 350 
                self.Y = 333+ self.LIST_SHIP_4
                self.rotate(range_Y_1= 345, range_Y_2= 375, number_X= 351, number_Y= 333)
                        
            elif  self.Y <= 370 + cell.HEIGHT and 375 + cell.HEIGHT and self.ROTATE == True:
                self.X = 350
                self.Y = 387 + self.LIST_SHIP_4
                self.rotate(range_Y_1= 370, range_Y_2= 375, number_X= 351, number_Y= 333)
                        
            elif  self.Y <= 395 + cell.HEIGHT and 375 + cell.HEIGHT and self.ROTATE == True:
                self.X = 350
                self.Y = 414 + self.LIST_SHIP_4
                self.rotate(range_Y_1= 395, range_Y_2= 375, number_X= 351, number_Y= 333)
        # друга клітинка 
        if self.X >= 375 and self.X <= 375 + cell.WIDTH:
            if self.Y <= 170 + cell.HEIGHT and 400 + cell.HEIGHT and self.ROTATE == True:
                self.X = 375 
                self.Y = 171 + self.LIST_SHIP_4 + 2
                self.rotate(range_Y_1= 170, range_Y_2= 400, number_X= 375, number_Y= 171)
            ##
            elif self.Y <= 195 + cell.HEIGHT and 400 + cell.HEIGHT and self.ROTATE == True:
                self.X = 375 
                self.Y = 198 + self.LIST_SHIP_4
                self.rotate(range_Y_1= 195, range_Y_2= 400, number_X= 375, number_Y= 198)
            ##
            elif self.Y <= 220 + cell.HEIGHT and 400 + cell.HEIGHT and self.ROTATE == True:
                self.X = 375  
                self.Y = 225 + self.LIST_SHIP_4
                self.rotate(range_Y_1= 220, range_Y_2= 400, number_X= 375, number_Y= 225)
            ##
            elif self.Y <= 245 + cell.HEIGHT and 400 + cell.HEIGHT and self.ROTATE == True:
                self.X = 375
                self.Y = 252 + self.LIST_SHIP_4 + 2 
                self.rotate(range_Y_1= 245, range_Y_2= 400, number_X= 375, number_Y= 252)
            ##          
            elif self.Y <= 270 + cell.HEIGHT and 400 + cell.HEIGHT and self.ROTATE == True:
                self.X = 375  
                self.Y = 279 + self.LIST_SHIP_4 + 2 
                self.rotate(range_Y_1= 270, range_Y_2= 400, number_X= 375, number_Y= 279)
            ## 
            elif  self.Y <= 295 + cell.HEIGHT and 400 + cell.HEIGHT and self.ROTATE == True:
                self.X = 375  
                self.Y = 306 + self.LIST_SHIP_4 + 2
                self.rotate(range_Y_1= 295, range_Y_2= 400, number_X= 375, number_Y= 306)
            ##
            elif self.Y <= 320 + cell.HEIGHT and 400 + cell.HEIGHT and self.ROTATE == True:
                self.X = 375  
                self.Y = 333 + self.LIST_SHIP_4 + 2
                self.rotate(range_Y_1= 320, range_Y_2= 400, number_X= 375, number_Y= 333)
            ##
            elif  self.Y <= 345 + cell.HEIGHT and 400 + cell.HEIGHT and self.ROTATE == True:
                self.X = 375  
                self.Y = 360 + self.LIST_SHIP_4 + 2
                self.rotate(range_Y_1= 345, range_Y_2= 400, number_X= 375, number_Y= 333)
            ##
            elif self.Y <= 370 + cell.HEIGHT and 400 + cell.HEIGHT and self.ROTATE == True:
                self.X = 375 
                self.Y = 387 + self.LIST_SHIP_4 + 2
                self.rotate(range_Y_1= 370, range_Y_2= 400, number_X= 375, number_Y= 333)
            ##
            elif  self.Y <= 395 + cell.HEIGHT and 400 + cell.HEIGHT and self.ROTATE == True:
                self.X = 375  
                self.Y = 414  + self.LIST_SHIP_4 + 2
                
                self.rotate(range_Y_1= 395, range_Y_2= 400, number_X= 375, number_Y= 333)
        # третя клітинка 
        if self.X >= 400 and self.X <= 400 + cell.WIDTH:
            if self.Y <= 170 + cell.HEIGHT and 425 + cell.HEIGHT and self.ROTATE == True:
                self.X = 400 
                self.Y = 171 + self.LIST_SHIP_4 + 4
                        
                self.rotate(range_Y_1= 170, range_Y_2= 425, number_X= 400, number_Y= 171)
                
            # третя клітинка
            elif self.Y <= 195 + cell.HEIGHT and 425 + cell.HEIGHT and self.ROTATE == True:
                self.X = 400
                self.Y = 198 + self.LIST_SHIP_4 + 4
                self.rotate(range_Y_1= 195, range_Y_2= 425, number_X= 400, number_Y= 198)
            elif self.Y <= 220 + cell.HEIGHT and 425 + cell.HEIGHT and self.ROTATE == True:
                self.X = 400 
                self.Y = 225 + self.LIST_SHIP_4 + 4
                self.rotate(range_Y_1= 220, range_Y_2= 425, number_X= 400, number_Y= 225)
            elif self.Y <= 245 + cell.HEIGHT and 425 + cell.HEIGHT and self.ROTATE == True:
                self.X = 400 
                self.Y = 252 + self.LIST_SHIP_4 + 4
                self.rotate(range_Y_1= 245, range_Y_2= 425, number_X= 400, number_Y= 252)
            elif self.Y <= 270 + cell.HEIGHT and 425 + cell.HEIGHT and self.ROTATE == True:
                self.X = 400 
                self.Y = 279 + self.LIST_SHIP_4 + 4 
                self.rotate(range_Y_1= 270, range_Y_2= 425, number_X= 400, number_Y= 279)
            elif  self.Y <= 295 + cell.HEIGHT and 425 + cell.HEIGHT and self.ROTATE == True:
                self.X = 400 
                self.Y = 306 + self.LIST_SHIP_4 + 4
                
                self.rotate(range_Y_1= 295, range_Y_2= 425, number_X= 400, number_Y= 306)
            elif self.Y <= 320 + cell.HEIGHT and 425 + cell.HEIGHT and self.ROTATE == True:
                self.X = 400 
                self.Y = 333 + self.LIST_SHIP_4 + 4
                self.rotate(range_Y_1= 320, range_Y_2= 425, number_X= 400, number_Y= 333)
                
            elif  self.Y <= 345 + cell.HEIGHT and 425 + cell.HEIGHT:
                self.X = 400 
                self.Y = 360 + self.LIST_SHIP_4 + 4
            
                self.rotate(range_Y_1= 345, range_Y_2= 425, number_X= 400, number_Y= 333)
            elif self.Y <= 370 + cell.HEIGHT and 425 + cell.HEIGHT and self.ROTATE == True:
                self.X 
                self.Y = 387+ self.LIST_SHIP_4 + 4

                
                self.rotate(range_Y_1= 370, range_Y_2= 425, number_X= 400, number_Y= 333)
            elif  self.Y <= 395 + cell.HEIGHT and 425 + cell.HEIGHT and self.ROTATE == True:
                self.X = 400 
                self.Y = 414  + self.LIST_SHIP_4 + 4
                
                self.rotate(range_Y_1= 395, range_Y_2= 425, number_X= 400, number_Y= 333)       
        # четверта клітинка
        if self.X >= 425 and self.X <= 425 + cell.WIDTH:
            if self.Y <= 170 + cell.HEIGHT and 450 + cell.HEIGHT and self.ROTATE == True:
                self.X = 425
                self.Y = 171 + self.LIST_SHIP_4 + 6
                self.rotate(range_Y_1= 170, range_Y_2= 450, number_X= 425, number_Y= 171)
            elif self.Y <= 195 + cell.HEIGHT and 450 + cell.HEIGHT and self.ROTATE == True:
                self.X = 425
                self.Y = 198 + self.LIST_SHIP_4 + 6
                self.rotate(range_Y_1= 195, range_Y_2= 450, number_X= 425, number_Y= 198)
            elif self.Y <= 220 + cell.HEIGHT and 450 + cell.HEIGHT and self.ROTATE == True:
                self.X = 425
                self.Y = 225 + self.LIST_SHIP_4 + 6
                self.rotate(range_Y_1= 220, range_Y_2= 450, number_X= 425, number_Y= 225)
            elif self.Y <= 245 + cell.HEIGHT and 450 + cell.HEIGHT and self.ROTATE == True:
                self.X = 425
                self.Y = 252 + self.LIST_SHIP_4 + 6
                self.rotate(range_Y_1= 245, range_Y_2= 450, number_X= 425, number_Y= 252)
            elif self.Y <= 270 + cell.HEIGHT and 450 + cell.HEIGHT and self.ROTATE == True:
                self.X = 425
                self.Y = 279 + self.LIST_SHIP_4 + 6
                self.rotate(range_Y_1= 270, range_Y_2= 450, number_X= 425, number_Y= 279)
            elif self.Y <= 295 + cell.HEIGHT and 450 + cell.HEIGHT and self.ROTATE == True:
                self.X = 425
                self.Y = 306 + self.LIST_SHIP_4 + 6
                
                self.rotate(range_Y_1= 295, range_Y_2= 450, number_X= 425, number_Y= 306)
            elif self.Y <= 320 + cell.HEIGHT and 450 + cell.HEIGHT and self.ROTATE == True:
                self.X = 425 
                self.Y = 333 + self.LIST_SHIP_4 + 6
                self.rotate(320, 450, 425, 333)
                
            elif self.Y <= 345 + cell.HEIGHT and 450 + cell.HEIGHT and self.ROTATE == True:
                self.X = 425
                self.Y = 360 + self.LIST_SHIP_4 + 6
                self.rotate(345, 450, 425, 333)
            
            elif self.Y <= 370 + cell.HEIGHT and 450 + cell.HEIGHT and self.ROTATE == True:
                self.X = 425
                self.Y = 387 + self.LIST_SHIP_4 + 6
                self.rotate(370, 450, 425, 387)
            elif  self.Y <= 395 + cell.HEIGHT and 450 + cell.HEIGHT and self.ROTATE == True:
                self.X = 425
                self.Y = 414 + self.LIST_SHIP_4 + 6
                self.rotate(395, 450, 425, 333)
                
        # пʼята клітинка
        if self.X >= 450 and self.X <= 450 + cell.WIDTH:
            if self.Y <= 170 + cell.HEIGHT and 475 + cell.HEIGHT and self.ROTATE == True:
                self.X = 450 
                self.Y = 171 + self.LIST_SHIP_4 + 8
                self.rotate(170, 475, 450, 171)
            elif self.Y <= 195 + cell.HEIGHT and 475 + cell.HEIGHT and self.ROTATE == True:
                self.X = 450  
                self.Y = 198 + self.LIST_SHIP_4 + 8
                self.rotate(195, 475, 450, 198)
            elif self.Y <= 220 + cell.HEIGHT and 475 + cell.HEIGHT and self.ROTATE == True:
                self.X = 450
                self.Y = 225  + self.LIST_SHIP_4 + 8
                self.rotate(220, 475, 450, 225)
            elif self.Y <= 245 + cell.HEIGHT and 475 + cell.HEIGHT and self.ROTATE == True:
                self.X = 450 
                self.Y = 252 + self.LIST_SHIP_4 + 8 
                self.rotate(245, 475, 450, 252)
            elif self.Y <= 270 + cell.HEIGHT and 475 + cell.HEIGHT and self.ROTATE == True:
                self.X = 450  
                self.Y = 279+ self.LIST_SHIP_4 + 8
                self.rotate(270, 475, 450, 279)
            elif  self.Y <= 295 + cell.HEIGHT and 475 + cell.HEIGHT and self.ROTATE == True:
                self.X = 450 
                self.Y = 306 + self.LIST_SHIP_4 + 8
                self.rotate(295, 475, 450, 306)
            elif  self.Y <= 320 + cell.HEIGHT and 475 + cell.HEIGHT and self.ROTATE == True:
                self.X = 450
                self.Y = 333 + self.LIST_SHIP_4 + 8
                
                self.rotate(325, 475, 450, 333)
            elif  self.Y <= 345 + cell.HEIGHT and 475 + cell.HEIGHT and self.ROTATE == True:
                self.X = 450 
                self.Y = 360 + self.LIST_SHIP_4 + 8
                self.rotate(345, 475, 450, 333)
            
            elif  self.Y <= 370 + cell.HEIGHT and 475 + cell.HEIGHT and self.ROTATE == True:
                self.X = 450 
                self.Y = 387 + self.LIST_SHIP_4 + 8
                self.rotate(375, 475, 450, 333)
            elif  self.Y <= 395 + cell.HEIGHT and 475 + cell.HEIGHT and self.ROTATE == True:
                self.X = 450 
                self.Y = 414 + self.LIST_SHIP_4 + 8
                self.rotate(395, 475, 450, 333)
        # шоста клітинка
        if self.X >= 475 and self.X <= 475 + cell.WIDTH:
            if self.Y <= 170 + cell.HEIGHT and 500 + cell.HEIGHT and self.ROTATE == True:
                self.X = 475 
                self.Y = 171 + self.LIST_SHIP_4 + 10
                self.rotate(170, 500, 475, 171)
            ##
            elif self.Y <= 195 + cell.HEIGHT and 500 + cell.HEIGHT and self.ROTATE == True:
                self.X = 475  
                self.Y = 198 + self.LIST_SHIP_4 + 10
                self.rotate(195, 500, 475, 198)
            ##
            elif self.Y <= 220 + cell.HEIGHT and 500 + cell.HEIGHT and self.ROTATE == True:
                self.X = 475 
                self.Y = 225 + self.LIST_SHIP_4 + 10
                self.rotate(220, 500, 475, 225)
            ##
            elif self.Y <= 245 + cell.HEIGHT and 500 + cell.HEIGHT:
                self.X = 475 + self.LIST_SHIP_4 + 10 
                self.Y = 252
                self.rotate(245, 500, 475, 252)
            ##
            elif self.Y <= 270 + cell.HEIGHT and 500 + cell.HEIGHT:
                self.X = 475 + self.LIST_SHIP_4 + 10 
                self.Y = 279
                self.rotate(270, 500, 475, 279)
            ##
            elif  self.Y <= 295 + cell.HEIGHT and 500 + cell.HEIGHT:
                self.X = 475 + self.LIST_SHIP_4 + 10 
                self.Y = 306
                self.rotate(395, 500, 475, 306)
            ##
            elif  self.Y <= 320 + cell.HEIGHT and 500 + cell.HEIGHT:
                self.X = 475 + self.LIST_SHIP_4 + 10 
                self.Y = 333
                self.rotate(320, 500, 475, 333)
            ##
            elif  self.Y <= 345 + cell.HEIGHT and 500 + cell.HEIGHT:
                self.X = 475 + self.LIST_SHIP_4 + 10 
                self.Y = 360
                self.rotate(345, 500, 475, 333)
            
            
            ##
            elif  self.Y <= 370 + cell.HEIGHT and 500 + cell.HEIGHT:
                self.X = 475 + self.LIST_SHIP_4 + 10
                self.Y = 387
                self.rotate(370, 500, 475, 333)
            ##
            elif  self.Y <= 395 + cell.HEIGHT and 500 + cell.HEIGHT:
                self.X = 475 + self.LIST_SHIP_4 + 10 
                self.Y = 414
                self.rotate(395, 500, 475, 333)
        # сьома клітинка 
        if self.X >= 500 and self.X <= 500 + cell.WIDTH:
            if self.Y <= 170 + cell.HEIGHT and 525 + cell.HEIGHT:
                self.X = 500 + self.LIST_SHIP_4 + 12
                self.Y = 171
                self.rotate(170, 525, 500, 171)
                    
            ##
            elif self.Y <= 195 + cell.HEIGHT and 525 + cell.HEIGHT:
                self.X = 500 + self.LIST_SHIP_4 + 12
                self.Y = 198
                self.rotate(195, 525, 500, 198)
            ##
            elif self.Y <= 220 + cell.HEIGHT and 525 + cell.HEIGHT:
                self.X = 500 + self.LIST_SHIP_4 + 12
                self.Y = 225
                self.rotate(220, 525, 500, 225)
            ##
            elif self.Y <= 245 + cell.HEIGHT and 525 + cell.HEIGHT:
                self.X = 500 + self.LIST_SHIP_4 + 12
                self.Y = 252
                self.rotate(245, 525, 500, 252)
            ##
            elif self.Y <= 270 + cell.HEIGHT and 525 + cell.HEIGHT:
                self.X = 500 + self.LIST_SHIP_4 + 12
                self.Y = 279
                self.rotate(270, 525, 500, 279)
            ##
            elif  self.Y <= 295 + cell.HEIGHT and 525 + cell.HEIGHT:
                self.X = 500 + self.LIST_SHIP_4 + 12
                self.Y = 306
                self.rotate(295, 525, 500, 306)
            ##
            elif  self.Y <= 320 + cell.HEIGHT and 525 + cell.HEIGHT:
                self.X = 500 + self.LIST_SHIP_4 + 12
                self.Y = 333
                self.rotate(320, 525, 500, 333)
                
            ##
            elif  self.Y <= 345 + cell.HEIGHT and 525 + cell.HEIGHT:
                self.X = 500 + self.LIST_SHIP_4 + 12
                self.Y = 360
                self.rotate(345, 525, 500, 333)
            
            ##
            elif  self.Y <= 370 + cell.HEIGHT and 525 + cell.HEIGHT:
                self.X = 500 + self.LIST_SHIP_4 + 12
                self.Y = 387
                self.rotate(370, 525, 500, 333)
            ##
            elif  self.Y <= 395 + cell.HEIGHT and 525 + cell.HEIGHT:
                self.X = 500 + self.LIST_SHIP_4 + 12
                self.Y = 414
                self.rotate(395, 525, 500, 333)
        # восьма клітнка
        if self.X >= 525 and self.X <= 525 + cell.WIDTH:
            if self.Y <= 170 + cell.HEIGHT and 550 + cell.HEIGHT:
                self.X = 500 + self.LIST_SHIP_4 + 14 
                self.Y = 171
                self.rotate(170, 550, 500, 171)
            
            ##
            elif self.Y <= 195 + cell.HEIGHT and 550 + cell.HEIGHT:
                self.X = 500 + self.LIST_SHIP_4 + 14 
                self.Y = 198
                self.rotate(195, 550, 500, 198)
            
            ##
            elif self.Y <= 220 + cell.HEIGHT and 550 + cell.HEIGHT:
                self.X = 500 + self.LIST_SHIP_4 + 14
                self.Y = 225
                self.rotate(220, 550, 500, 225)
            ##
            elif self.Y <= 245 + cell.HEIGHT and 550 + cell.HEIGHT:
                self.X = 500 + self.LIST_SHIP_4 + 14 
                self.Y = 252
                self.rotate(245, 550, 500, 252)
            
            ##
            elif  self.Y <= 270 + cell.HEIGHT and 550 + cell.HEIGHT:
                self.X = 500 + self.LIST_SHIP_4 + 14 
                self.Y = 279
                self.rotate(270, 550, 500, 279)
            
            ##
            elif  self.Y <= 295 + cell.HEIGHT and 550 + cell.HEIGHT:
                self.X = 500 + self.LIST_SHIP_4 + 14 
                self.Y = 306
                self.rotate(295, 550, 500, 306)
                    
            ##
            elif  self.Y <= 320 + cell.HEIGHT and 550 + cell.HEIGHT:
                self.X = 500 + self.LIST_SHIP_4 + 14 
                self.Y = 333
                self.rotate(320, 550, 500, 333)
            ##
            elif self.Y <= 345 + cell.HEIGHT and 550 + cell.HEIGHT:
                self.X = 500 + self.LIST_SHIP_4 + 14
                self.Y = 360
                self.rotate(345, 550, 500, 333)
            ##
            elif self.Y <= 370 + cell.HEIGHT and 550 + cell.HEIGHT:
                self.X = 500 + self.LIST_SHIP_4 + 14 
                self.Y = 387
                self.rotate(370, 550, 500, 333)
            ##
            elif self.Y <= 395 + cell.HEIGHT and 550 + cell.HEIGHT:
                self.X = 500 + self.LIST_SHIP_4 + 14 
                self.Y = 414
                self.rotate(395, 550, 500, 333)
        # девʼята клітинка
        if self.X >= 550 and self.X <= 550 + cell.WIDTH:
            if self.Y <= 170 + cell.HEIGHT and 575 + cell.HEIGHT:
                self.X = 500 + self.LIST_SHIP_4 + 16
                self.Y = 171
                self.rotate(170, 575, 500, 171)
            ## 
            elif self.Y <= 195 + cell.HEIGHT and 575 + cell.HEIGHT:
                self.X = 500 + self.LIST_SHIP_4 + 16
                self.Y = 198
                self.rotate(195, 575, 500, 198) 
        
            ##
            elif self.Y <= 220 + cell.HEIGHT and 575 + cell.HEIGHT:
                self.X = 500 + self.LIST_SHIP_4 + 16
                self.Y = 225
                self.rotate(220, 575, 500, 225)
            
            ##
            elif self.Y <= 245 + cell.HEIGHT and 575 + cell.HEIGHT:
                self.X = 500 + self.LIST_SHIP_4 + 16
                self.Y = 252
                self.rotate(245, 575, 500, 252)
        
            ##
            elif self.Y <= 270 + cell.HEIGHT and 575 + cell.HEIGHT:
                self.X = 500 + self.LIST_SHIP_4 + 16
                self.Y = 279
                self.rotate(270, 575, 500, 279)
            
            ##
            elif self.Y <= 295 + cell.HEIGHT and 575 + cell.HEIGHT:
                self.X = 500 + self.LIST_SHIP_4 + 16 
                self.Y = 306
                self.rotate(295, 575, 500, 306)
            ##
            elif self.Y <= 320 + cell.HEIGHT and 575 + cell.HEIGHT:
                self.X = 500 + self.LIST_SHIP_4 + 16 
                self.Y = 333
                
                self.rotate(320, 575, 500, 333)
                 
            ##
            elif  self.Y <= 345 + cell.HEIGHT and 575 + cell.HEIGHT:
                self.X = 500 + self.LIST_SHIP_4 + 16 
                self.Y = 360
                self.rotate(345, 575, 500, 333)
            ##
            elif  self.Y <= 370 + cell.HEIGHT and 575 + cell.HEIGHT:
                self.X = 500 + self.LIST_SHIP_4 + 16 
                self.Y = 387
                self.rotate(370, 575, 500, 333)
            
            ##
            elif  self.Y <= 395 + cell.HEIGHT and 575 + cell.HEIGHT:
                self.X = 500 + self.LIST_SHIP_4 + 16
                self.Y = 414
                self.rotate(395, 575, 500, 333)
        # десята клітинка
        if self.X >= 575 and self.X <= 575 + cell.WIDTH:                
            if self.Y <= 170 + cell.HEIGHT and 600 + cell.HEIGHT:
                self.X = 500 + self.LIST_SHIP_4 + 18 
                self.Y = 171
                self.rotate(170, 525, 500, 171)
            ##
            elif self.Y <= 195 + cell.HEIGHT and 600 + cell.HEIGHT:
               self.X = 500 + self.LIST_SHIP_4 + 18 
               self.Y = 198
               self.rotate(195, 525, 500, 198)
            ##
            elif  self.Y <= 220 + cell.HEIGHT and 600 + cell.HEIGHT:
                self.X = 500 + self.LIST_SHIP_4 + 18 
                self.Y = 225
            
                self.rotate(220, 525, 500, 225)
            ##
            elif  self.Y <= 245 + cell.HEIGHT and 600 + cell.HEIGHT:
                self.X = 500 + self.LIST_SHIP_4 + 18 
                self.Y = 252
                self.rotate(245, 525, 500, 252)
            ##
            elif  self.Y <= 270 + cell.HEIGHT and 600 + cell.HEIGHT:
                self.X = 500 + self.LIST_SHIP_4 + 18 
                self.Y = 279
            if self.ROTATE:
                if  self.Y <= 270 + cell.HEIGHT and 600 + cell.HEIGHT:
                    self.X = 500 
                    self.Y = 279 + self.LIST_SHIP_4 
                self.rotate(295, 525, 500, 306)
            ##
            elif  self.Y <= 295 + cell.HEIGHT and 600 + cell.HEIGHT:
                self.X = 500 + self.LIST_SHIP_4 + 18 
                self.Y = 306
                
                self.rotate(295, 525, 500, 306)
            ##  
            elif  self.Y <= 320 + cell.HEIGHT and 600 + cell.HEIGHT:
                self.X = 500 + self.LIST_SHIP_4 + 18 
                self.Y = 333
                self.rotate(320, 525, 500, 333)
            ##
            elif self.Y <= 345 + cell.HEIGHT and 600 + cell.HEIGHT:
                self.X = 500 + self.LIST_SHIP_4 + 18 
                self.Y = 360
                self.rotate(345, 525, 500, 333)
            ##
            elif self.Y <= 370 + cell.HEIGHT and 600 + cell.HEIGHT:
                self.X = 500 + self.LIST_SHIP_4 + 18 
                self.Y = 387
                
                self.rotate(370, 525, 500, 333)
            ##    
            elif self.Y <= 395 + cell.HEIGHT and 600 + cell.HEIGHT:
                self.X = 500 + self.LIST_SHIP_4 + 18 
                self.Y = 414
                        
                self.rotate(395, 525, 500, 333)
              '''          