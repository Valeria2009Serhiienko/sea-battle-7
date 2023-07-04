import pygame
import modules.main_modules.data_base as m_data
import modules.blit_el_ship.ship_4_blit as m_ship
import random
pygame.init()

class Bot(m_ship.Ship_4):
    def __init__(self, width3= 0, height3= 0, x3 = 480, y3 = 180, size_ship_bot = None):
        m_ship.Ship_4.__init__(self, width1= width3, height1= height3, x1 = x3, y1 = y3, size_ship= size_ship_bot)
        self.RANDOM_NUMBER = 0
        self.COUNT = True
        self.SIZE_SHIP_BOT = size_ship_bot



    def who_turn(self):
        if m_data.step[0] == 'player':
            pass
        elif m_data.step[0] == 'bot':
            pass
    
    def set_ship_bot(self):

        random_index = random.randint(0, 6)
        random_col = random.randint(0, 6)

        if self.SIZE_SHIP_BOT == 3:
            random_index = random.randint(0, 7)
            random_col = random.randint(0, 7)
#
        if self.SIZE_SHIP_BOT == 2:
            random_index = random.randint(0, 8)
            random_col = random.randint(0, 8)   

        if self.SIZE_SHIP_BOT == 1:
            random_index = random.randint(0, 9)
            random_col = random.randint(0, 9)
                
        for i in m_data.set_ship:
            if random_col == 0:
                if random_index == 0:
                    if m_data.list_map_bot[0][0] == 0:
                        self.X = 545 + self.LIST_SHIP_4 
                        self.Y = 171
                        m_ship.ship_4.set_ship(set_row= 0, set_cell_start= 0, set_list= m_data.list_map_bot)

                        if self.SIZE_SHIP_BOT == 3:
                            m_ship.ship_3_1.set_ship(set_row= 0, set_cell_start= 0, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 2:
                            m_ship.ship_2_1.set_ship(set_row= 0, set_cell_start= 0, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 1:
                            m_ship.ship_1_1.set_ship(set_row= 0, set_cell_start= 0, set_list= m_data.list_map_bot)

                if random_index == 1:
                    if m_data.list_map_bot[0][1] == 0:
                        self.X = 570 + self.LIST_SHIP_4 
                        self.Y = 171
                        m_ship.ship_4.set_ship(set_row= 0, set_cell_start= 1, set_list= m_data.list_map_bot)

                        if self.SIZE_SHIP_BOT == 3:
                            m_ship.ship_3_1.set_ship(set_row= 0, set_cell_start= 1, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 2:
                            m_ship.ship_2_1.set_ship(set_row= 0, set_cell_start= 1, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 1:
                            m_ship.ship_1_1.set_ship(set_row= 0, set_cell_start= 1, set_list= m_data.list_map_bot)

                if random_index == 2:
                    if m_data.list_map_bot[0][2] == 0:
                        self.X = 595 + self.LIST_SHIP_4 
                        self.Y = 171
                        m_ship.ship_4.set_ship(set_row= 0, set_cell_start= 2, set_list= m_data.list_map_bot)

                        if self.SIZE_SHIP_BOT == 3:
                            m_ship.ship_3_1.set_ship(set_row= 0, set_cell_start= 2, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 2:
                            m_ship.ship_2_1.set_ship(set_row= 0, set_cell_start= 2, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 1:
                            m_ship.ship_1_1.set_ship(set_row= 0, set_cell_start= 2, set_list= m_data.list_map_bot)

                if random_index == 3:
                    if m_data.list_map_bot[0][3] == 0:
                        self.X = 620 + self.LIST_SHIP_4 
                        self.Y = 171
                        m_ship.ship_4.set_ship(set_row= 0, set_cell_start= 3, set_list= m_data.list_map_bot)

                        if self.SIZE_SHIP_BOT == 3:
                            m_ship.ship_3_1.set_ship(set_row= 0, set_cell_start= 3, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 2:
                            m_ship.ship_2_1.set_ship(set_row= 0, set_cell_start= 3, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 1:
                            m_ship.ship_1_1.set_ship(set_row= 0, set_cell_start= 3, set_list= m_data.list_map_bot)
                        
                if random_index == 4:
                    if m_data.list_map_bot[0][4] == 0:
                        self.X = 645 + self.LIST_SHIP_4 
                        self.Y = 171
                        m_ship.ship_4.set_ship(set_row= 0, set_cell_start= 4, set_list= m_data.list_map_bot)

                        if self.SIZE_SHIP_BOT == 3:
                            m_ship.ship_3_1.set_ship(set_row= 0, set_cell_start= 4, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 2:
                            m_ship.ship_2_1.set_ship(set_row= 0, set_cell_start= 4, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 1:
                            m_ship.ship_1_1.set_ship(set_row= 0, set_cell_start= 4, set_list= m_data.list_map_bot)

                if random_index == 5:
                    if m_data.list_map_bot[0][5] == 0:
                        self.X = 670 + self.LIST_SHIP_4 
                        self.Y = 171
                        m_ship.ship_4.set_ship(set_row= 0, set_cell_start= 5, set_list= m_data.list_map_bot)

                        if self.SIZE_SHIP_BOT == 3:
                            m_ship.ship_3_1.set_ship(set_row= 0, set_cell_start= 5, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 2:
                            m_ship.ship_2_1.set_ship(set_row= 0, set_cell_start= 5, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 1:
                            m_ship.ship_1_1.set_ship(set_row= 0, set_cell_start= 5, set_list= m_data.list_map_bot)

                if random_index == 6:
                    if m_data.list_map_bot[0][6] == 0:
                        self.X = 695 + self.LIST_SHIP_4 
                        self.Y = 171
                        m_ship.ship_4.set_ship(set_row= 0, set_cell_start= 6, set_list= m_data.list_map_bot)

                        if self.SIZE_SHIP_BOT == 3:
                            m_ship.ship_3_1.set_ship(set_row= 0, set_cell_start= 6, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 2:
                            m_ship.ship_2_1.set_ship(set_row= 0, set_cell_start= 6, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 1:
                            m_ship.ship_1_1.set_ship(set_row= 0, set_cell_start= 6, set_list= m_data.list_map_bot)

                if random_index == 7:
                    if m_data.list_map_bot[0][7] == 0:
                        self.X = 720 + self.LIST_SHIP_4 
                        self.Y = 171
 
                        if self.SIZE_SHIP_BOT == 3:
                            m_ship.ship_3_1.set_ship(set_row= 0, set_cell_start= 7, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 2:
                            m_ship.ship_2_1.set_ship(set_row= 0, set_cell_start= 7, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 1:
                            m_ship.ship_1_1.set_ship(set_row= 0, set_cell_start= 7, set_list= m_data.list_map_bot)
                        
                if random_index == 8:
                    if m_data.list_map_bot[0][8] == 0:
                        self.X = 745 + self.LIST_SHIP_4 
                        self.Y = 171

                        if self.SIZE_SHIP_BOT == 3:
                            m_ship.ship_3_1.set_ship(set_row= 0, set_cell_start= 8, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 2:
                            m_ship.ship_2_1.set_ship(set_row= 0, set_cell_start= 8, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 1:
                            m_ship.ship_1_1.set_ship(set_row= 0, set_cell_start= 8, set_list= m_data.list_map_bot)

                if random_index == 9:
                    if m_data.list_map_bot[0][9] == 0:
                        self.X = 770 + self.LIST_SHIP_4 
                        self.Y = 171

                        if self.SIZE_SHIP_BOT == 3:
                            m_ship.ship_3_1.set_ship(set_row= 0, set_cell_start= 9, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 2:
                            m_ship.ship_2_1.set_ship(set_row= 0, set_cell_start= 9, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 1:
                            m_ship.ship_1_1.set_ship(set_row= 0, set_cell_start= 9, set_list= m_data.list_map_bot)
   
            if random_col == 1:
                if random_index == 0:
                    if m_data.list_map_bot[1][0] == 0:
                        self.X = 545 + self.LIST_SHIP_4 
                        self.Y = 198
                        m_ship.ship_4.set_ship(set_row= 1, set_cell_start= 0, set_list= m_data.list_map_bot)

                        if self.SIZE_SHIP_BOT == 3:
                            m_ship.ship_3_1.set_ship(set_row= 1, set_cell_start= 0, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 2:
                            m_ship.ship_2_1.set_ship(set_row= 1, set_cell_start= 0, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 1:
                            m_ship.ship_1_1.set_ship(set_row= 1, set_cell_start= 0, set_list= m_data.list_map_bot)

                if random_index == 1:
                    if m_data.list_map_bot[1][1] == 0:
                        self.X = 570 + self.LIST_SHIP_4 
                        self.Y = 198
                        m_ship.ship_4.set_ship(set_row= 1, set_cell_start= 1, set_list= m_data.list_map_bot)

                        if self.SIZE_SHIP_BOT == 3:
                            m_ship.ship_3_1.set_ship(set_row= 1, set_cell_start= 1, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 2:
                            m_ship.ship_2_1.set_ship(set_row= 1, set_cell_start= 1, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 1:
                            m_ship.ship_1_1.set_ship(set_row= 1, set_cell_start= 1, set_list= m_data.list_map_bot)

                if random_index == 2:
                    if m_data.list_map_bot[1][2] == 0:
                        self.X = 595 + self.LIST_SHIP_4 
                        self.Y = 198
                        m_ship.ship_4.set_ship(set_row= 1, set_cell_start= 2, set_list= m_data.list_map_bot)

                        if self.SIZE_SHIP_BOT == 3:
                            m_ship.ship_3_1.set_ship(set_row= 1, set_cell_start= 2, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 2:
                            m_ship.ship_2_1.set_ship(set_row= 1, set_cell_start= 2, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 1:
                            m_ship.ship_1_1.set_ship(set_row= 1, set_cell_start= 2, set_list= m_data.list_map_bot)

                if random_index == 3:
                    if m_data.list_map_bot[1][3] == 0:
                        self.X = 620 + self.LIST_SHIP_4 
                        self.Y = 198
                        m_ship.ship_4.set_ship(set_row= 1, set_cell_start= 3, set_list= m_data.list_map_bot)

                        if self.SIZE_SHIP_BOT == 3:
                            m_ship.ship_3_1.set_ship(set_row= 1, set_cell_start= 3, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 2:
                            m_ship.ship_2_1.set_ship(set_row= 1, set_cell_start= 3, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 1:
                            m_ship.ship_1_1.set_ship(set_row= 1, set_cell_start= 3, set_list= m_data.list_map_bot)

                if random_index == 4:
                    if m_data.list_map_bot[1][4] == 0:
                        self.X = 645 + self.LIST_SHIP_4 
                        self.Y = 198
                        m_ship.ship_4.set_ship(set_row= 1, set_cell_start= 4, set_list= m_data.list_map_bot)

                        if self.SIZE_SHIP_BOT == 3:
                            m_ship.ship_3_1.set_ship(set_row= 1, set_cell_start= 4, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 2:
                            m_ship.ship_2_1.set_ship(set_row= 1, set_cell_start= 4, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 1:
                            m_ship.ship_1_1.set_ship(set_row= 1, set_cell_start= 4, set_list= m_data.list_map_bot)

                if random_index == 5:
                    if m_data.list_map_bot[1][5] == 0:
                        self.X = 670 + self.LIST_SHIP_4 
                        self.Y = 198
                        m_ship.ship_4.set_ship(set_row= 1, set_cell_start= 5, set_list= m_data.list_map_bot)

                        if self.SIZE_SHIP_BOT == 3:
                            m_ship.ship_3_1.set_ship(set_row= 1, set_cell_start= 5, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 2:
                            m_ship.ship_2_1.set_ship(set_row= 1, set_cell_start= 5, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 1:
                            m_ship.ship_1_1.set_ship(set_row= 1, set_cell_start= 5, set_list= m_data.list_map_bot)

                if random_index == 6:
                    if m_data.list_map_bot[1][6] == 0:
                        self.X = 695 + self.LIST_SHIP_4 
                        self.Y = 198
                        m_ship.ship_4.set_ship(set_row= 1, set_cell_start= 6, set_list= m_data.list_map_bot)

                        if self.SIZE_SHIP_BOT == 3:
                            m_ship.ship_3_1.set_ship(set_row= 1, set_cell_start= 6, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 2:
                            m_ship.ship_2_1.set_ship(set_row= 1, set_cell_start= 6, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 1:
                            m_ship.ship_1_1.set_ship(set_row= 1, set_cell_start= 6, set_list= m_data.list_map_bot)
                        
                if random_index == 7:
                    if m_data.list_map_bot[1][7] == 0:
                        self.X = 720 + self.LIST_SHIP_4 
                        self.Y = 198
 
                        if self.SIZE_SHIP_BOT == 3:
                            m_ship.ship_3_1.set_ship(set_row= 1, set_cell_start= 7, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 2:
                            m_ship.ship_2_1.set_ship(set_row= 1, set_cell_start= 7, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 1:
                            m_ship.ship_1_1.set_ship(set_row= 1, set_cell_start= 7, set_list= m_data.list_map_bot)
                        
                if random_index == 8:
                    if m_data.list_map_bot[1][8] == 0:
                        self.X = 745 + self.LIST_SHIP_4 
                        self.Y = 198
 
                        if self.SIZE_SHIP_BOT == 3:
                            m_ship.ship_3_1.set_ship(set_row= 1, set_cell_start= 8, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 2:
                            m_ship.ship_2_1.set_ship(set_row= 1, set_cell_start= 8, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 1:
                            m_ship.ship_1_1.set_ship(set_row= 1, set_cell_start= 8, set_list= m_data.list_map_bot)

                if random_index == 9:
                    if m_data.list_map_bot[1][9] == 0:
                        self.X = 770 + self.LIST_SHIP_4 
                        self.Y = 198
 
                        if self.SIZE_SHIP_BOT == 3:
                            m_ship.ship_3_1.set_ship(set_row= 1, set_cell_start= 9, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 2:
                            m_ship.ship_2_1.set_ship(set_row= 1, set_cell_start= 9, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 1:
                            m_ship.ship_1_1.set_ship(set_row= 1, set_cell_start= 9, set_list= m_data.list_map_bot)

            if random_col == 2:
                if random_index == 0:
                    if m_data.list_map_bot[2][0] == 0:
                        self.X = 545 + self.LIST_SHIP_4 
                        self.Y = 225
                        m_ship.ship_4.set_ship(set_row= 2, set_cell_start= 0, set_list= m_data.list_map_bot)

                        if self.SIZE_SHIP_BOT == 3:
                            m_ship.ship_3_1.set_ship(set_row= 2, set_cell_start= 0, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 2:
                            m_ship.ship_2_1.set_ship(set_row= 2, set_cell_start= 0, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 1:
                            m_ship.ship_1_1.set_ship(set_row= 2, set_cell_start= 0, set_list= m_data.list_map_bot)

                if random_index == 1:
                    if m_data.list_map_bot[2][1] == 0:
                        self.X = 570 + self.LIST_SHIP_4 
                        self.Y = 225
                        m_ship.ship_4.set_ship(set_row= 2, set_cell_start= 1, set_list= m_data.list_map_bot)

                        if self.SIZE_SHIP_BOT == 3:
                            m_ship.ship_3_1.set_ship(set_row= 2, set_cell_start= 1, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 2:
                            m_ship.ship_2_1.set_ship(set_row= 2, set_cell_start= 1, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 1:
                            m_ship.ship_1_1.set_ship(set_row= 2, set_cell_start= 1, set_list= m_data.list_map_bot)

                if random_index == 2:
                    if m_data.list_map_bot[2][2] == 0:
                        self.X = 595 + self.LIST_SHIP_4 
                        self.Y = 225
                        m_ship.ship_4.set_ship(set_row= 2, set_cell_start= 2, set_list= m_data.list_map_bot)

                        if self.SIZE_SHIP_BOT == 3:
                            m_ship.ship_3_1.set_ship(set_row= 2, set_cell_start= 2, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 2:
                            m_ship.ship_2_1.set_ship(set_row= 2, set_cell_start= 2, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 1:
                            m_ship.ship_1_1.set_ship(set_row= 2, set_cell_start= 2, set_list= m_data.list_map_bot)

                if random_index == 3:
                    if m_data.list_map_bot[2][3] == 0:
                        self.X = 620 + self.LIST_SHIP_4 
                        self.Y = 225
                        m_ship.ship_4.set_ship(set_row= 2, set_cell_start= 3, set_list= m_data.list_map_bot)

                        if self.SIZE_SHIP_BOT == 3:
                            m_ship.ship_3_1.set_ship(set_row= 2, set_cell_start= 3, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 2:
                            m_ship.ship_2_1.set_ship(set_row= 2, set_cell_start= 3, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 1:
                            m_ship.ship_1_1.set_ship(set_row= 2, set_cell_start= 3, set_list= m_data.list_map_bot)

                if random_index == 4:
                    if m_data.list_map_bot[2][4] == 0:
                        self.X = 645 + self.LIST_SHIP_4 
                        self.Y = 225
                        m_ship.ship_4.set_ship(set_row= 2, set_cell_start= 4, set_list= m_data.list_map_bot)

                        if self.SIZE_SHIP_BOT == 3:
                            m_ship.ship_3_1.set_ship(set_row= 2, set_cell_start= 4, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 2:
                            m_ship.ship_2_1.set_ship(set_row= 2, set_cell_start= 4, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 1:
                            m_ship.ship_1_1.set_ship(set_row= 2, set_cell_start= 4, set_list= m_data.list_map_bot)

                if random_index == 5:
                    if m_data.list_map_bot[2][5] == 0:
                        self.X = 670 + self.LIST_SHIP_4 
                        self.Y = 225
                        m_ship.ship_4.set_ship(set_row= 2, set_cell_start= 5, set_list= m_data.list_map_bot)

                        if self.SIZE_SHIP_BOT == 3:
                            m_ship.ship_3_1.set_ship(set_row= 2, set_cell_start= 5, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 2:
                            m_ship.ship_2_1.set_ship(set_row= 2, set_cell_start= 5, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 1:
                            m_ship.ship_1_1.set_ship(set_row= 2, set_cell_start= 5, set_list= m_data.list_map_bot)


                if random_index == 6:
                    if m_data.list_map_bot[2][6] == 0:
                        self.X = 695 + self.LIST_SHIP_4 
                        self.Y = 225
                        m_ship.ship_4.set_ship(set_row= 2, set_cell_start= 6, set_list= m_data.list_map_bot)

                        if self.SIZE_SHIP_BOT == 3:
                            m_ship.ship_3_1.set_ship(set_row= 2, set_cell_start= 6, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 2:
                            m_ship.ship_2_1.set_ship(set_row= 2, set_cell_start= 6, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 1:
                            m_ship.ship_1_1.set_ship(set_row= 2, set_cell_start= 6, set_list= m_data.list_map_bot)

                if random_index == 7:
                    if m_data.list_map_bot[2][7] == 0:
                        self.X = 720 + self.LIST_SHIP_4 
                        self.Y = 225
 
                        if self.SIZE_SHIP_BOT == 3:
                            m_ship.ship_3_1.set_ship(set_row= 2, set_cell_start= 7, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 2:
                            m_ship.ship_2_1.set_ship(set_row= 2, set_cell_start= 7, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 1:
                            m_ship.ship_1_1.set_ship(set_row= 2, set_cell_start= 7, set_list= m_data.list_map_bot)
                        
                if random_index == 8:
                    if m_data.list_map_bot[2][8] == 0:
                        self.X = 745 + self.LIST_SHIP_4 
                        self.Y = 225
 
                        if self.SIZE_SHIP_BOT == 3:
                            m_ship.ship_3_1.set_ship(set_row= 2, set_cell_start= 8, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 2:
                            m_ship.ship_2_1.set_ship(set_row= 2, set_cell_start= 8, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 1:
                            m_ship.ship_1_1.set_ship(set_row= 2, set_cell_start= 8, set_list= m_data.list_map_bot)

                if random_index == 9:
                    if m_data.list_map_bot[2][9] == 0:
                        self.X = 770 + self.LIST_SHIP_4 
                        self.Y = 225
 
                        if self.SIZE_SHIP_BOT == 3:
                            m_ship.ship_3_1.set_ship(set_row= 2, set_cell_start= 9, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 2:
                            m_ship.ship_2_1.set_ship(set_row= 2, set_cell_start= 9, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 1:
                            m_ship.ship_1_1.set_ship(set_row= 2, set_cell_start= 9, set_list= m_data.list_map_bot)

            if random_col == 3:
                if random_index == 0:
                    if m_data.list_map_bot[3][0] == 0:
                        self.X = 545 + self.LIST_SHIP_4 
                        self.Y = 252
                        m_ship.ship_4.set_ship(set_row= 3, set_cell_start= 0, set_list= m_data.list_map_bot)

                        if self.SIZE_SHIP_BOT == 3:
                            m_ship.ship_3_1.set_ship(set_row= 3, set_cell_start= 0, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 2:
                            m_ship.ship_2_1.set_ship(set_row= 3, set_cell_start= 0, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 1:
                            m_ship.ship_1_1.set_ship(set_row= 3, set_cell_start= 0, set_list= m_data.list_map_bot)

                if random_index == 1:
                    if m_data.list_map_bot[3][1] == 0:
                        self.X = 570 + self.LIST_SHIP_4 
                        self.Y = 252
                        m_ship.ship_4.set_ship(set_row= 3, set_cell_start= 1, set_list= m_data.list_map_bot)

                        if self.SIZE_SHIP_BOT == 3:
                            m_ship.ship_3_1.set_ship(set_row= 3, set_cell_start= 1, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 2:
                            m_ship.ship_2_1.set_ship(set_row= 3, set_cell_start= 1, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 1:
                            m_ship.ship_1_1.set_ship(set_row= 3, set_cell_start= 1, set_list= m_data.list_map_bot)

                if random_index == 2:
                    if m_data.list_map_bot[3][2] == 0:
                        self.X = 595 + self.LIST_SHIP_4 
                        self.Y = 252
                        m_ship.ship_4.set_ship(set_row= 3, set_cell_start= 2, set_list= m_data.list_map_bot)

                        if self.SIZE_SHIP_BOT == 3:
                            m_ship.ship_3_1.set_ship(set_row= 3, set_cell_start= 2, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 2:
                            m_ship.ship_2_1.set_ship(set_row= 3, set_cell_start= 2, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 1:
                            m_ship.ship_1_1.set_ship(set_row= 3, set_cell_start= 2, set_list= m_data.list_map_bot)

                if random_index == 3:
                    if m_data.list_map_bot[3][3] == 0:
                        self.X = 620 + self.LIST_SHIP_4 
                        self.Y = 252
                        m_ship.ship_4.set_ship(set_row= 3, set_cell_start= 3, set_list= m_data.list_map_bot)

                        if self.SIZE_SHIP_BOT == 3:
                            m_ship.ship_3_1.set_ship(set_row= 3, set_cell_start= 3, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 2:
                            m_ship.ship_2_1.set_ship(set_row= 3, set_cell_start= 3, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 1:
                            m_ship.ship_1_1.set_ship(set_row= 3, set_cell_start= 3, set_list= m_data.list_map_bot)

                if random_index == 4:
                    if m_data.list_map_bot[3][4] == 0:
                        self.X = 645 + self.LIST_SHIP_4 
                        self.Y = 252
                        m_ship.ship_4.set_ship(set_row= 3, set_cell_start= 4, set_list= m_data.list_map_bot)

                        if self.SIZE_SHIP_BOT == 3:
                            m_ship.ship_3_1.set_ship(set_row= 3, set_cell_start= 4, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 2:
                            m_ship.ship_2_1.set_ship(set_row= 3, set_cell_start= 4, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 1:
                            m_ship.ship_1_1.set_ship(set_row= 3, set_cell_start= 4, set_list= m_data.list_map_bot)

                if random_index == 5:
                    if m_data.list_map_bot[3][5] == 0:
                        self.X = 670 + self.LIST_SHIP_4 
                        self.Y = 252
                        m_ship.ship_4.set_ship(set_row= 3, set_cell_start= 5, set_list= m_data.list_map_bot)

                        if self.SIZE_SHIP_BOT == 3:
                            m_ship.ship_3_1.set_ship(set_row= 3, set_cell_start= 5, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 2:
                            m_ship.ship_2_1.set_ship(set_row= 3, set_cell_start= 5, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 1:
                            m_ship.ship_1_1.set_ship(set_row= 3, set_cell_start= 5, set_list= m_data.list_map_bot)

                if random_index == 6:
                    if m_data.list_map_bot[3][6] == 0:
                        self.X = 695 + self.LIST_SHIP_4 
                        self.Y = 252
                        m_ship.ship_4.set_ship(set_row= 3, set_cell_start= 6, set_list= m_data.list_map_bot)

                        if self.SIZE_SHIP_BOT == 3:
                            m_ship.ship_3_1.set_ship(set_row= 3, set_cell_start= 6, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 2:
                            m_ship.ship_2_1.set_ship(set_row= 3, set_cell_start= 6, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 1:
                            m_ship.ship_1_1.set_ship(set_row= 3, set_cell_start= 6, set_list= m_data.list_map_bot)

                if random_index == 7:
                    if m_data.list_map_bot[3][7] == 0:
                        self.X = 720 + self.LIST_SHIP_4 
                        self.Y = 252
 
                        if self.SIZE_SHIP_BOT == 3:
                            m_ship.ship_3_1.set_ship(set_row= 3, set_cell_start= 7, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 2:
                            m_ship.ship_2_1.set_ship(set_row= 3, set_cell_start= 7, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 1:
                            m_ship.ship_1_1.set_ship(set_row= 3, set_cell_start= 7, set_list= m_data.list_map_bot)
                        
                if random_index == 8:
                    if m_data.list_map_bot[3][8] == 0:
                        self.X = 745 + self.LIST_SHIP_4 
                        self.Y = 252
 
                        if self.SIZE_SHIP_BOT == 3:
                            m_ship.ship_3_1.set_ship(set_row= 3, set_cell_start= 8, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 2:
                            m_ship.ship_2_1.set_ship(set_row= 3, set_cell_start= 8, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 1:
                            m_ship.ship_1_1.set_ship(set_row= 3, set_cell_start= 8, set_list= m_data.list_map_bot)

                if random_index == 9:
                    if m_data.list_map_bot[3][9] == 0:
                        self.X = 770 + self.LIST_SHIP_4 
                        self.Y = 252
 
                        if self.SIZE_SHIP_BOT == 3:
                            m_ship.ship_3_1.set_ship(set_row= 3, set_cell_start= 9, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 2:
                            m_ship.ship_2_1.set_ship(set_row= 3,set_cell_start= 9, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 1:
                            m_ship.ship_1_1.set_ship(set_row= 3, set_cell_start= 9, set_list= m_data.list_map_bot)

            if random_col == 4:
                if random_index == 0:
                    if m_data.list_map_bot[4][0] == 0:
                        self.X = 545 + self.LIST_SHIP_4 
                        self.Y = 279
                        m_ship.ship_4.set_ship(set_row= 4, set_cell_start= 0, set_list= m_data.list_map_bot)

                        if self.SIZE_SHIP_BOT == 3:
                            m_ship.ship_3_1.set_ship(set_row= 4, set_cell_start= 0, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 2:
                            m_ship.ship_2_1.set_ship(set_row= 4, set_cell_start= 0, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 1:
                            m_ship.ship_1_1.set_ship(set_row= 4, set_cell_start= 0, set_list= m_data.list_map_bot)

                if random_index == 1:
                    if m_data.list_map_bot[4][1] == 0:
                        self.X = 570 + self.LIST_SHIP_4 
                        self.Y = 279
                        m_ship.ship_4.set_ship(set_row= 4, set_cell_start= 1, set_list= m_data.list_map_bot)

                        if self.SIZE_SHIP_BOT == 3:
                            m_ship.ship_3_1.set_ship(set_row= 4, set_cell_start= 1, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 2:
                            m_ship.ship_2_1.set_ship(set_row= 4, set_cell_start= 1, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 1:
                            m_ship.ship_1_1.set_ship(set_row= 4, set_cell_start= 1, set_list= m_data.list_map_bot)

                if random_index == 2:
                    if m_data.list_map_bot[4][2] == 0:
                        self.X = 595 + self.LIST_SHIP_4 
                        self.Y = 279
                        m_ship.ship_4.set_ship(set_row= 4, set_cell_start= 2, set_list= m_data.list_map_bot)

                        if self.SIZE_SHIP_BOT == 3:
                            m_ship.ship_3_1.set_ship(set_row= 4, set_cell_start= 2, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 2:
                            m_ship.ship_2_1.set_ship(set_row= 4, set_cell_start= 2, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 1:
                            m_ship.ship_1_1.set_ship(set_row= 4, set_cell_start= 2, set_list= m_data.list_map_bot)

                if random_index == 3:
                    if m_data.list_map_bot[4][3] == 0:
                        self.X = 620 + self.LIST_SHIP_4 
                        self.Y = 279
                        m_ship.ship_4.set_ship(set_row= 4, set_cell_start= 2, set_list= m_data.list_map_bot)

                        if self.SIZE_SHIP_BOT == 3:
                            m_ship.ship_3_1.set_ship(set_row= 4, set_cell_start= 2, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 2:
                            m_ship.ship_2_1.set_ship(set_row= 4, set_cell_start= 2, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 1:
                            m_ship.ship_1_1.set_ship(set_row= 4, set_cell_start= 2, set_list= m_data.list_map_bot)

                if random_index == 4:
                    if m_data.list_map_bot[4][4] == 0:
                        self.X = 645 + self.LIST_SHIP_4 
                        self.Y = 279
                        m_ship.ship_4.set_ship(set_row= 4, set_cell_start= 3, set_list= m_data.list_map_bot)

                        if self.SIZE_SHIP_BOT == 3:
                            m_ship.ship_3_1.set_ship(set_row= 4, set_cell_start= 3, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 2:
                            m_ship.ship_2_1.set_ship(set_row= 4, set_cell_start= 3, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 1:
                            m_ship.ship_1_1.set_ship(set_row= 4, set_cell_start= 3, set_list= m_data.list_map_bot)
                        
                if random_index == 5:
                    if m_data.list_map_bot[4][5] == 0:
                        self.X = 670 + self.LIST_SHIP_4
                        self.Y = 279
                        m_ship.ship_4.set_ship(set_row= 4, set_cell_start= 4, set_list= m_data.list_map_bot)

                        if self.SIZE_SHIP_BOT == 3:
                            m_ship.ship_3_1.set_ship(set_row= 4, set_cell_start= 4, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 2:
                            m_ship.ship_2_1.set_ship(set_row= 4, set_cell_start= 4, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 1:
                            m_ship.ship_1_1.set_ship(set_row= 4, set_cell_start= 4, set_list= m_data.list_map_bot)

                if random_index == 6:
                    if m_data.list_map_bot[4][6] == 0:
                        self.X = 695 + self.LIST_SHIP_4 
                        self.Y = 279
                        m_ship.ship_4.set_ship(set_row= 4, set_cell_start= 5, set_list= m_data.list_map_bot)

                        if self.SIZE_SHIP_BOT == 3:
                            m_ship.ship_3_1.set_ship(set_row= 4, set_cell_start= 5, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 2:
                            m_ship.ship_2_1.set_ship(set_row= 4, set_cell_start= 5, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 1:
                            m_ship.ship_1_1.set_ship(set_row= 4, set_cell_start= 5, set_list= m_data.list_map_bot)

                if random_index == 7:
                    if m_data.list_map_bot[4][7] == 0:
                        self.X = 720 + self.LIST_SHIP_4 
                        self.Y = 279
 
                        if self.SIZE_SHIP_BOT == 3:
                            m_ship.ship_3_1.set_ship(set_row= 4, set_cell_start= 6, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 2:
                            m_ship.ship_2_1.set_ship(set_row= 4, set_cell_start= 6, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 1:
                            m_ship.ship_1_1.set_ship(set_row= 4, set_cell_start= 6, set_list= m_data.list_map_bot)
                        
                if random_index == 8:
                    if m_data.list_map_bot[4][8] == 0:
                        self.X = 745 + self.LIST_SHIP_4 
                        self.Y = 279
 
                        if self.SIZE_SHIP_BOT == 3:
                            m_ship.ship_3_1.set_ship(set_row= 4, set_cell_start= 7, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 2:
                            m_ship.ship_2_1.set_ship(set_row= 4, set_cell_start= 7, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 1:
                            m_ship.ship_1_1.set_ship(set_row= 4, set_cell_start= 7, set_list= m_data.list_map_bot)

                if random_index == 9:
                    if m_data.list_map_bot[4][9] == 0:
                        self.X = 770 + self.LIST_SHIP_4 
                        self.Y = 279
 
                        if self.SIZE_SHIP_BOT == 3:
                            m_ship.ship_3_1.set_ship(set_row= 4, set_cell_start= 8, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 2:
                            m_ship.ship_2_1.set_ship(set_row= 4, set_cell_start= 8, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 1:
                            m_ship.ship_1_1.set_ship(set_row= 4, set_cell_start= 8, set_list= m_data.list_map_bot)

            if random_col == 5:
                if random_index == 0:
                    if m_data.list_map_bot[5][0] == 0:
                        self.X = 545 + self.LIST_SHIP_4 
                        self.Y = 306
                        m_ship.ship_4.set_ship(set_row= 4, set_cell_start= 9, set_list= m_data.list_map_bot)

                        if self.SIZE_SHIP_BOT == 3:
                            m_ship.ship_3_1.set_ship(set_row= 4, set_cell_start= 9, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 2:
                            m_ship.ship_2_1.set_ship(set_row= 4, set_cell_start= 9, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 1:
                            m_ship.ship_1_1.set_ship(set_row= 4, set_cell_start= 9, set_list= m_data.list_map_bot)

                if random_index == 1:
                    if m_data.list_map_bot[5][1] == 0:
                        self.X = 570 + self.LIST_SHIP_4 
                        self.Y = 306
                        m_ship.ship_4.set_ship(set_row= 5, set_cell_start= 0, set_list= m_data.list_map_bot)

                        if self.SIZE_SHIP_BOT == 3:
                            m_ship.ship_3_1.set_ship(set_row= 5, set_cell_start= 0, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 2:
                            m_ship.ship_2_1.set_ship(set_row= 5, set_cell_start= 0, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 1:
                            m_ship.ship_1_1.set_ship(set_row= 5, set_cell_start= 0, set_list= m_data.list_map_bot)

                if random_index == 2:
                    if m_data.list_map_bot[5][2] == 0:
                        self.X = 595 + self.LIST_SHIP_4 
                        self.Y = 306
                        m_ship.ship_4.set_ship(set_row= 5, set_cell_start= 1, set_list= m_data.list_map_bot)

                        if self.SIZE_SHIP_BOT == 3:
                            m_ship.ship_3_1.set_ship(set_row= 5, set_cell_start= 1, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 2:
                            m_ship.ship_2_1.set_ship(set_row= 5, set_cell_start= 1, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 1:
                            m_ship.ship_1_1.set_ship(set_row= 5, set_cell_start= 1, set_list= m_data.list_map_bot)

                if random_index == 3:
                    if m_data.list_map_bot[5][3] == 0:
                        self.X = 620 + self.LIST_SHIP_4 
                        self.Y = 306
                        m_ship.ship_4.set_ship(set_row= 5, set_cell_start= 2, set_list= m_data.list_map_bot)

                        if self.SIZE_SHIP_BOT == 3:
                            m_ship.ship_3_1.set_ship(set_row= 5, set_cell_start= 2, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 2:
                            m_ship.ship_2_1.set_ship(set_row= 5, set_cell_start= 2, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 1:
                            m_ship.ship_1_1.set_ship(set_row= 5, set_cell_start= 2, set_list= m_data.list_map_bot)

                if random_index == 4:
                    if m_data.list_map_bot[5][4] == 0:
                        self.X = 645 + self.LIST_SHIP_4 
                        self.Y = 306
                        m_ship.ship_4.set_ship(set_row= 5, set_cell_start= 3, set_list= m_data.list_map_bot)

                        if self.SIZE_SHIP_BOT == 3:
                            m_ship.ship_3_1.set_ship(set_row= 5,set_cell_start= 3, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 2:
                            m_ship.ship_2_1.set_ship(set_row= 5, set_cell_start= 3, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 1:
                            m_ship.ship_1_1.set_ship(set_row= 5, set_cell_start= 3, set_list= m_data.list_map_bot)

                if random_index == 5:
                    if m_data.list_map_bot[5][5] == 0:
                        self.X = 670 + self.LIST_SHIP_4 
                        self.Y = 306
                        m_ship.ship_4.set_ship(set_row= 5, set_cell_start= 4, set_list= m_data.list_map_bot)

                        if self.SIZE_SHIP_BOT == 3:
                            m_ship.ship_3_1.set_ship(set_row= 5, set_cell_start= 4, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 2:
                            m_ship.ship_2_1.set_ship(set_row= 5, set_cell_start= 4, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 1:
                            m_ship.ship_1_1.set_ship(set_row= 5, set_cell_start= 4, set_list= m_data.list_map_bot)

                if random_index == 6:
                    if m_data.list_map_bot[5][6] == 0:
                        self.X = 695 + self.LIST_SHIP_4 
                        self.Y = 306
                        m_ship.ship_4.set_ship(set_row= 5, set_cell_start= 6, set_list= m_data.list_map_bot)

                        if self.SIZE_SHIP_BOT == 3:
                            m_ship.ship_3_1.set_ship(set_row= 5, set_cell_start= 6, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 2:
                            m_ship.ship_2_1.set_ship(set_row= 5, set_cell_start= 6, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 1:
                            m_ship.ship_1_1.set_ship(set_row= 5, set_cell_start= 6, set_list= m_data.list_map_bot)

                if random_index == 7:
                    if m_data.list_map_bot[5][7] == 0:
                        self.X = 720 + self.LIST_SHIP_4 
                        self.Y = 306
 
                        if self.SIZE_SHIP_BOT == 3:
                            m_ship.ship_3_1.set_ship(set_row= 5, set_cell_start= 7, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 2:
                            m_ship.ship_2_1.set_ship(set_row= 5, set_cell_start= 7, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 1:
                            m_ship.ship_1_1.set_ship(set_row= 5, set_cell_start= 7, set_list= m_data.list_map_bot)
                        
                if random_index == 8:
                    if m_data.list_map_bot[5][8] == 0:
                        self.X = 745 + self.LIST_SHIP_4 
                        self.Y = 306
 
                        if self.SIZE_SHIP_BOT == 3:
                            m_ship.ship_3_1.set_ship(set_row= 5, set_cell_start= 8, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 2:
                            m_ship.ship_2_1.set_ship(set_row= 5, set_cell_start= 8, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 1:
                            m_ship.ship_1_1.set_ship(set_row= 5, set_cell_start= 8, set_list= m_data.list_map_bot)

                if random_index == 9:
                    if m_data.list_map_bot[5][9] == 0:
                        self.X = 770 + self.LIST_SHIP_4 
                        self.Y = 306
 
                        if self.SIZE_SHIP_BOT == 3:
                            m_ship.ship_3_1.set_ship(set_row= 5, set_cell_start= 9, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 2:
                            m_ship.ship_2_1.set_ship(set_row= 5, set_cell_start= 9, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 1:
                            m_ship.ship_1_1.set_ship(set_row= 5, set_cell_start= 9, set_list= m_data.list_map_bot)

            if random_col == 6:
                if random_index == 0:
                    if m_data.list_map_bot[6][0] == 0:
                        self.X = 545 + self.LIST_SHIP_4 
                        self.Y = 333
                        m_ship.ship_4.set_ship(set_row= 6, set_cell_start= 0, set_list= m_data.list_map_bot)

                        if self.SIZE_SHIP_BOT == 3:
                            m_ship.ship_3_1.set_ship(set_row= 6, set_cell_start= 0, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 2:
                            m_ship.ship_2_1.set_ship(set_row= 6, set_cell_start= 0, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 1:
                            m_ship.ship_1_1.set_ship(set_row= 6, set_cell_start= 0, set_list= m_data.list_map_bot)

                if random_index == 1:
                    if m_data.list_map_bot[6][1] == 0:
                        self.X = 570 + self.LIST_SHIP_4 
                        self.Y = 333
                        m_ship.ship_4.set_ship(set_row= 6, set_cell_start= 1, set_list= m_data.list_map_bot)

                        if self.SIZE_SHIP_BOT == 3:
                            m_ship.ship_3_1.set_ship(set_row= 6, set_cell_start= 1, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 2:
                            m_ship.ship_2_1.set_ship(set_row= 6, set_cell_start= 1, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 1:
                            m_ship.ship_1_1.set_ship(set_row= 6, set_cell_start= 1, set_list= m_data.list_map_bot)

                if random_index == 2:
                    if m_data.list_map_bot[6][2] == 0:
                        self.X = 595 + self.LIST_SHIP_4 
                        self.Y = 333
                        m_ship.ship_4.set_ship(set_row= 6, set_cell_start= 2, set_list= m_data.list_map_bot)

                        if self.SIZE_SHIP_BOT == 3:
                            m_ship.ship_3_1.set_ship(set_row= 6,set_cell_start= 2, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 2:
                            m_ship.ship_2_1.set_ship(set_row= 6, set_cell_start= 2, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 1:
                            m_ship.ship_1_1.set_ship(set_row= 6, set_cell_start= 2, set_list= m_data.list_map_bot)

                if random_index == 3:
                    if m_data.list_map_bot[6][3] == 0:
                        self.X = 620 + self.LIST_SHIP_4 
                        self.Y = 333
                        m_ship.ship_4.set_ship(set_row= 6, set_cell_start= 3, set_list= m_data.list_map_bot)

                        if self.SIZE_SHIP_BOT == 3:
                            m_ship.ship_3_1.set_ship(set_row= 6, set_cell_start= 3, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 2:
                            m_ship.ship_2_1.set_ship(set_row= 6, set_cell_start= 3, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 1:
                            m_ship.ship_1_1.set_ship(set_row= 6, set_cell_start= 3, set_list= m_data.list_map_bot)

                if random_index == 4:
                    if m_data.list_map_bot[6][4] == 0:
                        self.X = 645 + self.LIST_SHIP_4 
                        self.Y = 333
                        m_ship.ship_4.set_ship(set_row= 6, set_cell_start= 4, set_list= m_data.list_map_bot)

                        if self.SIZE_SHIP_BOT == 3:
                            m_ship.ship_3_1.set_ship(set_row= 6, set_cell_start= 4, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 2:
                            m_ship.ship_2_1.set_ship(set_row= 6, set_cell_start= 4, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 1:
                            m_ship.ship_1_1.set_ship(set_row= 6, set_cell_start= 4, set_list= m_data.list_map_bot)

                if random_index == 5:
                    if m_data.list_map_bot[6][5] == 0:
                        self.X = 670 + self.LIST_SHIP_4 
                        self.Y = 333
                        m_ship.ship_4.set_ship(set_row= 6, set_cell_start= 5, set_list= m_data.list_map_bot)

                        if self.SIZE_SHIP_BOT == 3:
                            m_ship.ship_3_1.set_ship(set_row= 6, set_cell_start= 5, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 2:
                            m_ship.ship_2_1.set_ship(set_row= 6, set_cell_start= 5, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 1:
                            m_ship.ship_1_1.set_ship(set_row= 6, set_cell_start= 5, set_list= m_data.list_map_bot)

                if random_index == 6:
                    if m_data.list_map_bot[6][6] == 0:
                        self.X = 695 + self.LIST_SHIP_4 
                        self.Y = 333
                        m_ship.ship_4.set_ship(set_row= 6, set_cell_start= 6, set_list= m_data.list_map_bot)

                        if self.SIZE_SHIP_BOT == 3:
                            m_ship.ship_3_1.set_ship(set_row= 6, set_cell_start= 6, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 2:
                            m_ship.ship_2_1.set_ship(set_row= 6, set_cell_start= 6, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 1:
                            m_ship.ship_1_1.set_ship(set_row= 6, set_cell_start= 6, set_list= m_data.list_map_bot)
                
                if random_index == 1:
                    if m_data.list_map_bot[6][7] == 0:
                        self.X = 720 + self.LIST_SHIP_4 
                        self.Y = 306
 
                        if self.SIZE_SHIP_BOT == 3:
                            m_ship.ship_3_1.set_ship(set_row= 6, set_cell_start= 7, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 2:
                            m_ship.ship_2_1.set_ship(set_row= 6, set_cell_start= 7, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 1:
                            m_ship.ship_1_1.set_ship(set_row= 6, set_cell_start= 7, set_list= m_data.list_map_bot)
                            
                if random_index == 8:
                    if m_data.list_map_bot[6][8] == 0:
                        self.X = 745 + self.LIST_SHIP_4 
                        self.Y = 306
 
                        if self.SIZE_SHIP_BOT == 3:
                            m_ship.ship_3_1.set_ship(set_row= 6, set_cell_start= 8, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 2:
                            m_ship.ship_2_1.set_ship(set_row= 6, set_cell_start= 8, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 1:
                            m_ship.ship_1_1.set_ship(set_row= 6, set_cell_start= 8, set_list= m_data.list_map_bot)

                if random_index == 9:
                    if m_data.list_map_bot[6][9] == 0:
                        self.X = 770 + self.LIST_SHIP_4 
                        self.Y = 306
 
                        if self.SIZE_SHIP_BOT == 3:
                            m_ship.ship_3_1.set_ship(set_row= 6, set_cell_start= 9, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 2:
                            m_ship.ship_2_1.set_ship(set_row= 6, set_cell_start= 9, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 1:
                            m_ship.ship_1_1.set_ship(set_row= 6, set_cell_start= 9, set_list= m_data.list_map_bot)

            if random_col == 7:
                if random_index == 0:
                    if m_data.list_map_bot[7][0] == 0:
                        self.X = 545 + self.LIST_SHIP_4 
                        self.Y = 360
                        m_ship.ship_4.set_ship(set_row= 7, set_cell_start= 0, set_list= m_data.list_map_bot)

                        if self.SIZE_SHIP_BOT == 3:
                            m_ship.ship_3_1.set_ship(set_row= 7, set_cell_start= 0, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 2:
                            m_ship.ship_2_1.set_ship(set_row= 7, set_cell_start= 0, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 1:
                            m_ship.ship_1_1.set_ship(set_row= 7, set_cell_start= 0, set_list= m_data.list_map_bot)
                
                if random_index == 1:
                    if m_data.list_map_bot[7][1] == 0:
                        self.X = 570 + self.LIST_SHIP_4 
                        self.Y = 360
                        m_ship.ship_4.set_ship(set_row= 7, set_cell_start= 1, set_list= m_data.list_map_bot)

                        if self.SIZE_SHIP_BOT == 3:
                            m_ship.ship_3_1.set_ship(set_row= 7, set_cell_start= 1, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 2:
                            m_ship.ship_2_1.set_ship(set_row= 7, set_cell_start= 1, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 1:
                            m_ship.ship_1_1.set_ship(set_row= 7, set_cell_start= 1, set_list= m_data.list_map_bot)

                if random_index == 2:
                    if m_data.list_map_bot[7][2] == 0:
                        self.X = 595 + self.LIST_SHIP_4 
                        self.Y = 360
                        m_ship.ship_4.set_ship(set_row= 7, set_cell_start= 2, set_list= m_data.list_map_bot)

                        if self.SIZE_SHIP_BOT == 3:
                            m_ship.ship_3_1.set_ship(set_row= 7, set_cell_start= 2, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 2:
                            m_ship.ship_2_1.set_ship(set_row= 7, set_cell_start= 2, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 1:
                            m_ship.ship_1_1.set_ship(set_row= 7, set_cell_start= 2, set_list= m_data.list_map_bot)

                if random_index == 3:
                    if m_data.list_map_bot[7][3] == 0:
                        self.X = 620 + self.LIST_SHIP_4 
                        self.Y = 360
                        m_ship.ship_4.set_ship(set_row= 7, set_cell_start= 3, set_list= m_data.list_map_bot)

                        if self.SIZE_SHIP_BOT == 3:
                            m_ship.ship_3_1.set_ship(set_row= 7, set_cell_start= 3, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 2:
                            m_ship.ship_2_1.set_ship(set_row= 7, set_cell_start= 3, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 1:
                            m_ship.ship_1_1.set_ship(set_row= 7, set_cell_start= 3, set_list= m_data.list_map_bot)

                if random_index == 4:
                    if m_data.list_map_bot[7][4] == 0:
                        self.X = 645 + self.LIST_SHIP_4 
                        self.Y = 360
                        m_ship.ship_4.set_ship(set_row= 7, set_cell_start= 4, set_list= m_data.list_map_bot)

                        if self.SIZE_SHIP_BOT == 3:
                            m_ship.ship_3_1.set_ship(set_row= 7, set_cell_start= 4, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 2:
                            m_ship.ship_2_1.set_ship(set_row= 7, set_cell_start= 4, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 1:
                            m_ship.ship_1_1.set_ship(set_row= 7, set_cell_start= 4, set_list= m_data.list_map_bot)

                if random_index == 5:
                    if m_data.list_map_bot[7][5] == 0:
                        self.X = 670 + self.LIST_SHIP_4 
                        self.Y = 360
                        m_ship.ship_4.set_ship(set_row= 7, set_cell_start= 5, set_list= m_data.list_map_bot)

                        if self.SIZE_SHIP_BOT == 3:
                            m_ship.ship_3_1.set_ship(set_row= 7, set_cell_start= 5, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 2:
                            m_ship.ship_2_1.set_ship(set_row= 7, set_cell_start= 5, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 1:
                            m_ship.ship_1_1.set_ship(set_row= 7, set_cell_start= 5, set_list= m_data.list_map_bot)

                if random_index == 6:
                    if m_data.list_map_bot[7][6] == 0:
                        self.X = 695 + self.LIST_SHIP_4 
                        self.Y = 360
                        m_ship.ship_4.set_ship(set_row= 7, set_cell_start= 6, set_list= m_data.list_map_bot)

                        if self.SIZE_SHIP_BOT == 3:
                            m_ship.ship_3_1.set_ship(set_row= 7, set_cell_start= 6, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 2:
                            m_ship.ship_2_1.set_ship(set_row= 7, set_cell_start= 6, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 1:
                            m_ship.ship_1_1.set_ship(set_row= 7, set_cell_start= 6, set_list= m_data.list_map_bot)

                if random_index == 7:
                    if m_data.list_map_bot[7][7] == 0:
                        self.X = 720 + self.LIST_SHIP_4 
                        self.Y = 360
 
                        if self.SIZE_SHIP_BOT == 3:
                            m_ship.ship_3_1.set_ship(set_row= 7, set_cell_start= 7, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 2:
                            m_ship.ship_2_1.set_ship(set_row= 7, set_cell_start= 7, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 1:
                            m_ship.ship_1_1.set_ship(set_row= 7, set_cell_start= 7, set_list= m_data.list_map_bot)

                if random_index == 8:
                    if m_data.list_map_bot[7][8] == 0:
                        self.X = 745 + self.LIST_SHIP_4 
                        self.Y = 360
 
                        if self.SIZE_SHIP_BOT == 3:
                            m_ship.ship_3_1.set_ship(set_row= 7, set_cell_start= 8, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 2:
                            m_ship.ship_2_1.set_ship(set_row= 7, set_cell_start= 8, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 1:
                            m_ship.ship_1_1.set_ship(set_row= 7, set_cell_start= 8, set_list= m_data.list_map_bot)

                if random_index == 9:
                    if m_data.list_map_bot[7][9] == 0:
                        self.X = 770 + self.LIST_SHIP_4 
                        self.Y = 360
 
                        if self.SIZE_SHIP_BOT == 3:
                            m_ship.ship_3_1.set_ship(set_row= 7, set_cell_start= 9, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 2:
                            m_ship.ship_2_1.set_ship(set_row= 7, set_cell_start= 9, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 1:
                            m_ship.ship_1_1.set_ship(set_row= 7, set_cell_start= 9, set_list= m_data.list_map_bot)

            if random_col == 8:
                if random_index == 0:
                    if m_data.list_map_bot[8][0] == 0:
                        self.X = 545 + self.LIST_SHIP_4 
                        self.Y = 387
                        m_ship.ship_4.set_ship(set_row= 8, set_cell_start= 0, set_list= m_data.list_map_bot)

                        if self.SIZE_SHIP_BOT == 3:
                            m_ship.ship_3_1.set_ship(set_row= 8, set_cell_start= 0, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 2:
                            m_ship.ship_2_1.set_ship(set_row= 8, set_cell_start= 0, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 1:
                            m_ship.ship_1_1.set_ship(set_row= 8, set_cell_start= 0, set_list= m_data.list_map_bot)

                if random_index == 1:
                    if m_data.list_map_bot[8][1] == 0:
                        self.X = 570 + self.LIST_SHIP_4 
                        self.Y = 387
                        m_ship.ship_4.set_ship(set_row= 8, set_cell_start= 1, set_list= m_data.list_map_bot)

                        if self.SIZE_SHIP_BOT == 3:
                            m_ship.ship_3_1.set_ship(set_row= 8, set_cell_start= 1, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 2:
                            m_ship.ship_2_1.set_ship(set_row= 8, set_cell_start= 1, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 1:
                            m_ship.ship_1_1.set_ship(set_row= 8, set_cell_start= 1, set_list= m_data.list_map_bot)
                        
                if random_index == 2:
                    if m_data.list_map_bot[8][2] == 0:
                        self.X = 595 + self.LIST_SHIP_4 
                        self.Y = 387
                        m_ship.ship_4.set_ship(set_row= 8, set_cell_start= 2, set_list= m_data.list_map_bot)

                        if self.SIZE_SHIP_BOT == 3:
                            m_ship.ship_3_1.set_ship(set_row= 8, set_cell_start= 2, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 2:
                            m_ship.ship_2_1.set_ship(set_row= 8, set_cell_start= 2, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 1:
                            m_ship.ship_1_1.set_ship(set_row= 8, set_cell_start= 2, set_list= m_data.list_map_bot)

                if random_index == 3:
                    if m_data.list_map_bot[8][3] == 0:
                        self.X = 620 + self.LIST_SHIP_4 
                        self.Y = 387
                        m_ship.ship_4.set_ship(set_row= 8, set_cell_start= 3, set_list= m_data.list_map_bot)

                        if self.SIZE_SHIP_BOT == 3:
                            m_ship.ship_3_1.set_ship(set_row= 8, set_cell_start= 3, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 2:
                            m_ship.ship_2_1.set_ship(set_row= 8, set_cell_start= 3, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 1:
                            m_ship.ship_1_1.set_ship(set_row= 8, set_cell_start= 3, set_list= m_data.list_map_bot)

                if random_index == 4:
                    if m_data.list_map_bot[8][4] == 0:
                        self.X = 645 + self.LIST_SHIP_4 
                        self.Y = 387
                        m_ship.ship_4.set_ship(set_row= 8, set_cell_start= 4, set_list= m_data.list_map_bot)

                        if self.SIZE_SHIP_BOT == 3:
                            m_ship.ship_3_1.set_ship(set_row= 8, set_cell_start= 4, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 2:
                            m_ship.ship_2_1.set_ship(set_row= 8, set_cell_start= 4, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 1:
                            m_ship.ship_1_1.set_ship(set_row= 8, set_cell_start= 4, set_list= m_data.list_map_bot)

                if random_index == 5:
                    if m_data.list_map_bot[8][5] == 0:
                        self.X = 670 + self.LIST_SHIP_4 
                        self.Y = 387
                        m_ship.ship_4.set_ship(set_row= 8, set_cell_start= 5, set_list= m_data.list_map_bot)

                        if self.SIZE_SHIP_BOT == 3:
                            m_ship.ship_3_1.set_ship(set_row= 8, set_cell_start= 5, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 2:
                            m_ship.ship_2_1.set_ship(set_row= 8, set_cell_start= 5, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 1:
                            m_ship.ship_1_1.set_ship(set_row= 8, set_cell_start= 5, set_list= m_data.list_map_bot)

                if random_index == 6:
                    if m_data.list_map_bot[8][6] == 0:
                        self.X = 695 + self.LIST_SHIP_4 
                        self.Y = 387
                        m_ship.ship_4.set_ship(set_row= 8, set_cell_start= 6, set_list= m_data.list_map_bot)

                        if self.SIZE_SHIP_BOT == 3:
                            m_ship.ship_3_1.set_ship(set_row= 8, set_cell_start= 6, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 2:
                            m_ship.ship_2_1.set_ship(set_row= 8, set_cell_start= 6, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 1:
                            m_ship.ship_1_1.set_ship(set_row= 8, set_cell_start= 6, set_list= m_data.list_map_bot)
                        
                if random_index == 7:
                    if m_data.list_map_bot[8][7] == 0:
                        self.X = 720 + self.LIST_SHIP_4 
                        self.Y = 387
 
                        if self.SIZE_SHIP_BOT == 3:
                            m_ship.ship_3_1.set_ship(set_row= 8, set_cell_start= 7, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 2:
                            m_ship.ship_2_1.set_ship(set_row= 8, set_cell_start= 7, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 1:
                            m_ship.ship_1_1.set_ship(set_row= 8, set_cell_start= 7, set_list= m_data.list_map_bot)

                if random_index == 8:
                    if m_data.list_map_bot[8][8] == 0:
                        self.X = 745 + self.LIST_SHIP_4 
                        self.Y = 387
 
                        if self.SIZE_SHIP_BOT == 3:
                            m_ship.ship_3_1.set_ship(set_row= 8, set_cell_start= 8, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 2:
                            m_ship.ship_2_1.set_ship(set_row= 8, set_cell_start= 8, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 1:
                            m_ship.ship_1_1.set_ship(set_row= 8, set_cell_start= 8, set_list= m_data.list_map_bot)

                if random_index == 9:
                    if m_data.list_map_bot[8][9] == 0:
                        self.X = 770 + self.LIST_SHIP_4 
                        self.Y = 387
 
                        if self.SIZE_SHIP_BOT == 3:
                            m_ship.ship_3_1.set_ship(set_row= 8, set_cell_start= 9, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 2:
                            m_ship.ship_2_1.set_ship(set_row= 8, set_cell_start= 9, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 1:
                            m_ship.ship_1_1.set_ship(set_row= 8, set_cell_start= 9, set_list= m_data.list_map_bot)
    
            if random_col == 9:
                if random_index == 0:
                    if m_data.list_map_bot[9][0] == 0:
                        self.X = 545 + self.LIST_SHIP_4 
                        self.Y = 414
                        m_ship.ship_4.set_ship(set_row= 9, set_cell_start= 0, set_list= m_data.list_map_bot)

                        if self.SIZE_SHIP_BOT == 3:
                            m_ship.ship_3_1.set_ship(set_row= 9, set_cell_start= 0, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 2:
                            m_ship.ship_2_1.set_ship(set_row= 9, set_cell_start= 0, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 1:
                            m_ship.ship_1_1.set_ship(set_row= 9, set_cell_start= 0, set_list= m_data.list_map_bot)
                if random_index == 1:
                    if m_data.list_map_bot[9][1] == 0:
                        self.X = 570 + self.LIST_SHIP_4 
                        self.Y = 414
                        m_ship.ship_4.set_ship(set_row= 9, set_cell_start= 1, set_list= m_data.list_map_bot)

                        if self.SIZE_SHIP_BOT == 3:
                            m_ship.ship_3_1.set_ship(set_row= 9, set_cell_start= 1, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 2:
                            m_ship.ship_2_1.set_ship(set_row= 9, set_cell_start= 1, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 1:
                            m_ship.ship_1_1.set_ship(set_row= 9, set_cell_start= 1, set_list= m_data.list_map_bot)

                if random_index == 2:
                    if m_data.list_map_bot[9][2] == 0:
                        self.X = 595 + self.LIST_SHIP_4 
                        self.Y = 414
                        m_ship.ship_4.set_ship(set_row= 9, set_cell_start= 2, set_list= m_data.list_map_bot)

                        if self.SIZE_SHIP_BOT == 3:
                            m_ship.ship_3_1.set_ship(set_row= 9, set_cell_start= 2, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 2:
                            m_ship.ship_2_1.set_ship(set_row= 9, set_cell_start= 2, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 1:
                            m_ship.ship_1_1.set_ship(set_row= 9, set_cell_start= 2, set_list= m_data.list_map_bot)
                if random_index == 3:
                    if m_data.list_map_bot[9][3] == 0:
                        self.X = 620 + self.LIST_SHIP_4 
                        self.Y = 414
                        m_ship.ship_4.set_ship(set_row= 9, set_cell_start= 3, set_list= m_data.list_map_bot)

                        if self.SIZE_SHIP_BOT == 3:
                            m_ship.ship_3_1.set_ship(set_row= 9, set_cell_start= 3, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 2:
                            m_ship.ship_2_1.set_ship(set_row= 9, set_cell_start= 3, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 1:
                            m_ship.ship_1_1.set_ship(set_row= 9, set_cell_start= 3, set_list= m_data.list_map_bot)

                if random_index == 4:
                    if m_data.list_map_bot[9][4] == 0:
                        self.X = 645 + self.LIST_SHIP_4 
                        self.Y = 414
                        m_ship.ship_4.set_ship(set_row= 9, set_cell_start= 4, set_list= m_data.list_map_bot)

                        if self.SIZE_SHIP_BOT == 3:
                            m_ship.ship_3_1.set_ship(set_row= 9, set_cell_start= 4, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 2:
                            m_ship.ship_2_1.set_ship(set_row= 9, set_cell_start= 4, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 1:
                            m_ship.ship_1_1.set_ship(set_row= 9, set_cell_start= 4, set_list= m_data.list_map_bot)
                if random_index == 5:
                    if m_data.list_map_bot[9][5] == 0:
                        self.X = 670 + self.LIST_SHIP_4 
                        self.Y = 414
                        m_ship.ship_4.set_ship(set_row= 9, set_cell_start= 5, set_list= m_data.list_map_bot)

                        if self.SIZE_SHIP_BOT == 3:
                            m_ship.ship_3_1.set_ship(set_row= 9, set_cell_start= 5, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 2:
                            m_ship.ship_2_1.set_ship(set_row= 9, set_cell_start= 5, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 1:
                            m_ship.ship_1_1.set_ship(set_row= 9, set_cell_start= 5, set_list= m_data.list_map_bot)

                if random_index == 6:
                    if m_data.list_map_bot[9][6] == 0:
                        self.X = 695 + self.LIST_SHIP_4 
                        self.Y = 414
                        m_ship.ship_4.set_ship(set_row= 9, set_cell_start= 6, set_list= m_data.list_map_bot)

                        if self.SIZE_SHIP_BOT == 3:
                            m_ship.ship_3_1.set_ship(set_row= 9, set_cell_start= 6, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 2:
                            m_ship.ship_2_1.set_ship(set_row= 9, set_cell_start= 6, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 1:
                            m_ship.ship_1_1.set_ship(set_row= 9, set_cell_start= 6, set_list= m_data.list_map_bot)

                if random_index == 7:
                    if m_data.list_map_bot[9][7] == 0:
                        self.X = 720 + self.LIST_SHIP_4 
                        self.Y = 414
 
                        if self.SIZE_SHIP_BOT == 3:
                            m_ship.ship_3_1.set_ship(set_row= 9, set_cell_start= 7, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 2:
                            m_ship.ship_2_1.set_ship(set_row= 9, set_cell_start= 7, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 1:
                            m_ship.ship_1_1.set_ship(set_row= 9, set_cell_start= 7, set_list= m_data.list_map_bot)

                if random_index == 8:
                    if m_data.list_map_bot[9][8] == 0:
                        self.X = 745 + self.LIST_SHIP_4 
                        self.Y = 414
 
                        if self.SIZE_SHIP_BOT == 3:
                            m_ship.ship_3_1.set_ship(set_row= 9, set_cell_start= 8, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 2:
                            m_ship.ship_2_1.set_ship(set_row= 9, set_cell_start= 8, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 1:
                            m_ship.ship_1_1.set_ship(set_row= 9, set_cell_start= 8, set_list= m_data.list_map_bot)
                if random_index == 9:
                    if m_data.list_map_bot[9][9] == 0:
                        self.X = 770 + self.LIST_SHIP_4 
                        self.Y = 414
 
                        if self.SIZE_SHIP_BOT == 3:
                            m_ship.ship_3_1.set_ship(set_row= 9, set_cell_start= 9, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 2:
                            m_ship.ship_2_1.set_ship(set_row= 9, set_cell_start= 9, set_list= m_data.list_map_bot)
                        if self.SIZE_SHIP_BOT == 1:
                            m_ship.ship_1_1.set_ship(set_row= 9, set_cell_start= 9, set_list= m_data.list_map_bot)

        if self.COUNT:
            print('List bot =')
            for i in m_data.list_map_bot:  
                print(i)
            print("\n")
            self.COUNT = False

bot = Bot()


ship_3_1 = Bot(width3= 75, y3= 180, size_ship_bot= 3)
ship_3_2 = Bot(width3= 75, y3= 230, size_ship_bot= 3)

#
ship_2_1 = Bot(width3= 50, y3= 180, size_ship_bot= 2)
ship_2_2 = Bot(width3= 50, y3= 230, size_ship_bot= 2)
ship_2_3 = Bot(width3= 50, y3= 280, size_ship_bot= 2)

#
ship_1_1 = Bot(width3= 25, y3= 180, size_ship_bot= 1)
ship_1_2 = Bot(width3= 25, y3= 230, size_ship_bot= 1)
ship_1_3 = Bot(width3= 25, y3= 280, size_ship_bot= 1)
ship_1_4 = Bot(width3= 25, y3= 330, size_ship_bot= 1)


