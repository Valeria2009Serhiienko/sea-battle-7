import pygame
import modules.main_modules.settings as m_settings
import modules.main_modules.data_base as m_data
import modules.cell.create_cell as m_cell
import random
pygame.init()

# 4
class Ship_4(m_settings.Settings):
    def __init__(self, width1 = 100, height1 = 25, x1 = 480, y1 = 180,
                list_ship_4 = m_data.list_x[3], list_ship_3 = m_data.list_x[2], 
                list_ship_2 = m_data.list_x[1], list_ship_1 = m_data.list_x[0], 
                name1 = 'img/ship/ship_4.png',
                direction_x1 = 0, direction_y1 = 0,
                size_ship = 4):
        m_settings.Settings.__init__(self, width = width1, height = height1, x = x1, y = y1, 
                file_name = name1, direction_x= direction_x1, direction_y= direction_y1)

        self.load_image()  
        self.ROTATE = False

        self.LIST_SHIP_4 = list_ship_4
        self.LIST_SHIP_3 = list_ship_3
        self.LIST_SHIP_2 = list_ship_2
        self.LIST_SHIP_1 = list_ship_1
        
        self.SIZE_SHIP = size_ship
        self.FLAG = 0 
        self.X_START = x1
        self.Y_START = y1
        self.RANDOM_NUMBER = 0 
        self.SET_SHIP = False 
        self.READY = False

    def rotate(self, range_Y_1, range_Y_2, number_X, number_Y):
        for cell in m_data.list_cells:
            if self.ROTATE:
                if self.Y <= range_Y_1 + cell.HEIGHT and range_Y_2 + cell.HEIGHT:
                    self.X = number_X
                    self.Y = number_Y + self.LIST_SHIP_4 

    def set_ship(self, set_row, set_cell_start, set_list = m_data.list_map_player):
        #
        number_ship = self.SIZE_SHIP
        cell_start = set_cell_start
        #
        # умова горизонтального розміщення корабля та заповнення списку відповідно розташуванню корабля
        if self.ROTATE == False and len(set_list[set_row]) - cell_start >= self.SIZE_SHIP:
            # len(set_list[set_row]) - cell_start > self.SIZE_SHIP:
            self.SET_SHIP = True
            set_list[set_row][cell_start] = number_ship
            # цикл що задає цифри розміру корабля замість ноликів 
            for count in range(number_ship - 1):
                cell_start += 1
                set_list[set_row][cell_start] = number_ship
            # умова що перевіряє нулевий рядок та займає комірки 5 все навколо коробля
            if set_row == 0:
                # умова що перевіряє, якщо довжина списка не перевищена, то за кораблем ставимо зайнято 5
                if len(set_list[set_row]) > cell_start + 1:
                    set_list[set_row][cell_start + 1] = 5
                # умова що перевіряє, якщо стартова комірка розташування корабля більша за нуль, то перед кораблем ставимо зайнято 5
                if set_cell_start > 0:
                    set_list[set_row][cell_start - (number_ship)] = 5
                # 
                cell_start = set_cell_start
                for count in range(number_ship + 1):
                    # умова що перевіряє, якщо довжина списка не перевищена, то під кораблем ставимо зайнято 5
                    if len(set_list[set_row]) > cell_start:
                        set_list[set_row + 1][cell_start] = 5
                        cell_start += 1
                    else:
                        # умова що перевіряє, якщо довжина списка перевищена, то під кораблем, 
                        # індекс що менше на одиницю за стортовий ставимо зайнято 5, а також в тому ж самому рядку що стоїть корабель
                        set_list[set_row][cell_start - (number_ship + 1)] = 5
                        set_list[set_row + 1][cell_start - (number_ship + 1)] = 5
            # рядки від 1 до 8, 0 рядок перший, 9 рядок - останній
            if set_row > 0 and set_row < 9:
                if len(set_list[set_row]) > cell_start + 1:
                    set_list[set_row][cell_start + 1] = 5
                if set_cell_start > 0:
                    set_list[set_row][cell_start - (number_ship)] = 5
                    set_list[set_row + 1][cell_start - (number_ship)] = 5
                    set_list[set_row - 1][cell_start - (number_ship)] = 5
                cell_start = set_cell_start
                for count in range(number_ship + 1):
                    if len(set_list[set_row]) > cell_start:
                        set_list[set_row + 1][cell_start] = 5
                        set_list[set_row - 1][cell_start] = 5
                        cell_start += 1
                    else:
                        set_list[set_row][cell_start - (number_ship + 1)] = 5
                        set_list[set_row + 1][cell_start - (number_ship + 1)] = 5
                        set_list[set_row - 1][cell_start - (number_ship + 1)] = 5
            # для останнього рядка
            if set_row == 9:
                if len(set_list[set_row]) > cell_start + 1:
                    set_list[set_row][cell_start + 1] = 5
                if set_cell_start > 0:
                    set_list[set_row][cell_start - (number_ship)] = 5
                    set_list[set_row - 1][cell_start - (number_ship)] = 5
                cell_start = set_cell_start
                for count in range(number_ship + 1):
                    if len(set_list[set_row]) > cell_start:
                        set_list[set_row - 1][cell_start] = 5
                        cell_start += 1
                    else:
                        set_list[set_row][cell_start - (number_ship + 1)] = 5
                        set_list[set_row - 1][cell_start - (number_ship + 1)] = 5
            #return 
        #
        if self.FLAG == 0:
            for i in set_list:
                print(i)
            print("\n")
            self.FLAG = 1

    def collision_ship_4(self):
        for cell in m_data.list_cells:
            # стовбчик перший
            if self.X >= 190 and self.X <= 190 + cell.WIDTH:
                # ряд перший перша комірка
                if self.Y <= 170 + cell.HEIGHT:
                    if m_data.list_map_player[0][0] == 0:
                        self.X = 190 + self.LIST_SHIP_4 
                        self.Y = 171
                        self.set_ship(set_row= 0, set_cell_start= 0)

                    if m_data.list_map_player[0][0] == 5:
                        if self.SET_SHIP == False:
                            self.X = self.X_START
                            self.Y = self.Y_START

                            # 3
                            if self.SIZE_SHiP == 3:
                                m_data.end_blit_ship_3_1[0] = False
                                m_data.end_blit_ship_3_2[0] = False

                            # 2
                            if self.SIZE_SHIP == 2:
                                m_data.end_blit_ship_2_1[0] = False
                                m_data.end_blit_ship_2_2[0] = False
                                m_data.end_blit_ship_2_3[0] = False

                            #1
                            if self.SIZE_SHIP == 1:
                                m_data.end_blit_ship_1_1[0] = False
                                m_data.end_blit_ship_1_2[0] = False
                                m_data.end_blit_ship_1_3[0] = False
                                m_data.end_blit_ship_1_4[0] = False
                        
                # ряд другий перша комірка 
                elif self.Y <= 195 + cell.HEIGHT:
                    if m_data.list_map_player[1][0] == 0:
                        self.X = 190 + self.LIST_SHIP_4
                        self.Y = 198 
                        self.set_ship(set_row= 1, set_cell_start= 0)
                    if m_data.list_map_player[1][0] in m_data.number:
                        if self.SET_SHIP == False:
                            self.X = self.X_START
                            self.Y = self.Y_START
                
                            if self.SIZE_SHIP == 3:
                                m_data.end_blit_ship_3_1[0] = False
                                m_data.end_blit_ship_3_2[0] = False

                            # 2
                            if self.SIZE_SHIP == 2:
                                m_data.end_blit_ship_2_1[0] = False
                                m_data.end_blit_ship_2_2[0] = False
                                m_data.end_blit_ship_2_3[0] = False

                            #1
                            if self.SIZE_SHIP == 1:
                                m_data.end_blit_ship_1_1[0] = False
                                m_data.end_blit_ship_1_2[0] = False
                                m_data.end_blit_ship_1_3[0] = False
                                m_data.end_blit_ship_1_4[0] = False

                # ряд третій перша комірка 
                elif self.Y <= 220 + cell.HEIGHT and 215 + cell.HEIGHT:
                    if m_data.list_map_player[2][0] == 0:
                        self.X = 190 + self.LIST_SHIP_4
                        self.Y = 225
                        self.set_ship(set_row= 2, set_cell_start= 0)
                    if m_data.list_map_player[2][0] == 5:
                        if self.SET_SHIP == False:
                            self.X = self.X_START
                            self.Y = self.Y_START
                            if self.SIZE_SHIP == 3:
                                m_data.end_blit_ship_3_1[0] = False
                                m_data.end_blit_ship_3_2[0] = False

                            # 2
                            if self.SIZE_SHIP == 2:
                                m_data.end_blit_ship_2_1[0] = False
                                m_data.end_blit_ship_2_2[0] = False
                                m_data.end_blit_ship_2_3[0] = False

                            #1
                            if self.SIZE_SHIP == 1:
                                m_data.end_blit_ship_1_1[0] = False
                                m_data.end_blit_ship_1_2[0] = False
                                m_data.end_blit_ship_1_3[0] = False
                                m_data.end_blit_ship_1_4[0] = False
                
                # ряд четвертий перша комірка 
                elif self.Y <= 245 + cell.HEIGHT and 215 + cell.HEIGHT:
                    if m_data.list_map_player[3][0] == 0:
                        self.X = 190 + self.LIST_SHIP_4
                        self.Y = 252
                        self.set_ship(set_row= 3, set_cell_start= 0)
                    if m_data.list_map_player[3][0] == 5:
                        if self.SET_SHIP == False:
                            self.X = self.X_START
                            self.Y = self.Y_START

                            if self.SIZE_SHIP == 3:
                                m_data.end_blit_ship_3_1[0] = False
                                m_data.end_blit_ship_3_2[0] = False

                            # 2
                            if self.SIZE_SHIP == 2:
                                m_data.end_blit_ship_2_1[0] = False
                                m_data.end_blit_ship_2_2[0] = False
                                m_data.end_blit_ship_2_3[0] = False

                            #1
                            if self.SIZE_SHIP == 1:
                                m_data.end_blit_ship_1_1[0] = False
                                m_data.end_blit_ship_1_2[0] = False
                                m_data.end_blit_ship_1_3[0] = False
                                m_data.end_blit_ship_1_4[0] = False

                # ряд пʼятий перша комірка 
                elif self.Y <= 270 + cell.HEIGHT and 215 + cell.HEIGHT:
                    if m_data.list_map_player[4][0] == 0:
                        self.X = 190 + self.LIST_SHIP_4
                        self.Y = 279 
                        self.set_ship(set_row= 4, set_cell_start= 0)
                    if m_data.list_map_player[4][0] == 5:
                        if self.SET_SHIP == False:
                            self.X = self.X_START
                            self.Y = self.Y_START

                            if self.SIZE_SHIP == 3:
                                m_data.end_blit_ship_3_1[0] = False
                                m_data.end_blit_ship_3_2[0] = False

                            # 2
                            if self.SIZE_SHIP == 2:
                                m_data.end_blit_ship_2_1[0] = False
                                m_data.end_blit_ship_2_2[0] = False
                                m_data.end_blit_ship_2_3[0] = False

                            #1
                            if self.SIZE_SHIP == 1:
                                m_data.end_blit_ship_1_1[0] = False
                                m_data.end_blit_ship_1_2[0] = False
                                m_data.end_blit_ship_1_3[0] = False
                                m_data.end_blit_ship_1_4[0] = False
                # ряд шостий перша комірка 
                elif self.Y <= 295 + cell.HEIGHT and 215 + cell.HEIGHT:
                    if m_data.list_map_player[5][0] == 0:
                        self.X = 190 + self.LIST_SHIP_4
                        self.Y = 306
                        self.set_ship(set_row= 5, set_cell_start= 0)
                    if m_data.list_map_player[5][0] == 5:
                        if self.SET_SHIP == False:
                            self.X = self.X_START
                            self.Y = self.Y_START

                            if self.SIZE_SHIP == 3:
                                m_data.end_blit_ship_3_1[0] = False
                                m_data.end_blit_ship_3_2[0] = False

                            # 2
                            if self.SIZE_SHIP == 2:
                                m_data.end_blit_ship_2_1[0] = False
                                m_data.end_blit_ship_2_2[0] = False
                                m_data.end_blit_ship_2_3[0] = False

                            #1
                            if self.SIZE_SHIP == 1:
                                m_data.end_blit_ship_1_1[0] = False
                                m_data.end_blit_ship_1_2[0] = False
                                m_data.end_blit_ship_1_3[0] = False
                                m_data.end_blit_ship_1_4[0] = False
                            
                # ряд сьомий перша комірка 
                elif self.Y <= 320 + cell.HEIGHT and 215 + cell.HEIGHT:
                    if m_data.list_map_player[6][0] == 0:
                        self.X = 190 + self.LIST_SHIP_4
                        self.Y = 333
                        self.set_ship(set_row= 6, set_cell_start= 0)
                    if m_data.list_map_player[6][0] == 5:
                        if self.SET_SHIP == False:
                            self.X = self.X_START
                            self.Y = self.Y_START

                            if self.SIZE_SHIP == 3:
                                m_data.end_blit_ship_3_1[0] = False
                                m_data.end_blit_ship_3_2[0] = False

                            # 2
                            if self.SIZE_SHIP == 2:
                                m_data.end_blit_ship_2_1[0] = False
                                m_data.end_blit_ship_2_2[0] = False
                                m_data.end_blit_ship_2_3[0] = False

                            #1
                            if self.SIZE_SHIP == 1:
                                m_data.end_blit_ship_1_1[0] = False
                                m_data.end_blit_ship_1_2[0] = False
                                m_data.end_blit_ship_1_3[0] = False
                                m_data.end_blit_ship_1_4[0] = False

                # ряд восьмий перша комірка    
                elif  self.Y <= 345 + cell.HEIGHT and 215 + cell.HEIGHT:
                    if m_data.list_map_player[7][0] == 0:
                        self.X = 190 + self.LIST_SHIP_4
                        self.Y = 333
                        self.set_ship(set_row= 7, set_cell_start= 0)
                    if m_data.list_map_player[7][0] == 5:
                        if self.SET_SHIP == False:
                            self.X = self.X_START
                            self.Y = self.Y_START

                            if self.SIZE_SHIP == 3:
                                m_data.end_blit_ship_3_1[0] = False
                                m_data.end_blit_ship_3_2[0] = False

                            # 2
                            if self.SIZE_SHIP == 2:
                                m_data.end_blit_ship_2_1[0] = False
                                m_data.end_blit_ship_2_2[0] = False
                                m_data.end_blit_ship_2_3[0] = False

                            #1
                            if self.SIZE_SHIP == 1:
                                m_data.end_blit_ship_1_1[0] = False
                                m_data.end_blit_ship_1_2[0] = False
                                m_data.end_blit_ship_1_3[0] = False
                                m_data.end_blit_ship_1_4[0] = False

                # ряд девʼятий перша комірка             
                elif  self.Y <= 370 + cell.HEIGHT and 215 + cell.HEIGHT:
                    if m_data.list_map_player[8][0] == 0:
                        self.X = 190 + self.LIST_SHIP_4
                        self.Y = 387
                        self.set_ship(set_row= 8, set_cell_start= 0)
                    if m_data.list_map_player[8][0] == 5:
                        if self.SET_SHIP == False:
                            self.X = self.X_START
                            self.Y = self.Y_START

                            if self.SIZE_SHIP == 3:
                                m_data.end_blit_ship_3_1[0] = False
                                m_data.end_blit_ship_3_2[0] = False

                            # 2
                            if self.SIZE_SHIP == 2:
                                m_data.end_blit_ship_2_1[0] = False
                                m_data.end_blit_ship_2_2[0] = False
                                m_data.end_blit_ship_2_3[0] = False

                            #1
                            if self.SIZE_SHIP == 1:
                                m_data.end_blit_ship_1_1[0] = False
                                m_data.end_blit_ship_1_2[0] = False
                                m_data.end_blit_ship_1_3[0] = False
                                m_data.end_blit_ship_1_4[0] = False

                # ряд десятий перша комірка            
                elif  self.Y <= 395 + cell.HEIGHT and 215 + cell.HEIGHT:
                    if m_data.list_map_player[9][0] == 0:
                        self.X = 190 + self.LIST_SHIP_4
                        self.Y = 414
                        self.set_ship(set_row= 9, set_cell_start= 0)
                    if m_data.list_map_player[9][0] == 5:
                        if self.SET_SHIP == False:
                            self.X = self.X_START
                            self.Y = self.Y_START

                            if self.SIZE_SHIP == 3:
                                m_data.end_blit_ship_3_1[0] = False
                                m_data.end_blit_ship_3_2[0] = False

                            # 2
                            if self.SIZE_SHIP == 2:
                                m_data.end_blit_ship_2_1[0] = False
                                m_data.end_blit_ship_2_2[0] = False
                                m_data.end_blit_ship_2_3[0] = False

                            #1
                            if self.SIZE_SHIP == 1:
                                m_data.end_blit_ship_1_1[0] = False
                                m_data.end_blit_ship_1_2[0] = False
                                m_data.end_blit_ship_1_3[0] = False
                                m_data.end_blit_ship_1_4[0] = False

            # друга клітинка 
            if self.X >= 215 and self.X <= 215 + cell.WIDTH:
                # ряд перший друга комірка
                if self.Y <= 170 + cell.HEIGHT and 240 + cell.HEIGHT:
                    if m_data.list_map_player[0][1] == 0:
                        self.X = 215 + self.LIST_SHIP_4 + 2
                        self.Y = 171
                        self.set_ship(set_row= 0, set_cell_start= 1)
                    if m_data.list_map_player[0][1] == 5:
                        if self.SET_SHIP == False:
                            self.X = self.X_START
                            self.Y = self.Y_START

                            if self.SIZE_SHIP == 3:
                                m_data.end_blit_ship_3_1[0] = False
                                m_data.end_blit_ship_3_2[0] = False

                            # 2
                            if self.SIZE_SHIP == 2:
                                m_data.end_blit_ship_2_1[0] = False
                                m_data.end_blit_ship_2_2[0] = False
                                m_data.end_blit_ship_2_3[0] = False

                            #1
                            if self.SIZE_SHIP == 1:
                                m_data.end_blit_ship_1_1[0] = False
                                m_data.end_blit_ship_1_2[0] = False
                                m_data.end_blit_ship_1_3[0] = False
                                m_data.end_blit_ship_1_4[0] = False

                # ряд другий друга комірка
                elif self.Y <= 195 + cell.HEIGHT and 240 + cell.HEIGHT:
                    if m_data.list_map_player[1][1] == 0:
                        self.X = 215 + self.LIST_SHIP_4 + 2
                        self.Y = 198
                        self.set_ship(set_row= 1, set_cell_start= 1)
                    if m_data.list_map_player[1][1] == 5:
                        if self.SET_SHIP == False:
                            self.X = self.X_START
                            self.Y = self.Y_START

                            if self.SIZE_SHIP == 3:
                                m_data.end_blit_ship_3_1[0] = False
                                m_data.end_blit_ship_3_2[0] = False

                            # 2
                            if self.SIZE_SHIP == 2:
                                m_data.end_blit_ship_2_1[0] = False
                                m_data.end_blit_ship_2_2[0] = False
                                m_data.end_blit_ship_2_3[0] = False

                            #1
                            if self.SIZE_SHIP == 1:
                                m_data.end_blit_ship_1_1[0] = False
                                m_data.end_blit_ship_1_2[0] = False
                                m_data.end_blit_ship_1_3[0] = False
                                m_data.end_blit_ship_1_4[0] = False

                # ряд третій друга комірка
                elif self.Y <= 220 + cell.HEIGHT and 240 + cell.HEIGHT:
                    if m_data.list_map_player[2][1] == 0:
                        self.X = 215 + self.LIST_SHIP_4 + 2 
                        self.Y = 225
                        self.set_ship(set_row= 2, set_cell_start= 1)
                    if m_data.list_map_player[2][1] == 5:
                        if self.SET_SHIP == False:
                            self.X = self.X_START
                            self.Y = self.Y_START

                            if self.SIZE_SHIP == 3:
                                m_data.end_blit_ship_3_1[0] = False
                                m_data.end_blit_ship_3_2[0] = False

                            # 2
                            if self.SIZE_SHIP == 2:
                                m_data.end_blit_ship_2_1[0] = False
                                m_data.end_blit_ship_2_2[0] = False
                                m_data.end_blit_ship_2_3[0] = False

                            #1
                            if self.SIZE_SHIP == 1:
                                m_data.end_blit_ship_1_1[0] = False
                                m_data.end_blit_ship_1_2[0] = False
                                m_data.end_blit_ship_1_3[0] = False
                                m_data.end_blit_ship_1_4[0] = False
                        
                # ряд четвертий друга комірка
                elif self.Y <= 245 + cell.HEIGHT and 240 + cell.HEIGHT:
                    if m_data.list_map_player[3][1] == 0:
                        self.X = 215 + self.LIST_SHIP_4 + 2 
                        self.Y = 252
                        self.set_ship(set_row= 3, set_cell_start= 1)
                    if m_data.list_map_player[3][1] == 5:
                        if self.SET_SHIP == False:
                            self.X = self.X_START
                            self.Y = self.Y_START

                            if self.SIZE_SHIP == 3:
                                m_data.end_blit_ship_3_1[0] = False
                                m_data.end_blit_ship_3_2[0] = False

                            # 2
                            if self.SIZE_SHIP == 2:
                                m_data.end_blit_ship_2_1[0] = False
                                m_data.end_blit_ship_2_2[0] = False
                                m_data.end_blit_ship_2_3[0] = False

                            #1
                            if self.SIZE_SHIP == 1:
                                m_data.end_blit_ship_1_1[0] = False
                                m_data.end_blit_ship_1_2[0] = False
                                m_data.end_blit_ship_1_3[0] = False
                                m_data.end_blit_ship_1_4[0] = False

                    
                # ряд пʼятий друга комірка        
                elif self.Y <= 270 + cell.HEIGHT and 240 + cell.HEIGHT:
                    if m_data.list_map_player[4][1] == 0:
                        self.X = 215 + self.LIST_SHIP_4 + 2  
                        self.Y = 279
                        self.set_ship(set_row= 4, set_cell_start= 1)
                    if m_data.list_map_player[4][1] == 5:
                        if self.SET_SHIP == False:
                            self.X = self.X_START
                            self.Y = self.Y_START  

                            if self.SIZE_SHIP == 3:
                                m_data.end_blit_ship_3_1[0] = False
                                m_data.end_blit_ship_3_2[0] = False

                            # 2
                            if self.SIZE_SHIP == 2:
                                m_data.end_blit_ship_2_1[0] = False
                                m_data.end_blit_ship_2_2[0] = False
                                m_data.end_blit_ship_2_3[0] = False

                            #1
                            if self.SIZE_SHIP == 1:
                                m_data.end_blit_ship_1_1[0] = False
                                m_data.end_blit_ship_1_2[0] = False
                                m_data.end_blit_ship_1_3[0] = False
                                m_data.end_blit_ship_1_4[0] = False
                        
                # ряд шостий друга комірка
                elif  self.Y <= 295 + cell.HEIGHT and 240 + cell.HEIGHT:
                    if m_data.list_map_player[5][1] == 0:
                        self.X = 215 + self.LIST_SHIP_4 + 2  
                        self.Y = 306
                        self.set_ship(set_row= 5, set_cell_start= 1)
                    if m_data.list_map_player[5][1] == 5:
                        if self.SET_SHIP == False:
                            self.X = self.X_START
                            self.Y = self.Y_START 

                            if self.SIZE_SHIP == 3:
                                m_data.end_blit_ship_3_1[0] = False
                                m_data.end_blit_ship_3_2[0] = False

                            # 2
                            if self.SIZE_SHIP == 2:
                                m_data.end_blit_ship_2_1[0] = False
                                m_data.end_blit_ship_2_2[0] = False
                                m_data.end_blit_ship_2_3[0] = False

                            #1
                            if self.SIZE_SHIP == 1:
                                m_data.end_blit_ship_1_1[0] = False
                                m_data.end_blit_ship_1_2[0] = False
                                m_data.end_blit_ship_1_3[0] = False
                                m_data.end_blit_ship_1_4[0] = False

                # ряд сьомий друга комірка
                elif self.Y <= 320 + cell.HEIGHT and 240 + cell.HEIGHT:  
                    if m_data.list_map_player[6][1] == 0:
                        self.X = 215 + self.LIST_SHIP_4 + 2  
                        self.Y = 333
                        self.set_ship(set_row= 6, set_cell_start= 1)
                    if m_data.list_map_player[6][1] == 5:
                        if self.SET_SHIP == False:
                            self.X = self.X_START
                            self.Y = self.Y_START 

                            if self.SIZE_SHIP == 3:
                                m_data.end_blit_ship_3_1[0] = False
                                m_data.end_blit_ship_3_2[0] = False

                            # 2
                            if self.SIZE_SHIP == 2:
                                m_data.end_blit_ship_2_1[0] = False
                                m_data.end_blit_ship_2_2[0] = False
                                m_data.end_blit_ship_2_3[0] = False

                            #1
                            if self.SIZE_SHIP == 1:
                                m_data.end_blit_ship_1_1[0] = False
                                m_data.end_blit_ship_1_2[0] = False
                                m_data.end_blit_ship_1_3[0] = False
                                m_data.end_blit_ship_1_4[0] = False
    
                # ряд восьмий друга комірка
                elif  self.Y <= 345 + cell.HEIGHT and 240 + cell.HEIGHT:
                    if m_data.list_map_player[7][1] == 0:
                        self.X = 215 + self.LIST_SHIP_4 + 2  
                        self.Y = 360
                        self.set_ship(set_row= 7, set_cell_start= 1)
                    if m_data.list_map_player[7][1] == 5:
                        if self.SET_SHIP == False:
                            self.X = self.X_START
                            self.Y = self.Y_START

                            if self.SIZE_SHIP == 3:
                                m_data.end_blit_ship_3_1[0] = False
                                m_data.end_blit_ship_3_2[0] = False

                            # 2
                            if self.SIZE_SHIP == 2:
                                m_data.end_blit_ship_2_1[0] = False
                                m_data.end_blit_ship_2_2[0] = False
                                m_data.end_blit_ship_2_3[0] = False

                            #1
                            if self.SIZE_SHIP == 1:
                                m_data.end_blit_ship_1_1[0] = False
                                m_data.end_blit_ship_1_2[0] = False
                                m_data.end_blit_ship_1_3[0] = False
                                m_data.end_blit_ship_1_4[0] = False
                        
                # ряд девʼятий друга комірка
                elif self.Y <= 370 + cell.HEIGHT and 240 + cell.HEIGHT:
                    if m_data.list_map_player[8][1] == 0:
                        self.X = 215 + self.LIST_SHIP_4 + 2 
                        self.Y = 387
                        self.set_ship(set_row= 8, set_cell_start= 1)
                    if m_data.list_map_player[8][1] == 5:
                        if self.SET_SHIP == False:
                            self.X = self.X_START
                            self.Y = self.Y_START

                            if self.SIZE_SHIP == 3:
                                m_data.end_blit_ship_3_1[0] = False
                                m_data.end_blit_ship_3_2[0] = False

                            # 2
                            if self.SIZE_SHIP == 2:
                                m_data.end_blit_ship_2_1[0] = False
                                m_data.end_blit_ship_2_2[0] = False
                                m_data.end_blit_ship_2_3[0] = False

                            #1
                            if self.SIZE_SHIP == 1:
                                m_data.end_blit_ship_1_1[0] = False
                                m_data.end_blit_ship_1_2[0] = False
                                m_data.end_blit_ship_1_3[0] = False
                                m_data.end_blit_ship_1_4[0] = False
                        
                # ряд десятий друга комірка
                elif  self.Y <= 395 + cell.HEIGHT and 240 + cell.HEIGHT:
                    if m_data.list_map_player[9][1] == 0:
                        self.X = 215 + self.LIST_SHIP_4 + 2  
                        self.Y = 414  
                        self.set_ship(set_row= 9, set_cell_start= 1)
                    if m_data.list_map_player[9][1] == 5:
                        if self.SET_SHIP == False:
                            self.X = self.X_START
                            self.Y = self.Y_START

                            if self.SIZE_SHIP == 3:
                                m_data.end_blit_ship_3_1[0] = False
                                m_data.end_blit_ship_3_2[0] = False

                            # 2
                            if self.SIZE_SHIP == 2:
                                m_data.end_blit_ship_2_1[0] = False
                                m_data.end_blit_ship_2_2[0] = False
                                m_data.end_blit_ship_2_3[0] = False

                            #1
                            if self.SIZE_SHIP == 1:
                                m_data.end_blit_ship_1_1[0] = False
                                m_data.end_blit_ship_1_2[0] = False
                                m_data.end_blit_ship_1_3[0] = False
                                m_data.end_blit_ship_1_4[0] = False
                        
            # третя клітинка 
            if self.X >= 240 and self.X <= 240 + cell.WIDTH:
                # ряд перший третя комірка
                if self.Y <= 170 + cell.HEIGHT and 265 + cell.HEIGHT:
                    if m_data.list_map_player[0][2] == 0:
                        self.X = 240 + self.LIST_SHIP_4 + 4 
                        self.Y = 171
                        self.set_ship(set_row= 0, set_cell_start= 2)
                    if m_data.list_map_player[0][2] == 5:
                        if self.SET_SHIP == False:
                            self.X = self.X_START
                            self.Y = self.Y_START

                            if self.SIZE_SHIP == 3:
                                m_data.end_blit_ship_3_1[0] = False
                                m_data.end_blit_ship_3_2[0] = False

                            # 2
                            if self.SIZE_SHIP == 2:
                                m_data.end_blit_ship_2_1[0] = False
                                m_data.end_blit_ship_2_2[0] = False
                                m_data.end_blit_ship_2_3[0] = False

                            #1
                            if self.SIZE_SHIP == 1:
                                m_data.end_blit_ship_1_1[0] = False
                                m_data.end_blit_ship_1_2[0] = False
                                m_data.end_blit_ship_1_3[0] = False
                                m_data.end_blit_ship_1_4[0] = False
                            
                # ряд другий третя клітинка
                elif self.Y <= 195 + cell.HEIGHT and 265 + cell.HEIGHT:
                    if m_data.list_map_player[1][2] == 0:
                        self.X = 240 + self.LIST_SHIP_4 + 4
                        self.Y = 198
                        self.set_ship(set_row= 1, set_cell_start= 2)
                    if m_data.list_map_player[1][2] == 5:
                        if self.SET_SHIP == False:
                            self.X = self.X_START
                            self.Y = self.Y_START

                            if self.SIZE_SHIP == 3:
                                m_data.end_blit_ship_3_1[0] = False
                                m_data.end_blit_ship_3_2[0] = False

                            # 2
                            if self.SIZE_SHIP == 2:
                                m_data.end_blit_ship_2_1[0] = False
                                m_data.end_blit_ship_2_2[0] = False
                                m_data.end_blit_ship_2_3[0] = False

                            #1
                            if self.SIZE_SHIP == 1:
                                m_data.end_blit_ship_1_1[0] = False
                                m_data.end_blit_ship_1_2[0] = False
                                m_data.end_blit_ship_1_3[0] = False
                                m_data.end_blit_ship_1_4[0] = False

                # ряд третій третя клітинка
                elif self.Y <= 220 + cell.HEIGHT and 265 + cell.HEIGHT:
                    if m_data.list_map_player[2][2] == 0:
                        self.X = 240 + self.LIST_SHIP_4 + 4 
                        self.Y = 225
                        self.set_ship(set_row= 2, set_cell_start= 2)
                    if m_data.list_map_player[2][2] == 5:
                        if self.SET_SHIP == False:
                            self.X = self.X_START
                            self.Y = self.Y_START

                            if self.SIZE_SHIP == 3:
                                m_data.end_blit_ship_3_1[0] = False
                                m_data.end_blit_ship_3_2[0] = False

                            # 2
                            if self.SIZE_SHIP == 2:
                                m_data.end_blit_ship_2_1[0] = False
                                m_data.end_blit_ship_2_2[0] = False
                                m_data.end_blit_ship_2_3[0] = False

                            #1
                            if self.SIZE_SHIP == 1:
                                m_data.end_blit_ship_1_1[0] = False
                                m_data.end_blit_ship_1_2[0] = False
                                m_data.end_blit_ship_1_3[0] = False
                                m_data.end_blit_ship_1_4[0] = False
                # ряд четвертий третя клітинка
                elif self.Y <= 245 + cell.HEIGHT and 265 + cell.HEIGHT:
                    if m_data.list_map_player[3][2] == 0:
                        self.X = 240 + self.LIST_SHIP_4 + 4 
                        self.Y = 252
                        self.set_ship(set_row= 3, set_cell_start= 2)
                    if m_data.list_map_player[3][2] == 5:
                        if self.SET_SHIP == False:
                            self.X = self.X_START
                            self.Y = self.Y_START

                            if self.SIZE_SHIP == 3:
                                m_data.end_blit_ship_3_1[0] = False
                                m_data.end_blit_ship_3_2[0] = False

                            # 2
                            if self.SIZE_SHIP == 2:
                                m_data.end_blit_ship_2_1[0] = False
                                m_data.end_blit_ship_2_2[0] = False
                                m_data.end_blit_ship_2_3[0] = False

                            #1
                            if self.SIZE_SHIP == 1:
                                m_data.end_blit_ship_1_1[0] = False
                                m_data.end_blit_ship_1_2[0] = False
                                m_data.end_blit_ship_1_3[0] = False
                                m_data.end_blit_ship_1_4[0] = False

                # ряд пʼятий третя клітинка
                elif self.Y <= 270 + cell.HEIGHT and 265 + cell.HEIGHT:
                    if m_data.list_map_player[4][2] == 0:
                        self.X = 240 + self.LIST_SHIP_4 + 4 
                        self.Y = 279
                        self.set_ship(set_row= 4, set_cell_start= 2)
                    if m_data.list_map_player[4][2] == 5:
                        if self.SET_SHIP == False:
                            self.X = self.X_START
                            self.Y = self.Y_START

                            if self.SIZE_SHIP == 3:
                                m_data.end_blit_ship_3_1[0] = False
                                m_data.end_blit_ship_3_2[0] = False

                            # 2
                            if self.SIZE_SHIP == 2:
                                m_data.end_blit_ship_2_1[0] = False
                                m_data.end_blit_ship_2_2[0] = False
                                m_data.end_blit_ship_2_3[0] = False

                            #1
                            if self.SIZE_SHIP == 1:
                                m_data.end_blit_ship_1_1[0] = False
                                m_data.end_blit_ship_1_2[0] = False
                                m_data.end_blit_ship_1_3[0] = False
                                m_data.end_blit_ship_1_4[0] = False


                # ряд шостий третя клітинка
                elif  self.Y <= 295 + cell.HEIGHT and 265 + cell.HEIGHT:
                    if m_data.list_map_player[5][2] == 0:
                        self.X = 240 + self.LIST_SHIP_4 + 4 
                        self.Y = 306
                        self.set_ship(set_row= 5, set_cell_start= 2)
                    if m_data.list_map_player[5][2] == 5:
                        if self.SET_SHIP == False:
                            self.X = self.X_START
                            self.Y = self.Y_START
                        
                            if self.SIZE_SHIP == 3:
                                m_data.end_blit_ship_3_1[0] = False
                                m_data.end_blit_ship_3_2[0] = False

                            # 2
                            if self.SIZE_SHIP == 2:
                                m_data.end_blit_ship_2_1[0] = False
                                m_data.end_blit_ship_2_2[0] = False
                                m_data.end_blit_ship_2_3[0] = False

                            #1
                            if self.SIZE_SHIP == 1:
                                m_data.end_blit_ship_1_1[0] = False
                                m_data.end_blit_ship_1_2[0] = False
                                m_data.end_blit_ship_1_3[0] = False
                                m_data.end_blit_ship_1_4[0] = False
                    
                # ряд сьомий третя клітинка
                elif self.Y <= 320 + cell.HEIGHT and 265 + cell.HEIGHT:
                    if m_data.list_map_player[6][2] == 0:
                        self.X = 240 + self.LIST_SHIP_4 + 4 
                        self.Y = 333
                        self.set_ship(set_row= 6, set_cell_start= 2)
                    if m_data.list_map_player[6][2] == 5:
                        if self.SET_SHIP == False:
                            self.X = self.X_START
                            self.Y = self.Y_START

                            if self.SIZE_SHIP == 3:
                                m_data.end_blit_ship_3_1[0] = False
                                m_data.end_blit_ship_3_2[0] = False

                            # 2
                            if self.SIZE_SHIP == 2:
                                m_data.end_blit_ship_2_1[0] = False
                                m_data.end_blit_ship_2_2[0] = False
                                m_data.end_blit_ship_2_3[0] = False

                            #1
                            if self.SIZE_SHIP == 1:
                                m_data.end_blit_ship_1_1[0] = False
                                m_data.end_blit_ship_1_2[0] = False
                                m_data.end_blit_ship_1_3[0] = False
                                m_data.end_blit_ship_1_4[0] = False
                # ряд восьмий третя клітинка    
                elif  self.Y <= 345 + cell.HEIGHT and 265 + cell.HEIGHT:
                    if m_data.list_map_player[7][2] == 0:
                        self.X = 240 + self.LIST_SHIP_4 + 4 
                        self.Y = 360
                        self.set_ship(set_row= 7, set_cell_start= 2)
                    if m_data.list_map_player[7][2] == 5:
                        if self.SET_SHIP == False:
                            self.X = self.X_START
                            self.Y = self.Y_START

                            if self.SIZE_SHIP == 3:
                                m_data.end_blit_ship_3_1[0] = False
                                m_data.end_blit_ship_3_2[0] = False

                            # 2
                            if self.SIZE_SHIP == 2:
                                m_data.end_blit_ship_2_1[0] = False
                                m_data.end_blit_ship_2_2[0] = False
                                m_data.end_blit_ship_2_3[0] = False

                            #1
                            if self.SIZE_SHIP == 1:
                                m_data.end_blit_ship_1_1[0] = False
                                m_data.end_blit_ship_1_2[0] = False
                                m_data.end_blit_ship_1_3[0] = False
                                m_data.end_blit_ship_1_4[0] = False
                
                # ряд девʼятий третя клітинка
                elif self.Y <= 370 + cell.HEIGHT and 265 + cell.HEIGHT:
                    if m_data.list_map_player[8][2] == 0:
                        self.X = 240 + self.LIST_SHIP_4 + 4
                        self.Y = 387
                        self.set_ship(set_row= 8, set_cell_start= 2)
                    if m_data.list_map_player[8][2] == 5:
                        if self.SET_SHIP == False:
                            self.X = self.X_START
                            self.Y = self.Y_START

                            if self.SIZE_SHIP == 3:
                                m_data.end_blit_ship_3_1[0] = False
                                m_data.end_blit_ship_3_2[0] = False

                            # 2
                            if self.SIZE_SHIP == 2:
                                m_data.end_blit_ship_2_1[0] = False
                                m_data.end_blit_ship_2_2[0] = False
                                m_data.end_blit_ship_2_3[0] = False

                            #1
                            if self.SIZE_SHIP == 1:
                                m_data.end_blit_ship_1_1[0] = False
                                m_data.end_blit_ship_1_2[0] = False
                                m_data.end_blit_ship_1_3[0] = False
                                m_data.end_blit_ship_1_4[0] = False

                # ряд десятий третя клітинка
                elif  self.Y <= 395 + cell.HEIGHT and 265 + cell.HEIGHT:
                    if m_data.list_map_player[9][2] == 0:
                        self.X = 240 + self.LIST_SHIP_4 + 4 
                        self.Y = 414 
                        self.set_ship(set_row= 9, set_cell_start= 2)
                    if m_data.list_map_player[9][2] == 5:
                        if self.SET_SHIP == False:
                            self.X = self.X_START
                            self.Y = self.Y_START

                            if self.SIZE_SHIP == 3:
                                m_data.end_blit_ship_3_1[0] = False
                                m_data.end_blit_ship_3_2[0] = False

                            # 2
                            if self.SIZE_SHIP == 2:
                                m_data.end_blit_ship_2_1[0] = False
                                m_data.end_blit_ship_2_2[0] = False
                                m_data.end_blit_ship_2_3[0] = False

                            #1
                            if self.SIZE_SHIP == 1:
                                m_data.end_blit_ship_1_1[0] = False
                                m_data.end_blit_ship_1_2[0] = False
                                m_data.end_blit_ship_1_3[0] = False
                                m_data.end_blit_ship_1_4[0] = False

            # четверта клітинка
            if self.X >= 265 and self.X <= 265 + cell.WIDTH:
                # ряд перший четверта клітинка
                if self.Y <= 170 + cell.HEIGHT and 290 + cell.HEIGHT:
                    if m_data.list_map_player[0][3] == 0:
                        self.X = 265 + self.LIST_SHIP_4 + 6
                        self.Y = 171
                        self.set_ship(set_row= 0, set_cell_start= 3)
                    if m_data.list_map_player[0][3] == 5:
                        if self.SET_SHIP == False:
                            self.X = self.X_START
                            self.Y = self.Y_START
                            if self.SIZE_SHIP == 3:
                                m_data.end_blit_ship_3_1[0] = False
                                m_data.end_blit_ship_3_2[0] = False

                            # 2
                            if self.SIZE_SHIP == 2:
                                m_data.end_blit_ship_2_1[0] = False
                                m_data.end_blit_ship_2_2[0] = False
                                m_data.end_blit_ship_2_3[0] = False

                            #1
                            if self.SIZE_SHIP == 1:
                                m_data.end_blit_ship_1_1[0] = False
                                m_data.end_blit_ship_1_2[0] = False
                                m_data.end_blit_ship_1_3[0] = False
                                m_data.end_blit_ship_1_4[0] = False

                # ряд другий четверта клітинка
                elif self.Y <= 195 + cell.HEIGHT and 290 + cell.HEIGHT:
                    if m_data.list_map_player[1][3] == 0:
                        self.X = 265 + self.LIST_SHIP_4 + 6
                        self.Y = 198
                        self.set_ship(set_row= 1, set_cell_start= 3)
                    if m_data.list_map_player[1][3] == 5:
                        if self.SET_SHIP == False:
                            self.X = self.X_START
                            self.Y = self.Y_START
                            if self.SIZE_SHIP == 3:
                                m_data.end_blit_ship_3_1[0] = False
                                m_data.end_blit_ship_3_2[0] = False

                            # 2
                            if self.SIZE_SHIP == 2:
                                m_data.end_blit_ship_2_1[0] = False
                                m_data.end_blit_ship_2_2[0] = False
                                m_data.end_blit_ship_2_3[0] = False

                            #1
                            if self.SIZE_SHIP == 1:
                                m_data.end_blit_ship_1_1[0] = False
                                m_data.end_blit_ship_1_2[0] = False
                                m_data.end_blit_ship_1_3[0] = False
                                m_data.end_blit_ship_1_4[0] = False

                 # ряд третій четверта клітинка
                elif self.Y <= 220 + cell.HEIGHT and 290 + cell.HEIGHT:
                    if m_data.list_map_player[2][3] == 0:
                        self.X = 265 + self.LIST_SHIP_4 + 6
                        self.Y = 225
                        self.set_ship(set_row= 2, set_cell_start= 3)
                    if m_data.list_map_player[2][3] == 5:
                        if self.SET_SHIP == False:
                            self.X = self.X_START
                            self.Y = self.Y_START
                            if self.SIZE_SHIP == 3:
                                m_data.end_blit_ship_3_1[0] = False
                                m_data.end_blit_ship_3_2[0] = False

                            # 2
                            if self.SIZE_SHIP == 2:
                                m_data.end_blit_ship_2_1[0] = False
                                m_data.end_blit_ship_2_2[0] = False
                                m_data.end_blit_ship_2_3[0] = False

                            #1
                            if self.SIZE_SHIP == 1:
                                m_data.end_blit_ship_1_1[0] = False
                                m_data.end_blit_ship_1_2[0] = False
                                m_data.end_blit_ship_1_3[0] = False
                                m_data.end_blit_ship_1_4[0] = False

                 # ряд четвертий четверта клітинка
                elif self.Y <= 245 + cell.HEIGHT and 290 + cell.HEIGHT:
                    if m_data.list_map_player[3][3] == 0:
                        self.X = 265 + self.LIST_SHIP_4 + 6
                        self.Y = 252
                        self.set_ship(set_row= 3, set_cell_start= 3)
                    if m_data.list_map_player[3][3] == 5:
                        if self.SET_SHIP == False:
                            self.X = self.X_START
                            self.Y = self.Y_START

                            if self.SIZE_SHIP == 3:
                                m_data.end_blit_ship_3_1[0] = False
                                m_data.end_blit_ship_3_2[0] = False

                            # 2
                            if self.SIZE_SHIP == 2:
                                m_data.end_blit_ship_2_1[0] = False
                                m_data.end_blit_ship_2_2[0] = False
                                m_data.end_blit_ship_2_3[0] = False

                            #1
                            if self.SIZE_SHIP == 1:
                                m_data.end_blit_ship_1_1[0] = False
                                m_data.end_blit_ship_1_2[0] = False
                                m_data.end_blit_ship_1_3[0] = False
                                m_data.end_blit_ship_1_4[0] = False


                # ряд пʼятий четверта клітинка
                elif self.Y <= 270 + cell.HEIGHT and 290 + cell.HEIGHT:
                    if m_data.list_map_player[4][3] == 0:
                        self.X = 265 + self.LIST_SHIP_4 + 6
                        self.Y = 279
                        self.set_ship(set_row= 4, set_cell_start= 3)
                    if m_data.list_map_player[4][3] == 5:
                        if self.SET_SHIP == False:
                            self.X = self.X_START
                            self.Y = self.Y_START

                            if self.SIZE_SHIP == 3:
                                m_data.end_blit_ship_3_1[0] = False
                                m_data.end_blit_ship_3_2[0] = False

                            # 2
                            if self.SIZE_SHIP == 2:
                                m_data.end_blit_ship_2_1[0] = False
                                m_data.end_blit_ship_2_2[0] = False
                                m_data.end_blit_ship_2_3[0] = False

                            #1
                            if self.SIZE_SHIP == 1:
                                m_data.end_blit_ship_1_1[0] = False
                                m_data.end_blit_ship_1_2[0] = False
                                m_data.end_blit_ship_1_3[0] = False
                                m_data.end_blit_ship_1_4[0] = False

                # ряд шостий четверта клітинка
                elif self.Y <= 295 + cell.HEIGHT and 290 + cell.HEIGHT:
                    if m_data.list_map_player[5][3] == 0:
                        self.X = 265 + self.LIST_SHIP_4 + 6
                        self.Y = 306
                        self.set_ship(set_row= 5, set_cell_start= 3)
                    if m_data.list_map_player[5][3] == 5:
                        if self.SET_SHIP == False:
                            self.X = self.X_START
                            self.Y = self.Y_START

                            if self.SIZE_SHIP == 3:
                                m_data.end_blit_ship_3_1[0] = False
                                m_data.end_blit_ship_3_2[0] = False

                            # 2
                            if self.SIZE_SHIP == 2:
                                m_data.end_blit_ship_2_1[0] = False
                                m_data.end_blit_ship_2_2[0] = False
                                m_data.end_blit_ship_2_3[0] = False

                            #1
                            if self.SIZE_SHIP == 1:
                                m_data.end_blit_ship_1_1[0] = False
                                m_data.end_blit_ship_1_2[0] = False
                                m_data.end_blit_ship_1_3[0] = False
                                m_data.end_blit_ship_1_4[0] = False
                    
                # ряд сьомий четверта клітинка
                elif self.Y <= 320 + cell.HEIGHT and 290 + cell.HEIGHT:
                    if m_data.list_map_player[6][3] == 0:
                        self.X = 265 + self.LIST_SHIP_4 + 6
                        self.Y = 333
                        self.set_ship(set_row= 6, set_cell_start= 3)
                    if m_data.list_map_player[6][3] == 5:
                        if self.SET_SHIP == False:
                            self.X = self.X_START
                            self.Y = self.Y_START

                            if self.SIZE_SHIP == 3:
                                m_data.end_blit_ship_3_1[0] = False
                                m_data.end_blit_ship_3_2[0] = False

                            # 2
                            if self.SIZE_SHIP == 2:
                                m_data.end_blit_ship_2_1[0] = False
                                m_data.end_blit_ship_2_2[0] = False
                                m_data.end_blit_ship_2_3[0] = False

                            #1
                            if self.SIZE_SHIP == 1:
                                m_data.end_blit_ship_1_1[0] = False
                                m_data.end_blit_ship_1_2[0] = False
                                m_data.end_blit_ship_1_3[0] = False
                                m_data.end_blit_ship_1_4[0] = False

                # ряд восьмий четверта клітинка     
                elif self.Y <= 345 + cell.HEIGHT and 290 + cell.HEIGHT:
                    if m_data.list_map_player[7][3] == 0:
                        self.X = 265 + self.LIST_SHIP_4 + 6
                        self.Y = 360
                        self.set_ship(set_row= 7, set_cell_start= 3)
                    if m_data.list_map_player[7][3] == 5:
                        if self.SET_SHIP == False:
                            self.X = self.X_START
                            self.Y = self.Y_START

                            if self.SIZE_SHIP == 3:
                                m_data.end_blit_ship_3_1[0] = False
                                m_data.end_blit_ship_3_2[0] = False

                            # 2
                            if self.SIZE_SHIP == 2:
                                m_data.end_blit_ship_2_1[0] = False
                                m_data.end_blit_ship_2_2[0] = False
                                m_data.end_blit_ship_2_3[0] = False

                            #1
                            if self.SIZE_SHIP == 1:
                                m_data.end_blit_ship_1_1[0] = False
                                m_data.end_blit_ship_1_2[0] = False
                                m_data.end_blit_ship_1_3[0] = False
                                m_data.end_blit_ship_1_4[0] = False

                # ряд девʼятий четверта клітинка
                elif self.Y <= 370 + cell.HEIGHT and 290 + cell.HEIGHT:
                    if m_data.list_map_player[8][3] == 0:
                        self.X = 265 + self.LIST_SHIP_4 + 6
                        self.Y = 387
                        self.set_ship(set_row= 8, set_cell_start= 3)
                    if m_data.list_map_player[8][3] == 5:
                        if self.SET_SHIP == False:
                            self.X = self.X_START
                            self.Y = self.Y_START

                            if self.SIZE_SHIP == 3:
                                m_data.end_blit_ship_3_1[0] = False
                                m_data.end_blit_ship_3_2[0] = False

                            # 2
                            if self.SIZE_SHIP == 2:
                                m_data.end_blit_ship_2_1[0] = False
                                m_data.end_blit_ship_2_2[0] = False
                                m_data.end_blit_ship_2_3[0] = False

                            #1
                            if self.SIZE_SHIP == 1:
                                m_data.end_blit_ship_1_1[0] = False
                                m_data.end_blit_ship_1_2[0] = False
                                m_data.end_blit_ship_1_3[0] = False
                                m_data.end_blit_ship_1_4[0] = False

                # ряд десятий четверта клітинка
                elif  self.Y <= 395 + cell.HEIGHT and 290 + cell.HEIGHT:
                    if m_data.list_map_player[9][3] == 0:
                        self.X = 265 + self.LIST_SHIP_4 + 6
                        self.Y = 414
                        self.set_ship(set_row= 9, set_cell_start= 3)
                    if m_data.list_map_player[9][3] == 5:
                        if self.SET_SHIP == False:
                            self.X = self.X_START
                            self.Y = self.Y_START

                            if self.SIZE_SHIP == 3:
                                m_data.end_blit_ship_3_1[0] = False
                                m_data.end_blit_ship_3_2[0] = False

                            # 2
                            if self.SIZE_SHIP == 2:
                                m_data.end_blit_ship_2_1[0] = False
                                m_data.end_blit_ship_2_2[0] = False
                                m_data.end_blit_ship_2_3[0] = False

                            #1
                            if self.SIZE_SHIP == 1:
                                m_data.end_blit_ship_1_1[0] = False
                                m_data.end_blit_ship_1_2[0] = False
                                m_data.end_blit_ship_1_3[0] = False
                                m_data.end_blit_ship_1_4[0] = False

            # пʼята клітинка
            if self.X >= 290 and self.X <= 290 + cell.WIDTH:
                # ряд перший пʼята клітинка
                if self.Y <= 170 + cell.HEIGHT and 315 + cell.HEIGHT:
                    if m_data.list_map_player[0][4] == 0:
                        self.X = 290 + self.LIST_SHIP_4 + 8
                        self.Y = 171
                        self.set_ship(set_row= 0, set_cell_start= 4)
                    if m_data.list_map_player[0][4] == 5:
                        if self.SET_SHIP == False:
                            self.X = self.X_START
                            self.Y = self.Y_START

                            if self.SIZE_SHIP == 3:
                                m_data.end_blit_ship_3_1[0] = False
                                m_data.end_blit_ship_3_2[0] = False

                            # 2
                            if self.SIZE_SHIP == 2:
                                m_data.end_blit_ship_2_1[0] = False
                                m_data.end_blit_ship_2_2[0] = False
                                m_data.end_blit_ship_2_3[0] = False

                            #1
                            if self.SIZE_SHIP == 1:
                                m_data.end_blit_ship_1_1[0] = False
                                m_data.end_blit_ship_1_2[0] = False
                                m_data.end_blit_ship_1_3[0] = False
                                m_data.end_blit_ship_1_4[0] = False

                # ряд другий пʼята клітинка
                elif self.Y <= 195 + cell.HEIGHT and 315 + cell.HEIGHT:
                    if m_data.list_map_player[1][4] == 0:
                        self.X = 290 + self.LIST_SHIP_4 + 8 
                        self.Y = 198
                        self.set_ship(set_row= 1, set_cell_start= 4)
                    if m_data.list_map_player[1][4] == 5:
                        if self.SET_SHIP == False:
                            self.X = self.X_START
                            self.Y = self.Y_START

                            if self.SIZE_SHIP == 3:
                                m_data.end_blit_ship_3_1[0] = False
                                m_data.end_blit_ship_3_2[0] = False

                            # 2
                            if self.SIZE_SHIP == 2:
                                m_data.end_blit_ship_2_1[0] = False
                                m_data.end_blit_ship_2_2[0] = False
                                m_data.end_blit_ship_2_3[0] = False

                            #1
                            if self.SIZE_SHIP == 1:
                                m_data.end_blit_ship_1_1[0] = False
                                m_data.end_blit_ship_1_2[0] = False
                                m_data.end_blit_ship_1_3[0] = False
                                m_data.end_blit_ship_1_4[0] = False

                # ряд третій пʼята клітинка
                elif self.Y <= 220 + cell.HEIGHT and 315 + cell.HEIGHT:
                    if m_data.list_map_player[2][4] == 0:
                        self.X = 290 + self.LIST_SHIP_4 + 8 
                        self.Y = 225
                        self.set_ship(set_row= 2, set_cell_start= 4)
                    if m_data.list_map_player[2][4] == 5:
                        if self.SET_SHIP == False:
                            self.X = self.X_START
                            self.Y = self.Y_START

                            if self.SIZE_SHIP == 3:
                                m_data.end_blit_ship_3_1[0] = False
                                m_data.end_blit_ship_3_2[0] = False

                            # 2
                            if self.SIZE_SHIP == 2:
                                m_data.end_blit_ship_2_1[0] = False
                                m_data.end_blit_ship_2_2[0] = False
                                m_data.end_blit_ship_2_3[0] = False

                            #1
                            if self.SIZE_SHIP == 1:
                                m_data.end_blit_ship_1_1[0] = False
                                m_data.end_blit_ship_1_2[0] = False
                                m_data.end_blit_ship_1_3[0] = False
                                m_data.end_blit_ship_1_4[0] = False

                # ряд четвертий  пʼята клітинка
                elif self.Y <= 245 + cell.HEIGHT and 315 + cell.HEIGHT:
                    if m_data.list_map_player[3][4] == 0:
                        self.X = 290 + self.LIST_SHIP_4 + 8 
                        self.Y = 252
                        self.set_ship(set_row= 3, set_cell_start= 4)
                    if m_data.list_map_player[3][4] == 5:
                        if self.SET_SHIP == False:
                            self.X = self.X_START
                            self.Y = self.Y_START

                            if self.SIZE_SHIP == 3:
                                m_data.end_blit_ship_3_1[0] = False
                                m_data.end_blit_ship_3_2[0] = False

                            # 2
                            if self.SIZE_SHIP == 2:
                                m_data.end_blit_ship_2_1[0] = False
                                m_data.end_blit_ship_2_2[0] = False
                                m_data.end_blit_ship_2_3[0] = False

                            #1
                            if self.SIZE_SHIP == 1:
                                m_data.end_blit_ship_1_1[0] = False
                                m_data.end_blit_ship_1_2[0] = False
                                m_data.end_blit_ship_1_3[0] = False
                                m_data.end_blit_ship_1_4[0] = False

                # ряд пʼятий  пʼята клітинка
                elif self.Y <= 270 + cell.HEIGHT and 315 + cell.HEIGHT:
                    if m_data.list_map_player[4][4] == 0:
                        self.X = 290 + self.LIST_SHIP_4 + 8 
                        self.Y = 279
                        self.set_ship(set_row= 4, set_cell_start= 4)
                    if m_data.list_map_player[4][4] == 5:
                        if self.SET_SHIP == False:
                            self.X = self.X_START
                            self.Y = self.Y_START

                            if self.SIZE_SHIP == 3:
                                m_data.end_blit_ship_3_1[0] = False
                                m_data.end_blit_ship_3_2[0] = False

                            # 2
                            if self.SIZE_SHIP == 2:
                                m_data.end_blit_ship_2_1[0] = False
                                m_data.end_blit_ship_2_2[0] = False
                                m_data.end_blit_ship_2_3[0] = False

                            #1
                            if self.SIZE_SHIP == 1:
                                m_data.end_blit_ship_1_1[0] = False
                                m_data.end_blit_ship_1_2[0] = False
                                m_data.end_blit_ship_1_3[0] = False
                                m_data.end_blit_ship_1_4[0] = False

                # ряд шостий пʼята клітинка
                elif  self.Y <= 295 + cell.HEIGHT and 315 + cell.HEIGHT:
                    if m_data.list_map_player[5][4] == 0:
                        self.X = 290 + self.LIST_SHIP_4 + 8 
                        self.Y = 306
                        self.set_ship(set_row= 5, set_cell_start= 4)
                    if m_data.list_map_player[5][4] == 5:
                        if self.SET_SHIP == False:
                            self.X = self.X_START
                            self.Y = self.Y_START

                            if self.SIZE_SHIP == 3:
                                m_data.end_blit_ship_3_1[0] = False
                                m_data.end_blit_ship_3_2[0] = False

                            # 2
                            if self.SIZE_SHIP == 2:
                                m_data.end_blit_ship_2_1[0] = False
                                m_data.end_blit_ship_2_2[0] = False
                                m_data.end_blit_ship_2_3[0] = False

                            #1
                            if self.SIZE_SHIP == 1:
                                m_data.end_blit_ship_1_1[0] = False
                                m_data.end_blit_ship_1_2[0] = False
                                m_data.end_blit_ship_1_3[0] = False
                                m_data.end_blit_ship_1_4[0] = False

                # ряд сьомий пʼята клітинка
                elif  self.Y <= 320 + cell.HEIGHT and 315 + cell.HEIGHT:
                    if m_data.list_map_player[6][4] == 0:
                        self.X = 290 + self.LIST_SHIP_4 + 8
                        self.Y = 333
                        self.set_ship(set_row= 6, set_cell_start= 4)
                    if m_data.list_map_player[6][4] == 5:
                        if self.SET_SHIP == False:
                            self.X = self.X_START
                            self.Y = self.Y_START

                            if self.SIZE_SHIP == 3:
                                m_data.end_blit_ship_3_1[0] = False
                                m_data.end_blit_ship_3_2[0] = False

                            # 2
                            if self.SIZE_SHIP == 2:
                                m_data.end_blit_ship_2_1[0] = False
                                m_data.end_blit_ship_2_2[0] = False
                                m_data.end_blit_ship_2_3[0] = False

                            #1
                            if self.SIZE_SHIP == 1:
                                m_data.end_blit_ship_1_1[0] = False
                                m_data.end_blit_ship_1_2[0] = False
                                m_data.end_blit_ship_1_3[0] = False
                                m_data.end_blit_ship_1_4[0] = False
                
                # ряд восьмий пʼята клітинка
                elif  self.Y <= 345 + cell.HEIGHT and 315 + cell.HEIGHT:
                    if m_data.list_map_player[7][4] == 0:
                        self.X = 290 + self.LIST_SHIP_4 + 8 
                        self.Y = 360
                        self.set_ship(set_row= 7, set_cell_start= 4)
                    if m_data.list_map_player[7][4] == 5:
                        if self.SET_SHIP == False:
                            self.X = self.X_START
                            self.Y = self.Y_START

                            if self.SIZE_SHIP == 3:
                                m_data.end_blit_ship_3_1[0] = False
                                m_data.end_blit_ship_3_2[0] = False

                            # 2
                            if self.SIZE_SHIP == 2:
                                m_data.end_blit_ship_2_1[0] = False
                                m_data.end_blit_ship_2_2[0] = False
                                m_data.end_blit_ship_2_3[0] = False

                            #1
                            if self.SIZE_SHIP == 1:
                                m_data.end_blit_ship_1_1[0] = False
                                m_data.end_blit_ship_1_2[0] = False
                                m_data.end_blit_ship_1_3[0] = False
                                m_data.end_blit_ship_1_4[0] = False

                # ряд девʼятий пʼята клітинка
                elif  self.Y <= 370 + cell.HEIGHT and 315 + cell.HEIGHT:
                    if m_data.list_map_player[8][4] == 0:
                        self.X = 290 + self.LIST_SHIP_4 + 8 
                        self.Y = 387
                        self.set_ship(set_row= 8, set_cell_start= 4)
                    if m_data.list_map_player[8][4] == 5:
                        if self.SET_SHIP == False:
                            self.X = self.X_START
                            self.Y = self.Y_START

                            if self.SIZE_SHIP == 3:
                                m_data.end_blit_ship_3_1[0] = False
                                m_data.end_blit_ship_3_2[0] = False

                            # 2
                            if self.SIZE_SHIP == 2:
                                m_data.end_blit_ship_2_1[0] = False
                                m_data.end_blit_ship_2_2[0] = False
                                m_data.end_blit_ship_2_3[0] = False

                            #1
                            if self.SIZE_SHIP == 1:
                                m_data.end_blit_ship_1_1[0] = False
                                m_data.end_blit_ship_1_2[0] = False
                                m_data.end_blit_ship_1_3[0] = False
                                m_data.end_blit_ship_1_4[0] = False

                # ряд десятий пʼята клітинка
                elif  self.Y <= 395 + cell.HEIGHT and 315 + cell.HEIGHT:
                    if m_data.list_map_player[9][4] == 0:
                        self.X = 290 + self.LIST_SHIP_4 + 8 
                        self.Y = 414
                        self.set_ship(set_row= 9, set_cell_start= 4)
                    if m_data.list_map_player[9][4] == 5:
                        if self.SET_SHIP == False:
                            self.X = self.X_START
                            self.Y = self.Y_START

                            if self.SIZE_SHIP == 3:
                                m_data.end_blit_ship_3_1[0] = False
                                m_data.end_blit_ship_3_2[0] = False

                            # 2
                            if self.SIZE_SHIP == 2:
                                m_data.end_blit_ship_2_1[0] = False
                                m_data.end_blit_ship_2_2[0] = False
                                m_data.end_blit_ship_2_3[0] = False

                            #1
                            if self.SIZE_SHIP == 1:
                                m_data.end_blit_ship_1_1[0] = False
                                m_data.end_blit_ship_1_2[0] = False
                                m_data.end_blit_ship_1_3[0] = False
                                m_data.end_blit_ship_1_4[0] = False

            # шоста клітинка
            if self.X >= 315 and self.X <= 315 + cell.WIDTH:
                # ряд перший шоста клітинка
                if self.Y <= 170 + cell.HEIGHT and 500 + cell.HEIGHT:
                    if m_data.list_map_player[0][5] == 0:
                        self.X = 315 + self.LIST_SHIP_4 + 10
                        self.Y = 171
                        self.set_ship(set_row= 0, set_cell_start= 5)
                    if m_data.list_map_player[0][5] == 5:
                        if self.SET_SHIP == False:
                            self.X = self.X_START
                            self.Y = self.Y_START

                            if self.SIZE_SHIP == 3:
                                m_data.end_blit_ship_3_1[0] = False
                                m_data.end_blit_ship_3_2[0] = False

                            # 2
                            if self.SIZE_SHIP == 2:
                                m_data.end_blit_ship_2_1[0] = False
                                m_data.end_blit_ship_2_2[0] = False
                                m_data.end_blit_ship_2_3[0] = False

                            #1
                            if self.SIZE_SHIP == 1:
                                m_data.end_blit_ship_1_1[0] = False
                                m_data.end_blit_ship_1_2[0] = False
                                m_data.end_blit_ship_1_3[0] = False
                                m_data.end_blit_ship_1_4[0] = False

                # ряд другий шоста клітинка
                elif self.Y <= 195 + cell.HEIGHT and 500 + cell.HEIGHT:
                    if m_data.list_map_player[1][5] == 0:
                        self.X = 315 + self.LIST_SHIP_4 + 10 
                        self.Y = 198
                        self.set_ship(set_row= 1, set_cell_start= 5)
                    if m_data.list_map_player[1][5] in m_data.number:
                        if self.SET_SHIP == False:
                            self.X = self.X_START
                            self.Y = self.Y_START

                            if self.SIZE_SHIP == 3:
                                m_data.end_blit_ship_3_1[0] = False
                                m_data.end_blit_ship_3_2[0] = False

                            # 2
                            if self.SIZE_SHIP == 2:
                                m_data.end_blit_ship_2_1[0] = False
                                m_data.end_blit_ship_2_2[0] = False
                                m_data.end_blit_ship_2_3[0] = False

                            #1
                            if self.SIZE_SHIP == 1:
                                m_data.end_blit_ship_1_1[0] = False
                                m_data.end_blit_ship_1_2[0] = False
                                m_data.end_blit_ship_1_3[0] = False
                                m_data.end_blit_ship_1_4[0] = False

                # ряд третій шоста клітинка
                elif self.Y <= 220 + cell.HEIGHT and 500 + cell.HEIGHT:
                    if m_data.list_map_player[2][5] == 0:
                        self.X = 315 + self.LIST_SHIP_4 + 10 
                        self.Y = 225
                        self.set_ship(set_row= 2, set_cell_start= 5)
                    if m_data.list_map_player[2][5] == 5:
                        if self.SET_SHIP == False:
                            self.X = self.X_START
                            self.Y = self.Y_START

                            if self.SIZE_SHIP == 3:
                                m_data.end_blit_ship_3_1[0] = False
                                m_data.end_blit_ship_3_2[0] = False

                            # 2
                            if self.SIZE_SHIP == 2:
                                m_data.end_blit_ship_2_1[0] = False
                                m_data.end_blit_ship_2_2[0] = False
                                m_data.end_blit_ship_2_3[0] = False

                            #1
                            if self.SIZE_SHIP == 1:
                                m_data.end_blit_ship_1_1[0] = False
                                m_data.end_blit_ship_1_2[0] = False
                                m_data.end_blit_ship_1_3[0] = False
                                m_data.end_blit_ship_1_4[0] = False

                # ряд четвертий  шоста клітинка
                elif self.Y <= 245 + cell.HEIGHT and 500 + cell.HEIGHT:
                    if m_data.list_map_player[3][5] == 0:
                        self.X = 315 + self.LIST_SHIP_4 + 10 
                        self.Y = 252
                        self.set_ship(set_row= 3, set_cell_start= 5)
                    if m_data.list_map_player[3][5] == 5:
                        if self.SET_SHIP == False:
                            self.X = self.X_START
                            self.Y = self.Y_START

                            if self.SIZE_SHIP == 3:
                                m_data.end_blit_ship_3_1[0] = False
                                m_data.end_blit_ship_3_2[0] = False

                            # 2
                            if self.SIZE_SHIP == 2:
                                m_data.end_blit_ship_2_1[0] = False
                                m_data.end_blit_ship_2_2[0] = False
                                m_data.end_blit_ship_2_3[0] = False

                            #1
                            if self.SIZE_SHIP == 1:
                                m_data.end_blit_ship_1_1[0] = False
                                m_data.end_blit_ship_1_2[0] = False
                                m_data.end_blit_ship_1_3[0] = False
                                m_data.end_blit_ship_1_4[0] = False
                        

                # ряд пʼятий шоста клітинка
                elif self.Y <= 270 + cell.HEIGHT and 500 + cell.HEIGHT:
                    if m_data.list_map_player[4][5] == 0:
                        self.X = 315 + self.LIST_SHIP_4 + 10 
                        self.Y = 279
                        self.set_ship(set_row= 4, set_cell_start= 5)
                    if m_data.list_map_player[4][5] == 5:
                        if self.SET_SHIP == False:
                            self.X = self.X_START
                            self.Y = self.Y_START

                            if self.SIZE_SHIP == 3:
                                m_data.end_blit_ship_3_1[0] = False
                                m_data.end_blit_ship_3_2[0] = False

                            # 2
                            if self.SIZE_SHIP == 2:
                                m_data.end_blit_ship_2_1[0] = False
                                m_data.end_blit_ship_2_2[0] = False
                                m_data.end_blit_ship_2_3[0] = False

                            #1
                            if self.SIZE_SHIP == 1:
                                m_data.end_blit_ship_1_1[0] = False
                                m_data.end_blit_ship_1_2[0] = False
                                m_data.end_blit_ship_1_3[0] = False
                                m_data.end_blit_ship_1_4[0] = False

                # ряд шостий шоста клітинка
                elif  self.Y <= 295 + cell.HEIGHT and 500 + cell.HEIGHT:
                    if m_data.list_map_player[5][5] == 0:
                        self.X = 315 + self.LIST_SHIP_4 + 10 
                        self.Y = 306
                        self.set_ship(set_row= 5, set_cell_start= 5)
                    if m_data.list_map_player[5][5] == 5:
                        if self.SET_SHIP == False:
                            self.X = self.X_START
                            self.Y = self.Y_START

                            if self.SIZE_SHIP == 3:
                                m_data.end_blit_ship_3_1[0] = False
                                m_data.end_blit_ship_3_2[0] = False

                            # 2
                            if self.SIZE_SHIP == 2:
                                m_data.end_blit_ship_2_1[0] = False
                                m_data.end_blit_ship_2_2[0] = False
                                m_data.end_blit_ship_2_3[0] = False

                            #1
                            if self.SIZE_SHIP == 1:
                                m_data.end_blit_ship_1_1[0] = False
                                m_data.end_blit_ship_1_2[0] = False
                                m_data.end_blit_ship_1_3[0] = False
                                m_data.end_blit_ship_1_4[0] = False

                # ряд сьомий шоста клітинка
                elif  self.Y <= 320 + cell.HEIGHT and 500 + cell.HEIGHT:
                    if m_data.list_map_player[6][5] == 0:
                        self.X = 315 + self.LIST_SHIP_4 + 10 
                        self.Y = 333
                        self.set_ship(set_row= 6, set_cell_start= 5)
                    if m_data.list_map_player[6][5] == 5:
                        if self.SET_SHIP == False:
                            self.X = self.X_START
                            self.Y = self.Y_START

                            if self.SIZE_SHIP == 3:
                                m_data.end_blit_ship_3_1[0] = False
                                m_data.end_blit_ship_3_2[0] = False

                            # 2
                            if self.SIZE_SHIP == 2:
                                m_data.end_blit_ship_2_1[0] = False
                                m_data.end_blit_ship_2_2[0] = False
                                m_data.end_blit_ship_2_3[0] = False

                            #1
                            if self.SIZE_SHIP == 1:
                                m_data.end_blit_ship_1_1[0] = False
                                m_data.end_blit_ship_1_2[0] = False
                                m_data.end_blit_ship_1_3[0] = False
                                m_data.end_blit_ship_1_4[0] = False

               # ряд восьмий шоста клітинка
                elif  self.Y <= 345 + cell.HEIGHT and 500 + cell.HEIGHT:
                    if m_data.list_map_player[7][5] == 0:
                        self.X = 315 + self.LIST_SHIP_4 + 10 
                        self.Y = 360
                        self.set_ship(set_row= 7, set_cell_start= 5)
                    if m_data.list_map_player[7][5] == 5:
                        if self.SET_SHIP == False:
                            self.X = self.X_START    
                            self.Y = self.Y_START

                            if self.SIZE_SHIP == 3:
                                m_data.end_blit_ship_3_1[0] = False
                                m_data.end_blit_ship_3_2[0] = False

                            # 2
                            if self.SIZE_SHIP == 2:
                                m_data.end_blit_ship_2_1[0] = False
                                m_data.end_blit_ship_2_2[0] = False
                                m_data.end_blit_ship_2_3[0] = False

                            #1
                            if self.SIZE_SHIP == 1:
                                m_data.end_blit_ship_1_1[0] = False
                                m_data.end_blit_ship_1_2[0] = False
                                m_data.end_blit_ship_1_3[0] = False
                                m_data.end_blit_ship_1_4[0] = False
                
                # ряд девʼятий шоста клітинка
                elif  self.Y <= 370 + cell.HEIGHT and 500 + cell.HEIGHT:
                    if m_data.list_map_player[8][5] == 0:
                        self.X = 315 + self.LIST_SHIP_4 + 10
                        self.Y = 387
                        self.set_ship(set_row= 8, set_cell_start= 5)
                    if m_data.list_map_player[8][5] == 5:
                        if self.SET_SHIP == False:
                            self.X = self.X_START    
                            self.Y = self.Y_START

                            if self.SIZE_SHIP == 3:
                                m_data.end_blit_ship_3_1[0] = False
                                m_data.end_blit_ship_3_2[0] = False

                            # 2
                            if self.SIZE_SHIP == 2:
                                m_data.end_blit_ship_2_1[0] = False
                                m_data.end_blit_ship_2_2[0] = False
                                m_data.end_blit_ship_2_3[0] = False

                            #1
                            if self.SIZE_SHIP == 1:
                                m_data.end_blit_ship_1_1[0] = False
                                m_data.end_blit_ship_1_2[0] = False
                                m_data.end_blit_ship_1_3[0] = False
                                m_data.end_blit_ship_1_4[0] = False

                # ряд десятий шоста клітинка
                elif  self.Y <= 395 + cell.HEIGHT and 500 + cell.HEIGHT:
                    if m_data.list_map_player[9][5] == 0:
                        self.X = 315 + self.LIST_SHIP_4 + 10 
                        self.Y = 414
                        self.set_ship(set_row= 9, set_cell_start= 5)
                    if m_data.list_map_player[9][5] == 5:
                        if self.SET_SHIP == False:
                            self.X = self.X_START    
                            self.Y = self.Y_START

                            if self.SIZE_SHIP == 3:
                                m_data.end_blit_ship_3_1[0] = False
                                m_data.end_blit_ship_3_2[0] = False

                            # 2
                            if self.SIZE_SHIP == 2:
                                m_data.end_blit_ship_2_1[0] = False
                                m_data.end_blit_ship_2_2[0] = False
                                m_data.end_blit_ship_2_3[0] = False

                            #1
                            if self.SIZE_SHIP == 1:
                                m_data.end_blit_ship_1_1[0] = False
                                m_data.end_blit_ship_1_2[0] = False
                                m_data.end_blit_ship_1_3[0] = False
                                m_data.end_blit_ship_1_4[0] = False
                    
            # сьомий стовбчик
            if self.X >= 340 and self.X <= 340 + cell.WIDTH:
                # перший рядок сьома клітинка
                if self.Y <= 170 + cell.HEIGHT and 365 + cell.HEIGHT:
                    if m_data.list_map_player[0][6] == 0:
                        self.X = 340 + self.LIST_SHIP_4 + 12
                        self.Y = 171
                        self.set_ship(set_row= 0, set_cell_start= 6)
                    if m_data.list_map_player[0][6] == 5:
                        if self.SET_SHIP == False:
                            self.X = self.X_START    
                            self.Y = self.Y_START

                            if self.SIZE_SHIP == 3:
                                m_data.end_blit_ship_3_1[0] = False
                                m_data.end_blit_ship_3_2[0] = False

                            # 2
                            if self.SIZE_SHIP == 2:
                                m_data.end_blit_ship_2_1[0] = False
                                m_data.end_blit_ship_2_2[0] = False
                                m_data.end_blit_ship_2_3[0] = False

                            #1
                            if self.SIZE_SHIP == 1:
                                m_data.end_blit_ship_1_1[0] = False
                                m_data.end_blit_ship_1_2[0] = False
                                m_data.end_blit_ship_1_3[0] = False
                                m_data.end_blit_ship_1_4[0] = False
    
                # другий рядок сьома клітинка
                elif self.Y <= 195 + cell.HEIGHT and 525 + cell.HEIGHT:
                    if m_data.list_map_player[1][6] == 0:
                        self.X = 340 + self.LIST_SHIP_4 + 12
                        self.Y = 198
                        self.set_ship(set_row= 1, set_cell_start= 6)
                    if m_data.list_map_player[1][6] == 5:
                        if self.SET_SHIP == False:
                            self.X = self.X_START    
                            self.Y = self.Y_START

                            if self.SIZE_SHIP == 3:
                                m_data.end_blit_ship_3_1[0] = False
                                m_data.end_blit_ship_3_2[0] = False

                            # 2
                            if self.SIZE_SHIP == 2:
                                m_data.end_blit_ship_2_1[0] = False
                                m_data.end_blit_ship_2_2[0] = False
                                m_data.end_blit_ship_2_3[0] = False

                            #1
                            if self.SIZE_SHIP == 1:
                                m_data.end_blit_ship_1_1[0] = False
                                m_data.end_blit_ship_1_2[0] = False
                                m_data.end_blit_ship_1_3[0] = False
                                m_data.end_blit_ship_1_4[0] = False


                # третій рядок сьома клітинка
                elif self.Y <= 220 + cell.HEIGHT and 525 + cell.HEIGHT:
                    if m_data.list_map_player[2][6] == 0:
                        self.X = 340 + self.LIST_SHIP_4 + 12
                        self.Y = 225
                        self.set_ship(set_row= 2, set_cell_start= 6)
                    if m_data.list_map_player[2][6] == 5:
                        if self.SET_SHIP == False:
                            self.X = self.X_START    
                            self.Y = self.Y_START

                            if self.SIZE_SHIP == 3:
                                m_data.end_blit_ship_3_1[0] = False
                                m_data.end_blit_ship_3_2[0] = False

                            # 2
                            if self.SIZE_SHIP == 2:
                                m_data.end_blit_ship_2_1[0] = False
                                m_data.end_blit_ship_2_2[0] = False
                                m_data.end_blit_ship_2_3[0] = False

                            #1
                            if self.SIZE_SHIP == 1:
                                m_data.end_blit_ship_1_1[0] = False
                                m_data.end_blit_ship_1_2[0] = False
                                m_data.end_blit_ship_1_3[0] = False
                                m_data.end_blit_ship_1_4[0] = False

                # четвертий рядок сьома клітинка
                elif self.Y <= 245 + cell.HEIGHT and 525 + cell.HEIGHT:
                    if m_data.list_map_player[3][6] == 0:
                        self.X = 340 + self.LIST_SHIP_4 + 12
                        self.Y = 252
                        self.set_ship(set_row= 3, set_cell_start= 6)
                    if m_data.list_map_player[3][6] == 5:
                        if self.SET_SHIP == False:
                            self.X = self.X_START    
                            self.Y = self.Y_START

                            if self.SIZE_SHIP == 3:
                                m_data.end_blit_ship_3_1[0] = False
                                m_data.end_blit_ship_3_2[0] = False

                            # 2
                            if self.SIZE_SHIP == 2:
                                m_data.end_blit_ship_2_1[0] = False
                                m_data.end_blit_ship_2_2[0] = False
                                m_data.end_blit_ship_2_3[0] = False

                            #1
                            if self.SIZE_SHIP == 1:
                                m_data.end_blit_ship_1_1[0] = False
                                m_data.end_blit_ship_1_2[0] = False
                                m_data.end_blit_ship_1_3[0] = False
                                m_data.end_blit_ship_1_4[0] = False

                # пʼятий  рядок сьома клітинка
                elif self.Y <= 270 + cell.HEIGHT and 525 + cell.HEIGHT:
                    if m_data.list_map_player[4][6] == 0:
                        self.X = 340 + self.LIST_SHIP_4 + 12
                        self.Y = 279
                        self.set_ship(set_row= 4, set_cell_start= 6)
                    if m_data.list_map_player[4][6] == 5:
                        if self.SET_SHIP == False:
                            self.X = self.X_START    
                            self.Y = self.Y_START

                            if self.SIZE_SHIP == 3:
                                m_data.end_blit_ship_3_1[0] = False
                                m_data.end_blit_ship_3_2[0] = False

                            # 2
                            if self.SIZE_SHIP == 2:
                                m_data.end_blit_ship_2_1[0] = False
                                m_data.end_blit_ship_2_2[0] = False
                                m_data.end_blit_ship_2_3[0] = False

                            #1
                            if self.SIZE_SHIP == 1:
                                m_data.end_blit_ship_1_1[0] = False
                                m_data.end_blit_ship_1_2[0] = False
                                m_data.end_blit_ship_1_3[0] = False
                                m_data.end_blit_ship_1_4[0] = False

                # шостий рядок сьома клітинка
                elif  self.Y <= 295 + cell.HEIGHT and 525 + cell.HEIGHT:
                    if m_data.list_map_player[5][6] == 0:
                        self.X = 340 + self.LIST_SHIP_4 + 12
                        self.Y = 306
                        self.set_ship(set_row= 5, set_cell_start= 6)
                    if m_data.list_map_player[5][6] == 5:
                        if self.SET_SHIP == False:
                            self.X = self.X_START    
                            self.Y = self.Y_START

                            if self.SIZE_SHIP == 3:
                                m_data.end_blit_ship_3_1[0] = False
                                m_data.end_blit_ship_3_2[0] = False

                            # 2
                            if self.SIZE_SHIP == 2:
                                m_data.end_blit_ship_2_1[0] = False
                                m_data.end_blit_ship_2_2[0] = False
                                m_data.end_blit_ship_2_3[0] = False

                            #1
                            if self.SIZE_SHIP == 1:
                                m_data.end_blit_ship_1_1[0] = False
                                m_data.end_blit_ship_1_2[0] = False
                                m_data.end_blit_ship_1_3[0] = False
                                m_data.end_blit_ship_1_4[0] = False
                        
                # сьомий рядок сьома клітинка
                elif  self.Y <= 320 + cell.HEIGHT and 525 + cell.HEIGHT:
                    if m_data.list_map_player[6][6] == 0:
                        self.X = 340 + self.LIST_SHIP_4 + 12
                        self.Y = 333
                        self.set_ship(set_row= 6, set_cell_start= 6)
                    if m_data.list_map_player[6][6] == 5:
                        if self.SET_SHIP == False:
                            self.X = self.X_START    
                            self.Y = self.Y_START

                            if self.SIZE_SHIP == 3:
                                m_data.end_blit_ship_3_1[0] = False
                                m_data.end_blit_ship_3_2[0] = False

                            # 2
                            if self.SIZE_SHIP == 2:
                                m_data.end_blit_ship_2_1[0] = False
                                m_data.end_blit_ship_2_2[0] = False
                                m_data.end_blit_ship_2_3[0] = False

                            #1
                            if self.SIZE_SHIP == 1:
                                m_data.end_blit_ship_1_1[0] = False
                                m_data.end_blit_ship_1_2[0] = False
                                m_data.end_blit_ship_1_3[0] = False
                                m_data.end_blit_ship_1_4[0] = False

               # восьмий рядок сьома клітинка
                elif  self.Y <= 345 + cell.HEIGHT and 525 + cell.HEIGHT:
                    if m_data.list_map_player[7][6] == 0:
                        self.X = 340 + self.LIST_SHIP_4 + 12
                        self.Y = 360
                        self.set_ship(set_row= 7, set_cell_start= 6)
                    if m_data.list_map_player[7][6] == 5:
                        if self.SET_SHIP == False:
                            self.X = self.X_START    
                            self.Y = self.Y_START

                            if self.SIZE_SHIP == 3:
                                m_data.end_blit_ship_3_1[0] = False
                                m_data.end_blit_ship_3_2[0] = False

                            # 2
                            if self.SIZE_SHIP == 2:
                                m_data.end_blit_ship_2_1[0] = False
                                m_data.end_blit_ship_2_2[0] = False
                                m_data.end_blit_ship_2_3[0] = False

                            #1
                            if self.SIZE_SHIP == 1:
                                m_data.end_blit_ship_1_1[0] = False
                                m_data.end_blit_ship_1_2[0] = False
                                m_data.end_blit_ship_1_3[0] = False
                                m_data.end_blit_ship_1_4[0] = False

                # девʼятий рядок сьома клітинка
                elif  self.Y <= 370 + cell.HEIGHT and 525 + cell.HEIGHT:
                    if m_data.list_map_player[8][6] == 0:
                        self.X = 340 + self.LIST_SHIP_4 + 12
                        self.Y = 387
                        self.set_ship(set_row= 8, set_cell_start= 6)
                    if m_data.list_map_player[8][6] == 5:
                        if self.SET_SHIP == False:
                            self.X = self.X_START    
                            self.Y = self.Y_START

                            if self.SIZE_SHIP == 3:
                                m_data.end_blit_ship_3_1[0] = False
                                m_data.end_blit_ship_3_2[0] = False

                            # 2
                            if self.SIZE_SHIP == 2:
                                m_data.end_blit_ship_2_1[0] = False
                                m_data.end_blit_ship_2_2[0] = False
                                m_data.end_blit_ship_2_3[0] = False

                            #1
                            if self.SIZE_SHIP == 1:
                                m_data.end_blit_ship_1_1[0] = False
                                m_data.end_blit_ship_1_2[0] = False
                                m_data.end_blit_ship_1_3[0] = False
                                m_data.end_blit_ship_1_4[0] = False

                # десятий рядок сьома клітинка
                elif  self.Y <= 395 + cell.HEIGHT and 525 + cell.HEIGHT:
                    if m_data.list_map_player[9][6] == 0:
                        self.X = 340 + self.LIST_SHIP_4 + 12
                        self.Y = 414
                        self.set_ship(set_row= 9, set_cell_start= 6)
                    if m_data.list_map_player[9][6] == 5:
                        if self.SET_SHIP == False:
                            self.X = self.X_START    
                            self.Y = self.Y_START

                            if self.SIZE_SHIP == 3:
                                m_data.end_blit_ship_3_1[0] = False
                                m_data.end_blit_ship_3_2[0] = False

                            # 2
                            if self.SIZE_SHIP == 2:
                                m_data.end_blit_ship_2_1[0] = False
                                m_data.end_blit_ship_2_2[0] = False
                                m_data.end_blit_ship_2_3[0] = False

                            #1
                            if self.SIZE_SHIP == 1:
                                m_data.end_blit_ship_1_1[0] = False
                                m_data.end_blit_ship_1_2[0] = False
                                m_data.end_blit_ship_1_3[0] = False
                                m_data.end_blit_ship_1_4[0] = False

            # восьма клітнка
            if self.X >= 365 and self.X <= 365 + cell.WIDTH:
                # перший рядок восьма клітинка
                if self.Y <= 170 + cell.HEIGHT:
                    if m_data.list_map_player[0][7] == 0:
                        if self.SIZE_SHIP == 4:
                            self.X = self.X_START    
                            self.Y = self.Y_START
                            m_data.end_blit_ship_4[0] = False
                            
                        if self.SIZE_SHIP == 3:
                            self.X = 365 + self.LIST_SHIP_3 + 14 
                        if self.SIZE_SHIP == 2:
                            self.X = 365 + self.LIST_SHIP_2 + 14 
                        if self.SIZE_SHIP == 1:
                            self.X = 365 + self.LIST_SHIP_1 + 14 

                        self.Y = 171
                        self.set_ship(set_row= 0, set_cell_start= 7)
                    if m_data.list_map_player[0][7] == 5:
                        if self.SET_SHIP == False:
                            self.X = self.X_START    
                            self.Y = self.Y_START

                            if self.SIZE_SHIP == 3:
                                m_data.end_blit_ship_3_1[0] = False
                                m_data.end_blit_ship_3_2[0] = False

                            # 2
                            if self.SIZE_SHIP == 2:
                                m_data.end_blit_ship_2_1[0] = False
                                m_data.end_blit_ship_2_2[0] = False
                                m_data.end_blit_ship_2_3[0] = False

                            #1
                            if self.SIZE_SHIP == 1:
                                m_data.end_blit_ship_1_1[0] = False
                                m_data.end_blit_ship_1_2[0] = False
                                m_data.end_blit_ship_1_3[0] = False
                                m_data.end_blit_ship_1_4[0] = False
                
                # другий рядок восьма клітинка
                elif self.Y <= 195 + cell.HEIGHT:
                    if m_data.list_map_player[1][7] == 0:
                        if self.SIZE_SHIP == 4:
                            self.X = self.X_START    
                            self.Y = self.Y_START
                            m_data.end_blit_ship_4[0] = False

                        if self.SIZE_SHIP == 3:
                            self.X = 365 + self.LIST_SHIP_3 + 14 
                        if self.SIZE_SHIP == 2:
                            self.X = 365 + self.LIST_SHIP_2 + 14 
                        if self.SIZE_SHIP == 1:
                            self.X = 365 + self.LIST_SHIP_1 + 14 
                        self.Y = 198
                        self.set_ship(set_row= 1, set_cell_start= 7)
                    if m_data.list_map_player[1][7] == 5:
                        if self.SET_SHIP == False:
                            self.X = self.X_START    
                            self.Y = self.Y_START

                            if self.SIZE_SHIP == 3:
                                m_data.end_blit_ship_3_1[0] = False
                                m_data.end_blit_ship_3_2[0] = False

                            # 2
                            if self.SIZE_SHIP == 2:
                                m_data.end_blit_ship_2_1[0] = False
                                m_data.end_blit_ship_2_2[0] = False
                                m_data.end_blit_ship_2_3[0] = False

                            #1
                            if self.SIZE_SHIP == 1:
                                m_data.end_blit_ship_1_1[0] = False
                                m_data.end_blit_ship_1_2[0] = False
                                m_data.end_blit_ship_1_3[0] = False
                                m_data.end_blit_ship_1_4[0] = False
                
                # третій рядок восьма клітинка
                elif self.Y <= 220 + cell.HEIGHT:
                    if m_data.list_map_player[2][7] == 0:
                        if self.SIZE_SHIP == 4:
                            self.X = self.X_START    
                            self.Y = self.Y_START
                            m_data.end_blit_ship_4[0] = False
                        if self.SIZE_SHIP == 3:
                            self.X = 365 + self.LIST_SHIP_3 + 14 
                        if self.SIZE_SHIP == 2:
                            self.X = 365 + self.LIST_SHIP_2 + 14 
                        if self.SIZE_SHIP == 1:
                            self.X = 365 + self.LIST_SHIP_1 + 14 
                        self.Y = 225
                        self.set_ship(set_row= 2, set_cell_start= 7)
                    if m_data.list_map_player[2][7] == 5:
                        if self.SET_SHIP == False:
                            self.X = self.X_START    
                            self.Y = self.Y_START

                            if self.SIZE_SHIP == 3:
                                m_data.end_blit_ship_3_1[0] = False
                                m_data.end_blit_ship_3_2[0] = False

                            # 2
                            if self.SIZE_SHIP == 2:
                                m_data.end_blit_ship_2_1[0] = False
                                m_data.end_blit_ship_2_2[0] = False
                                m_data.end_blit_ship_2_3[0] = False

                            #1
                            if self.SIZE_SHIP == 1:
                                m_data.end_blit_ship_1_1[0] = False
                                m_data.end_blit_ship_1_2[0] = False
                                m_data.end_blit_ship_1_3[0] = False
                                m_data.end_blit_ship_1_4[0] = False

                # четвертий рядок восьма клітинка
                elif self.Y <= 245 + cell.HEIGHT:
                    if m_data.list_map_player[3][7] == 0:
                        if self.SIZE_SHIP == 4:
                            self.X = self.X_START    
                            self.Y = self.Y_START
                            m_data.end_blit_ship_4[0] = False
                        if self.SIZE_SHIP == 3:
                            self.X = 365 + self.LIST_SHIP_3 + 14 
                        if self.SIZE_SHIP == 2:
                            self.X = 365 + self.LIST_SHIP_2 + 14 
                        if self.SIZE_SHIP == 1:
                            self.X = 365 + self.LIST_SHIP_1 + 14 
                        self.Y = 252
                        self.set_ship(set_row= 3, set_cell_start= 7)
                    if m_data.list_map_player[3][7] == 5:
                        if self.SET_SHIP == False:
                            self.X = self.X_START    
                            self.Y = self.Y_START

                            if self.SIZE_SHIP == 3:
                                m_data.end_blit_ship_3_1[0] = False
                                m_data.end_blit_ship_3_2[0] = False

                            # 2
                            if self.SIZE_SHIP == 2:
                                m_data.end_blit_ship_2_1[0] = False
                                m_data.end_blit_ship_2_2[0] = False
                                m_data.end_blit_ship_2_3[0] = False

                            #1
                            if self.SIZE_SHIP == 1:
                                m_data.end_blit_ship_1_1[0] = False
                                m_data.end_blit_ship_1_2[0] = False
                                m_data.end_blit_ship_1_3[0] = False
                                m_data.end_blit_ship_1_4[0] = False

                # пʼятий рядок восьма клітинка
                elif  self.Y <= 270 + cell.HEIGHT:
                    if m_data.list_map_player[4][7] == 0:
                        if self.SIZE_SHIP == 4:
                            self.X = self.X_START    
                            self.Y = self.Y_START
                            m_data.end_blit_ship_4[0] = False
                        if self.SIZE_SHIP == 3:
                            self.X = 365 + self.LIST_SHIP_3 + 14 
                        if self.SIZE_SHIP == 2:
                            self.X = 365 + self.LIST_SHIP_2 + 14 
                        if self.SIZE_SHIP == 1:
                            self.X = 365 + self.LIST_SHIP_1 + 14 
                        self.Y = 279
                        self.set_ship(set_row= 4, set_cell_start= 7)
                    if m_data.list_map_player[4][7] == 5:
                        if self.SET_SHIP == False:
                            self.X = self.X_START    
                            self.Y = self.Y_START

                            if self.SIZE_SHIP == 3:
                                m_data.end_blit_ship_3_1[0] = False
                                m_data.end_blit_ship_3_2[0] = False

                            # 2
                            if self.SIZE_SHIP == 2:
                                m_data.end_blit_ship_2_1[0] = False
                                m_data.end_blit_ship_2_2[0] = False
                                m_data.end_blit_ship_2_3[0] = False

                            #1
                            if self.SIZE_SHIP == 1:
                                m_data.end_blit_ship_1_1[0] = False
                                m_data.end_blit_ship_1_2[0] = False
                                m_data.end_blit_ship_1_3[0] = False
                                m_data.end_blit_ship_1_4[0] = False
                
                # шостий рядок восьма клітинка
                elif  self.Y <= 295 + cell.HEIGHT:
                    if m_data.list_map_player[5][7] == 0:
                        if self.SIZE_SHIP == 4:
                            self.X = self.X_START    
                            self.Y = self.Y_START
                            m_data.end_blit_ship_4[0] = False
                        if self.SIZE_SHIP == 3:
                            self.X = 365 + self.LIST_SHIP_3 + 14 
                        if self.SIZE_SHIP == 2:
                            self.X = 365 + self.LIST_SHIP_2 + 14 
                        if self.SIZE_SHIP == 1:
                            self.X = 365 + self.LIST_SHIP_1 + 14 
                        self.Y = 306
                        self.set_ship(set_row= 5, set_cell_start= 7)
                    if m_data.list_map_player[5][7] == 5:
                        if self.SET_SHIP == False:
                            self.X = self.X_START    
                            self.Y = self.Y_START
                            m_data.end_blit_ship_3_1[0] = False
                            m_data.end_blit_ship_3_2[0] = False

                            # 2
                            m_data.end_blit_ship_2_1[0] = False
                            m_data.end_blit_ship_2_2[0] = False
                            m_data.end_blit_ship_2_3[0] = False

                            #1
                            m_data.end_blit_ship_1_1[0] = False
                            m_data.end_blit_ship_1_2[0] = False
                            m_data.end_blit_ship_1_3[0] = False
                            m_data.end_blit_ship_1_4[0] = False
                        
                # сьомий рядок восьма клітинка
                elif  self.Y <= 320 + cell.HEIGHT:
                    if m_data.list_map_player[6][7] == 0:
                        if self.SIZE_SHIP == 4:
                            self.X = self.X_START    
                            self.Y = self.Y_START
                            m_data.end_blit_ship_4[0] = False
                        if self.SIZE_SHIP == 3:
                            self.X = 365 + self.LIST_SHIP_3 + 14 
                        if self.SIZE_SHIP == 2:
                            self.X = 365 + self.LIST_SHIP_2 + 14 
                        if self.SIZE_SHIP == 1:
                            self.X = 365 + self.LIST_SHIP_1 + 14 
                        self.Y = 333
                        self.set_ship(set_row= 6, set_cell_start= 7)
                    if m_data.list_map_player[6][7] == 5:
                        if self.SET_SHIP == False:
                            self.X = self.X_START    
                            self.Y = self.Y_START

                            if self.SIZE_SHIP == 3:
                                m_data.end_blit_ship_3_1[0] = False
                                m_data.end_blit_ship_3_2[0] = False

                            # 2
                            if self.SIZE_SHIP == 2:
                                m_data.end_blit_ship_2_1[0] = False
                                m_data.end_blit_ship_2_2[0] = False
                                m_data.end_blit_ship_2_3[0] = False

                            #1
                            if self.SIZE_SHIP == 1:
                                m_data.end_blit_ship_1_1[0] = False
                                m_data.end_blit_ship_1_2[0] = False
                                m_data.end_blit_ship_1_3[0] = False
                                m_data.end_blit_ship_1_4[0] = False

                # восьмий рядок восьма клітинка
                elif self.Y <= 345 + cell.HEIGHT:
                    if m_data.list_map_player[7][7] == 0:
                        if self.SIZE_SHIP == 4:
                            self.X = self.X_START    
                            self.Y = self.Y_START
                            m_data.end_blit_ship_4[0] = False
                        if self.SIZE_SHIP == 3:
                            self.X = 365 + self.LIST_SHIP_3 + 14 
                        if self.SIZE_SHIP == 2:
                            self.X = 365 + self.LIST_SHIP_2 + 14 
                        if self.SIZE_SHIP == 1:
                            self.X = 365 + self.LIST_SHIP_1 + 14 
                        self.Y = 360
                        self.set_ship(set_row= 7, set_cell_start= 7)
                    if m_data.list_map_player[7][7] == 5:
                        if self.SET_SHIP == False:
                            self.X = self.X_START    
                            self.Y = self.Y_START

                            if self.SIZE_SHIP == 3:
                                m_data.end_blit_ship_3_1[0] = False
                                m_data.end_blit_ship_3_2[0] = False

                            # 2
                            if self.SIZE_SHIP == 2:
                                m_data.end_blit_ship_2_1[0] = False
                                m_data.end_blit_ship_2_2[0] = False
                                m_data.end_blit_ship_2_3[0] = False

                            #1
                            if self.SIZE_SHIP == 1:
                                m_data.end_blit_ship_1_1[0] = False
                                m_data.end_blit_ship_1_2[0] = False
                                m_data.end_blit_ship_1_3[0] = False
                                m_data.end_blit_ship_1_4[0] = False

                # девʼятий рядок восьма клітинка
                elif self.Y <= 370 + cell.HEIGHT:
                    if m_data.list_map_player[8][7] == 0:
                        if self.SIZE_SHIP == 4:
                            self.X = self.X_START    
                            self.Y = self.Y_START
                            m_data.end_blit_ship_4[0] = False
                        if self.SIZE_SHIP == 3:
                            self.X = 365 + self.LIST_SHIP_3 + 14 
                        if self.SIZE_SHIP == 2:
                            self.X = 365 + self.LIST_SHIP_2 + 14 
                        if self.SIZE_SHIP == 1:
                            self.X = 365 + self.LIST_SHIP_1 + 14 
                        self.Y = 387
                        self.set_ship(set_row= 8, set_cell_start= 7)
                    if m_data.list_map_player[8][7] == 5:
                        if self.SET_SHIP == False:
                            self.X = self.X_START    
                            self.Y = self.Y_START

                            if self.SIZE_SHIP == 3:
                                m_data.end_blit_ship_3_1[0] = False
                                m_data.end_blit_ship_3_2[0] = False

                            # 2
                            if self.SIZE_SHIP == 2:
                                m_data.end_blit_ship_2_1[0] = False
                                m_data.end_blit_ship_2_2[0] = False
                                m_data.end_blit_ship_2_3[0] = False

                            #1
                            if self.SIZE_SHIP == 1:
                                m_data.end_blit_ship_1_1[0] = False
                                m_data.end_blit_ship_1_2[0] = False
                                m_data.end_blit_ship_1_3[0] = False
                                m_data.end_blit_ship_1_4[0] = False

                # десятий рядок восьма клітинка
                elif self.Y <= 395 + cell.HEIGHT:
                    if m_data.list_map_player[9][7] == 0:
                        if self.SIZE_SHIP == 4:
                            self.X = self.X_START    
                            self.Y = self.Y_START
                            m_data.end_blit_ship_4[0] = False
                        if self.SIZE_SHIP == 3:
                            self.X = 365 + self.LIST_SHIP_3 + 14 
                        if self.SIZE_SHIP == 2:
                            self.X = 365 + self.LIST_SHIP_2 + 14 
                        if self.SIZE_SHIP == 1:
                            self.X = 365 + self.LIST_SHIP_1 + 14 
                        self.Y = 414
                        self.set_ship(set_row= 9, set_cell_start= 7)
                    if m_data.list_map_player[9][7] == 5:
                        if self.SET_SHIP == False:
                            self.X = self.X_START    
                            self.Y = self.Y_START

                            if self.SIZE_SHIP == 3:
                                m_data.end_blit_ship_3_1[0] = False
                                m_data.end_blit_ship_3_2[0] = False

                            # 2
                            if self.SIZE_SHIP == 2:
                                m_data.end_blit_ship_2_1[0] = False
                                m_data.end_blit_ship_2_2[0] = False
                                m_data.end_blit_ship_2_3[0] = False

                            #1
                            if self.SIZE_SHIP == 1:
                                m_data.end_blit_ship_1_1[0] = False
                                m_data.end_blit_ship_1_2[0] = False
                                m_data.end_blit_ship_1_3[0] = False
                                m_data.end_blit_ship_1_4[0] = False

            # девʼята клітинка
            if self.X >= 390 and self.X <= 390 + cell.WIDTH:
                # перший рядок девʼята клітинка
                if self.Y <= 170 + cell.HEIGHT and 415 + cell.HEIGHT:
                    if m_data.list_map_player[0][8] == 0:
                        if self.SIZE_SHIP == 4:
                            self.X = self.X_START    
                            self.Y = self.Y_START
                            m_data.end_blit_ship_4[0] = False

                        if self.SIZE_SHIP == 3:
                            self.X = self.X_START    
                            self.Y = self.Y_START

                            m_data.end_blit_ship_3_1[0] = False
                            m_data.end_blit_ship_3_2[0] = False

                        if self.SIZE_SHIP == 2:
                            self.X = 390 + self.LIST_SHIP_2 + 16
                            self.Y = 171
                        if self.SIZE_SHIP == 1:
                            self.X = 390 + self.LIST_SHIP_1 + 16
                            self.Y = 171
                        self.set_ship(set_row= 0, set_cell_start= 8)

                    if m_data.list_map_player[0][8] == 5:
                        if self.SET_SHIP == False:
                            self.X = self.X_START    
                            self.Y = self.Y_START

                            if self.SIZE_SHIP == 3:
                                m_data.end_blit_ship_3_1[0] = False
                                m_data.end_blit_ship_3_2[0] = False

                            # 2
                            if self.SIZE_SHIP == 2:
                                m_data.end_blit_ship_2_1[0] = False
                                m_data.end_blit_ship_2_2[0] = False
                                m_data.end_blit_ship_2_3[0] = False

                            #1
                            if self.SIZE_SHIP == 1:
                                m_data.end_blit_ship_1_1[0] = False
                                m_data.end_blit_ship_1_2[0] = False
                                m_data.end_blit_ship_1_3[0] = False
                                m_data.end_blit_ship_1_4[0] = False

                # другий рядок девʼята клітинка 
                elif self.Y <= 195 + cell.HEIGHT and 415 + cell.HEIGHT:
                    if m_data.list_map_player[1][8] == 0:
                        if self.SIZE_SHIP == 4:
                            self.X = self.X_START    
                            self.Y = self.Y_START
                            m_data.end_blit_ship_4[0] = False

                        if self.SIZE_SHIP == 3:
                            self.X = self.X_START    
                            self.Y = self.Y_START

                            m_data.end_blit_ship_3_1[0] = False
                            m_data.end_blit_ship_3_2[0] = False

                        if self.SIZE_SHIP == 2:
                            self.X = 390 + self.LIST_SHIP_2 + 16
                            self.Y = 198
                        if self.SIZE_SHIP == 1:
                            self.X = 390 + self.LIST_SHIP_1 + 16
                            self.Y = 198
                        self.set_ship(set_row= 1, set_cell_start= 8)
                    if m_data.list_map_player[1][8] == 5:
                        if self.SET_SHIP == False:
                            self.X = self.X_START    
                            self.Y = self.Y_START

                            if self.SIZE_SHIP == 3:
                                m_data.end_blit_ship_3_1[0] = False
                                m_data.end_blit_ship_3_2[0] = False

                            # 2
                            if self.SIZE_SHIP == 2:
                                m_data.end_blit_ship_2_1[0] = False
                                m_data.end_blit_ship_2_2[0] = False
                                m_data.end_blit_ship_2_3[0] = False

                            #1
                            if self.SIZE_SHIP == 1:
                                m_data.end_blit_ship_1_1[0] = False
                                m_data.end_blit_ship_1_2[0] = False
                                m_data.end_blit_ship_1_3[0] = False
                                m_data.end_blit_ship_1_4[0] = False
 
                # третій рядок девʼята клітинка
                elif self.Y <= 220 + cell.HEIGHT and 415 + cell.HEIGHT:
                    if m_data.list_map_player[2][8] == 0:
                        if self.SIZE_SHIP == 4:
                            self.X = self.X_START    
                            self.Y = self.Y_START
                            m_data.end_blit_ship_4[0] = False

                        if self.SIZE_SHIP == 3:
                            self.X = self.X_START    
                            self.Y = self.Y_START

                            m_data.end_blit_ship_3_1[0] = False
                            m_data.end_blit_ship_3_2[0] = False

                        if self.SIZE_SHIP == 2:
                            self.X = 390 + self.LIST_SHIP_2 + 16
                            self.Y = 225
                        if self.SIZE_SHIP == 1:
                            self.X = 390 + self.LIST_SHIP_1 + 16
                            self.Y = 225
                        self.set_ship(set_row= 2, set_cell_start= 8)
                    if m_data.list_map_player[2][8] == 5:
                        if self.SET_SHIP == False:
                            self.X = self.X_START    
                            self.Y = self.Y_START

                            if self.SIZE_SHIP == 3:
                                m_data.end_blit_ship_3_1[0] = False
                                m_data.end_blit_ship_3_2[0] = False

                            # 2
                            if self.SIZE_SHIP == 2:
                                m_data.end_blit_ship_2_1[0] = False
                                m_data.end_blit_ship_2_2[0] = False
                                m_data.end_blit_ship_2_3[0] = False

                            #1
                            if self.SIZE_SHIP == 1:
                                m_data.end_blit_ship_1_1[0] = False
                                m_data.end_blit_ship_1_2[0] = False
                                m_data.end_blit_ship_1_3[0] = False
                                m_data.end_blit_ship_1_4[0] = False

                # четвертий рядок девʼята клітинка
                elif self.Y <= 245 + cell.HEIGHT and 415 + cell.HEIGHT:
                    if m_data.list_map_player[3][8] == 0:
                        if self.SIZE_SHIP == 4:
                            self.X = self.X_START    
                            self.Y = self.Y_START
                            m_data.end_blit_ship_4[0] = False
                            
                        if self.SIZE_SHIP == 3:
                            self.X = self.X_START    
                            self.Y = self.Y_START

                            m_data.end_blit_ship_3_1[0] = False
                            m_data.end_blit_ship_3_2[0] = False

                        if self.SIZE_SHIP == 2:
                            self.X = 390 + self.LIST_SHIP_2 + 16
                            self.Y = 252
                        if self.SIZE_SHIP == 1:
                            self.X = 390 + self.LIST_SHIP_1 + 16
                            self.Y = 252
                        self.set_ship(set_row= 3, set_cell_start= 8)
                    if m_data.list_map_player[3][8] == 5:
                        if self.SET_SHIP == False:
                            self.X = self.X_START    
                            self.Y = self.Y_START

                            if self.SIZE_SHIP == 3:
                                m_data.end_blit_ship_3_1[0] = False
                                m_data.end_blit_ship_3_2[0] = False

                            # 2
                            if self.SIZE_SHIP == 2:
                                m_data.end_blit_ship_2_1[0] = False
                                m_data.end_blit_ship_2_2[0] = False
                                m_data.end_blit_ship_2_3[0] = False

                            #1
                            if self.SIZE_SHIP == 1:
                                m_data.end_blit_ship_1_1[0] = False
                                m_data.end_blit_ship_1_2[0] = False
                                m_data.end_blit_ship_1_3[0] = False
                                m_data.end_blit_ship_1_4[0] = False
            
                # пʼятий рядок девʼята клітинка
                elif self.Y <= 270 + cell.HEIGHT and 415 + cell.HEIGHT:
                    if m_data.list_map_player[4][8] == 0:
                        if self.SIZE_SHIP == 4:
                            self.X = self.X_START    
                            self.Y = self.Y_START
                            m_data.end_blit_ship_4[0] = False

                        if self.SIZE_SHIP == 3:
                            self.X = self.X_START    
                            self.Y = self.Y_START

                            m_data.end_blit_ship_3_1[0] = False
                            m_data.end_blit_ship_3_2[0] = False

                        if self.SIZE_SHIP == 2:
                            self.X = 390 + self.LIST_SHIP_2 + 16
                            self.Y = 279
                        if self.SIZE_SHIP == 1:
                            self.X = 390 + self.LIST_SHIP_1 + 16
                            self.Y = 279
                        self.set_ship(set_row= 4, set_cell_start= 8)
                    if m_data.list_map_player[4][8] == 5:
                        if self.SET_SHIP == False:
                            self.X = self.X_START    
                            self.Y = self.Y_START

                            if self.SIZE_SHIP == 3:
                                m_data.end_blit_ship_3_1[0] = False
                                m_data.end_blit_ship_3_2[0] = False

                            # 2
                            if self.SIZE_SHIP == 2:
                                m_data.end_blit_ship_2_1[0] = False
                                m_data.end_blit_ship_2_2[0] = False
                                m_data.end_blit_ship_2_3[0] = False

                            #1
                            if self.SIZE_SHIP == 1:
                                m_data.end_blit_ship_1_1[0] = False
                                m_data.end_blit_ship_1_2[0] = False
                                m_data.end_blit_ship_1_3[0] = False
                                m_data.end_blit_ship_1_4[0] = False
                
                # шостий рядок девʼята клітинка
                elif self.Y <= 295 + cell.HEIGHT and 415 + cell.HEIGHT:
                    if m_data.list_map_player[5][8] == 0:
                        if self.SIZE_SHIP == 4:
                            self.X = self.X_START    
                            self.Y = self.Y_START
                            m_data.end_blit_ship_4[0] = False
                            
                        if self.SIZE_SHIP == 3:
                            self.X = self.X_START    
                            self.Y = self.Y_START

                            m_data.end_blit_ship_3_1[0] = False
                            m_data.end_blit_ship_3_2[0] = False

                        if self.SIZE_SHIP == 2:
                            self.X = 390 + self.LIST_SHIP_2 + 16
                            self.Y = 306
                        if self.SIZE_SHIP == 1:
                            self.X = 390 + self.LIST_SHIP_1 + 16
                            self.Y = 306
                        self.set_ship(set_row= 5, set_cell_start= 8)
                    if m_data.list_map_player[5][8] == 5:
                        if self.SET_SHIP == False:
                            self.X = self.X_START    
                            self.Y = self.Y_START

                            if self.SIZE_SHIP == 3:
                                m_data.end_blit_ship_3_1[0] = False
                                m_data.end_blit_ship_3_2[0] = False

                            # 2
                            if self.SIZE_SHIP == 2:
                                m_data.end_blit_ship_2_1[0] = False
                                m_data.end_blit_ship_2_2[0] = False
                                m_data.end_blit_ship_2_3[0] = False

                            #1
                            if self.SIZE_SHIP == 1:
                                m_data.end_blit_ship_1_1[0] = False
                                m_data.end_blit_ship_1_2[0] = False
                                m_data.end_blit_ship_1_3[0] = False
                                m_data.end_blit_ship_1_4[0] = False

                # сьомий рядок девʼята клітинка
                elif self.Y <= 320 + cell.HEIGHT and 415 + cell.HEIGHT:
                    if m_data.list_map_player[6][8] == 0:
                        if self.SIZE_SHIP == 4:
                            self.X = self.X_START    
                            self.Y = self.Y_START
                            m_data.end_blit_ship_4[0] = False
                            m_data.end_blit_ship_3_1[0] = False
                            m_data.end_blit_ship_3_2[0] = False

                        if self.SIZE_SHIP == 3:
                            self.X = self.X_START    
                            self.Y = self.Y_START

                            m_data.end_blit_ship_3_1[0] = False
                            m_data.end_blit_ship_3_2[0] = False

                        if self.SIZE_SHIP == 2:
                            self.X = 390 + self.LIST_SHIP_2 + 16
                            self.Y = 333
                        if self.SIZE_SHIP == 1:
                            self.X = 390 + self.LIST_SHIP_1 + 16
                            self.Y = 333
                        self.set_ship(set_row= 6, set_cell_start= 8)
                    if m_data.list_map_player[6][8] == 5:
                        if self.SET_SHIP == False:
                            self.X = self.X_START    
                            self.Y = self.Y_START

                            if self.SIZE_SHIP == 3:
                                m_data.end_blit_ship_3_1[0] = False
                                m_data.end_blit_ship_3_2[0] = False

                            # 2
                            if self.SIZE_SHIP == 2:
                                m_data.end_blit_ship_2_1[0] = False
                                m_data.end_blit_ship_2_2[0] = False
                                m_data.end_blit_ship_2_3[0] = False

                            #1
                            if self.SIZE_SHIP == 1:
                                m_data.end_blit_ship_1_1[0] = False
                                m_data.end_blit_ship_1_2[0] = False
                                m_data.end_blit_ship_1_3[0] = False
                                m_data.end_blit_ship_1_4[0] = False
                     
                # восьмий рядок девʼята клітинка
                elif  self.Y <= 345 + cell.HEIGHT and 415 + cell.HEIGHT:
                    if m_data.list_map_player[7][8] == 0:
                        if self.SIZE_SHIP == 4:
                            self.X = self.X_START    
                            self.Y = self.Y_START
                            m_data.end_blit_ship_4[0] = False
                            
                        if self.SIZE_SHIP == 3:
                            self.X = self.X_START    
                            self.Y = self.Y_START

                            m_data.end_blit_ship_3_1[0] = False
                            m_data.end_blit_ship_3_2[0] = False

                        if self.SIZE_SHIP == 2:
                            self.X = 390 + self.LIST_SHIP_2 + 16
                            self.Y = 360
                        if self.SIZE_SHIP == 1:
                            self.X = 390 + self.LIST_SHIP_1 + 16
                            self.Y = 360
                        self.set_ship(set_row= 7, set_cell_start= 8)
                    if m_data.list_map_player[7][8] == 5:
                        if self.SET_SHIP == False:
                            self.X = self.X_START    
                            self.Y = self.Y_START

                            if self.SIZE_SHIP == 3:
                                m_data.end_blit_ship_3_1[0] = False
                                m_data.end_blit_ship_3_2[0] = False

                            # 2
                            if self.SIZE_SHIP == 2:
                                m_data.end_blit_ship_2_1[0] = False
                                m_data.end_blit_ship_2_2[0] = False
                                m_data.end_blit_ship_2_3[0] = False

                            #1
                            if self.SIZE_SHIP == 1:
                                m_data.end_blit_ship_1_1[0] = False
                                m_data.end_blit_ship_1_2[0] = False
                                m_data.end_blit_ship_1_3[0] = False
                                m_data.end_blit_ship_1_4[0] = False
                    
                # девʼятий рядок девʼята клітинка
                elif  self.Y <= 370 + cell.HEIGHT and 415 + cell.HEIGHT:
                    if m_data.list_map_player[8][8] == 0:
                        if self.SIZE_SHIP == 4: 
                            self.X = self.X_START    
                            self.Y = self.Y_START
                            m_data.end_blit_ship_4[0] = False
                           
                        if self.SIZE_SHIP == 3:
                            self.X = self.X_START    
                            self.Y = self.Y_START

                            m_data.end_blit_ship_3_1[0] = False
                            m_data.end_blit_ship_3_2[0] = False

                        if self.SIZE_SHIP == 2:
                            self.X = 390 + self.LIST_SHIP_2 + 16
                            self.Y = 387
                        if self.SIZE_SHIP == 1:
                            self.X = 390 + self.LIST_SHIP_1 + 16
                            self.Y = 387
                        self.set_ship(set_row= 8, set_cell_start= 8)
                    if m_data.list_map_player[8][8] == 5:
                        if self.SET_SHIP == False:
                            self.X = self.X_START    
                            self.Y = self.Y_START

                            if self.SIZE_SHIP == 3:
                                m_data.end_blit_ship_3_1[0] = False
                                m_data.end_blit_ship_3_2[0] = False

                            # 2
                            if self.SIZE_SHIP == 2:
                                m_data.end_blit_ship_2_1[0] = False
                                m_data.end_blit_ship_2_2[0] = False
                                m_data.end_blit_ship_2_3[0] = False

                            #1
                            if self.SIZE_SHIP == 1:
                                m_data.end_blit_ship_1_1[0] = False
                                m_data.end_blit_ship_1_2[0] = False
                                m_data.end_blit_ship_1_3[0] = False
                                m_data.end_blit_ship_1_4[0] = False
                
                # десятий рядок девʼята клітинка
                elif  self.Y <= 395 + cell.HEIGHT and 415 + cell.HEIGHT:
                    if m_data.list_map_player[9][8] == 0:
                        if self.SIZE_SHIP == 4:
                            self.X = self.X_START    
                            self.Y = self.Y_START
                            m_data.end_blit_ship_4[0] = False
                            
                        if self.SIZE_SHIP == 3:
                            self.X = self.X_START    
                            self.Y = self.Y_START

                            m_data.end_blit_ship_3_1[0] = False
                            m_data.end_blit_ship_3_2[0] = False

                        if self.SIZE_SHIP == 2:
                            self.X = 390 + self.LIST_SHIP_2 + 16
                            self.Y = 414
                        if self.SIZE_SHIP == 1:
                            self.X = 390 + self.LIST_SHIP_1 + 16
                            self.Y = 414
                        self.set_ship(set_row= 9, set_cell_start= 8)
                    if m_data.list_map_player[9][8] == 5:
                        if self.SET_SHIP == False:
                            self.X = self.X_START    
                            self.Y = self.Y_START

                            if self.SIZE_SHIP == 3:
                                m_data.end_blit_ship_3_1[0] = False
                                m_data.end_blit_ship_3_2[0] = False

                            # 2
                            if self.SIZE_SHIP == 2:
                                m_data.end_blit_ship_2_1[0] = False
                                m_data.end_blit_ship_2_2[0] = False
                                m_data.end_blit_ship_2_3[0] = False

                            #1
                            if self.SIZE_SHIP == 1:
                                m_data.end_blit_ship_1_1[0] = False
                                m_data.end_blit_ship_1_2[0] = False
                                m_data.end_blit_ship_1_3[0] = False
                                m_data.end_blit_ship_1_4[0] = False             

            # десята клітинка
            if self.X >= 415 and self.X <= 415 + cell.WIDTH: 
                # перший рядок десята клітинка               
                if self.Y <= 170 + cell.HEIGHT and 600 + cell.HEIGHT:
                    if m_data.list_map_player[0][9] == 0:
                        if self.SIZE_SHIP == 4:
                            self.X = self.X_START    
                            self.Y = self.Y_START
                            m_data.end_blit_ship_4[0] = False

                        if self.SIZE_SHIP == 3:
                            self.X = self.X_START    
                            self.Y = self.Y_START

                            m_data.end_blit_ship_3_1[0] = False
                            m_data.end_blit_ship_3_2[0] = False

                        if self.SIZE_SHIP == 2:
                            self.X = self.X_START    
                            self.Y = self.Y_START

                            m_data.end_blit_ship_2_1[0] = False
                            m_data.end_blit_ship_2_2[0] = False
                            m_data.end_blit_ship_2_3[0] = False

                        if self.SIZE_SHIP == 1:
                            self.X = 415 + self.LIST_SHIP_1 + 18
                            self.Y = 171
                        self.set_ship(set_row= 0, set_cell_start= 9)
                    if m_data.list_map_player[0][9] == 5:
                        if self.SET_SHIP == False:
                            self.X = self.X_START    
                            self.Y = self.Y_START

                            if self.SIZE_SHIP == 3:
                                m_data.end_blit_ship_3_1[0] = False
                                m_data.end_blit_ship_3_2[0] = False

                            # 2
                            if self.SIZE_SHIP == 2:
                                m_data.end_blit_ship_2_1[0] = False
                                m_data.end_blit_ship_2_2[0] = False
                                m_data.end_blit_ship_2_3[0] = False

                            #1
                            if self.SIZE_SHIP == 1:
                                m_data.end_blit_ship_1_1[0] = False
                                m_data.end_blit_ship_1_2[0] = False
                                m_data.end_blit_ship_1_3[0] = False
                                m_data.end_blit_ship_1_4[0] = False

                # другий рядок десята клітинка 
                elif self.Y <= 195 + cell.HEIGHT and 600 + cell.HEIGHT:
                    if m_data.list_map_player[1][9] == 0:
                        if self.SIZE_SHIP == 4:
                            self.X = self.X_START    
                            self.Y = self.Y_START
                            m_data.end_blit_ship_4[0] = False

                        if self.SIZE_SHIP == 3:
                            self.X = self.X_START    
                            self.Y = self.Y_START

                            m_data.end_blit_ship_3_1[0] = False
                            m_data.end_blit_ship_3_2[0] = False

                        if self.SIZE_SHIP == 2:
                            self.X = self.X_START    
                            self.Y = self.Y_START

                            m_data.end_blit_ship_2_1[0] = False
                            m_data.end_blit_ship_2_2[0] = False
                            m_data.end_blit_ship_2_3[0] = False

                        if self.SIZE_SHIP == 1:
                            self.X = 415 + self.LIST_SHIP_1 + 18
                            self.Y = 198
                        self.set_ship(set_row= 1, set_cell_start= 9)
                    if m_data.list_map_player[1][9] == 5:
                        if self.SET_SHIP == False:
                            self.X = self.X_START    
                            self.Y = self.Y_START

                            if self.SIZE_SHIP == 3:
                                m_data.end_blit_ship_3_1[0] = False
                                m_data.end_blit_ship_3_2[0] = False

                            # 2
                            if self.SIZE_SHIP == 2:
                                m_data.end_blit_ship_2_1[0] = False
                                m_data.end_blit_ship_2_2[0] = False
                                m_data.end_blit_ship_2_3[0] = False

                            #1
                            if self.SIZE_SHIP == 1:
                                m_data.end_blit_ship_1_1[0] = False
                                m_data.end_blit_ship_1_2[0] = False
                                m_data.end_blit_ship_1_3[0] = False
                                m_data.end_blit_ship_1_4[0] = False

                # третій рядок десята клітинка 
                elif  self.Y <= 220 + cell.HEIGHT and 600 + cell.HEIGHT:
                    if m_data.list_map_player[2][9] == 0:
                        if self.SIZE_SHIP == 4:
                            self.X = self.X_START    
                            self.Y = self.Y_START
                            m_data.end_blit_ship_4[0] = False

                        if self.SIZE_SHIP == 3:
                            self.X = self.X_START    
                            self.Y = self.Y_START

                            m_data.end_blit_ship_3_1[0] = False
                            m_data.end_blit_ship_3_2[0] = False

                        if self.SIZE_SHIP == 2:
                            self.X = self.X_START    
                            self.Y = self.Y_START

                            m_data.end_blit_ship_2_1[0] = False
                            m_data.end_blit_ship_2_2[0] = False
                            m_data.end_blit_ship_2_3[0] = False

                        if self.SIZE_SHIP == 1:
                            self.X = 415 + self.LIST_SHIP_1 + 18
                            self.Y = 225
                        self.set_ship(set_row= 2, set_cell_start= 9)
                    if m_data.list_map_player[2][9] == 5:
                        if self.SET_SHIP == False:
                            self.X = self.X_START    
                            self.Y = self.Y_START

                            if self.SIZE_SHIP == 3:
                                m_data.end_blit_ship_3_1[0] = False
                                m_data.end_blit_ship_3_2[0] = False

                            # 2
                            if self.SIZE_SHIP == 2:
                                m_data.end_blit_ship_2_1[0] = False
                                m_data.end_blit_ship_2_2[0] = False
                                m_data.end_blit_ship_2_3[0] = False

                            #1
                            if self.SIZE_SHIP == 1:
                                m_data.end_blit_ship_1_1[0] = False
                                m_data.end_blit_ship_1_2[0] = False
                                m_data.end_blit_ship_1_3[0] = False
                                m_data.end_blit_ship_1_4[0] = False

                # четвертий рядок десята клітинка 
                elif  self.Y <= 245 + cell.HEIGHT and 600 + cell.HEIGHT:
                    if m_data.list_map_player[3][9] == 0:
                        if self.SIZE_SHIP == 4:
                            self.X = self.X_START    
                            self.Y = self.Y_START
                            m_data.end_blit_ship_4[0] = False

                        if self.SIZE_SHIP == 3:
                            self.X = self.X_START    
                            self.Y = self.Y_START

                            m_data.end_blit_ship_3_1[0] = False
                            m_data.end_blit_ship_3_2[0] = False

                        if self.SIZE_SHIP == 2:
                            self.X = self.X_START    
                            self.Y = self.Y_START

                            m_data.end_blit_ship_2_1[0] = False
                            m_data.end_blit_ship_2_2[0] = False
                            m_data.end_blit_ship_2_3[0] = False

                        if self.SIZE_SHIP == 1:
                            self.X = 415 + self.LIST_SHIP_1 + 18
                            self.Y = 252
                        self.set_ship(set_row= 3, set_cell_start= 9)
                    if m_data.list_map_player[3][9] == 5:
                        if self.SET_SHIP == False:
                            self.X = self.X_START    
                            self.Y = self.Y_START

                            if self.SIZE_SHIP == 3:
                                m_data.end_blit_ship_3_1[0] = False
                                m_data.end_blit_ship_3_2[0] = False

                            # 2
                            if self.SIZE_SHIP == 2:
                                m_data.end_blit_ship_2_1[0] = False
                                m_data.end_blit_ship_2_2[0] = False
                                m_data.end_blit_ship_2_3[0] = False

                            #1
                            if self.SIZE_SHIP == 1:
                                m_data.end_blit_ship_1_1[0] = False
                                m_data.end_blit_ship_1_2[0] = False
                                m_data.end_blit_ship_1_3[0] = False
                                m_data.end_blit_ship_1_4[0] = False

                # пʼятий рядок десята клітинка 
                elif  self.Y <= 270 + cell.HEIGHT and 600 + cell.HEIGHT:
                    if m_data.list_map_player[4][9] == 0:
                        if self.SIZE_SHIP == 4:
                            self.X = self.X_START    
                            self.Y = self.Y_START
                            m_data.end_blit_ship_4[0] = False

                        if self.SIZE_SHIP == 3:
                            self.X = self.X_START    
                            self.Y = self.Y_START

                            m_data.end_blit_ship_3_1[0] = False
                            m_data.end_blit_ship_3_2[0] = False

                        if self.SIZE_SHIP == 2:
                            self.X = self.X_START    
                            self.Y = self.Y_START

                            m_data.end_blit_ship_2_1[0] = False
                            m_data.end_blit_ship_2_2[0] = False
                            m_data.end_blit_ship_2_3[0] = False

                        if self.SIZE_SHIP == 1:
                            self.X = 415 + self.LIST_SHIP_1 + 18
                            self.Y = 279
                        self.set_ship(set_row= 4, set_cell_start= 9)
                    if m_data.list_map_player[4][9] == 5:
                        if self.SET_SHIP == False:
                            self.X = self.X_START    
                            self.Y = self.Y_START

                            if self.SIZE_SHIP == 3:
                                m_data.end_blit_ship_3_1[0] = False
                                m_data.end_blit_ship_3_2[0] = False

                            # 2
                            if self.SIZE_SHIP == 2:
                                m_data.end_blit_ship_2_1[0] = False
                                m_data.end_blit_ship_2_2[0] = False
                                m_data.end_blit_ship_2_3[0] = False

                            #1
                            if self.SIZE_SHIP == 1:
                                m_data.end_blit_ship_1_1[0] = False
                                m_data.end_blit_ship_1_2[0] = False
                                m_data.end_blit_ship_1_3[0] = False
                                m_data.end_blit_ship_1_4[0] = False
                        
                # шостий рядок десята клітинка 
                elif  self.Y <= 295 + cell.HEIGHT and 600 + cell.HEIGHT:
                    if m_data.list_map_player[5][9] == 0:
                        if self.SIZE_SHIP == 4:
                            self.X = self.X_START    
                            self.Y = self.Y_START
                            m_data.end_blit_ship_4[0] = False

                        if self.SIZE_SHIP == 3:
                            self.X = self.X_START    
                            self.Y = self.Y_START

                            m_data.end_blit_ship_3_1[0] = False
                            m_data.end_blit_ship_3_2[0] = False

                        if self.SIZE_SHIP == 2:
                            self.X = self.X_START    
                            self.Y = self.Y_START

                            m_data.end_blit_ship_2_1[0] = False
                            m_data.end_blit_ship_2_2[0] = False
                            m_data.end_blit_ship_2_3[0] = False

                        if self.SIZE_SHIP == 1:
                            self.X = 415 + self.LIST_SHIP_1 + 18
                            self.Y = 306
                        self.set_ship(set_row= 5, set_cell_start= 9)
                    if m_data.list_map_player[5][9] == 5:
                        if self.SET_SHIP == False:
                            self.X = self.X_START    
                            self.Y = self.Y_START

                            if self.SIZE_SHIP == 3:
                                m_data.end_blit_ship_3_1[0] = False
                                m_data.end_blit_ship_3_2[0] = False

                            # 2
                            if self.SIZE_SHIP == 2:
                                m_data.end_blit_ship_2_1[0] = False
                                m_data.end_blit_ship_2_2[0] = False
                                m_data.end_blit_ship_2_3[0] = False

                            #1
                            if self.SIZE_SHIP == 1:
                                m_data.end_blit_ship_1_1[0] = False
                                m_data.end_blit_ship_1_2[0] = False
                                m_data.end_blit_ship_1_3[0] = False
                                m_data.end_blit_ship_1_4[0] = False

                # сьомий рядок десята клітинка       
                elif  self.Y <= 320 + cell.HEIGHT and 600 + cell.HEIGHT:
                    if m_data.list_map_player[6][9] == 0:
                        if self.SIZE_SHIP == 4:
                            self.X = self.X_START    
                            self.Y = self.Y_START
                            m_data.end_blit_ship_4[0] = False

                        if self.SIZE_SHIP == 3:
                            self.X = self.X_START    
                            self.Y = self.Y_START

                            m_data.end_blit_ship_3_1[0] = False
                            m_data.end_blit_ship_3_2[0] = False

                        if self.SIZE_SHIP == 2:
                            self.X = self.X_START    
                            self.Y = self.Y_START

                            m_data.end_blit_ship_2_1[0] = False
                            m_data.end_blit_ship_2_2[0] = False
                            m_data.end_blit_ship_2_3[0] = False

                        if self.SIZE_SHIP == 1:
                            self.X = 415 + self.LIST_SHIP_1 + 18
                            self.Y = 333
                        self.set_ship(set_row= 6, set_cell_start= 9)
                    if m_data.list_map_player[6][9] == 5:
                        if self.SET_SHIP == False:
                            self.X = self.X_START    
                            self.Y = self.Y_START

                            if self.SIZE_SHIP == 3:
                                m_data.end_blit_ship_3_1[0] = False
                                m_data.end_blit_ship_3_2[0] = False

                            # 2
                            if self.SIZE_SHIP == 2:
                                m_data.end_blit_ship_2_1[0] = False
                                m_data.end_blit_ship_2_2[0] = False
                                m_data.end_blit_ship_2_3[0] = False

                            #1
                            if self.SIZE_SHIP == 1:
                                m_data.end_blit_ship_1_1[0] = False
                                m_data.end_blit_ship_1_2[0] = False
                                m_data.end_blit_ship_1_3[0] = False
                                m_data.end_blit_ship_1_4[0] = False
                            
                # восьмий рядок десята клітинка 
                elif self.Y <= 345 + cell.HEIGHT and 600 + cell.HEIGHT:
                    if m_data.list_map_player[7][9] == 0:
                        if self.SIZE_SHIP == 4:
                            self.X = self.X_START    
                            self.Y = self.Y_START
                            m_data.end_blit_ship_4[0] = False

                        if self.SIZE_SHIP == 3:
                            self.X = self.X_START    
                            self.Y = self.Y_START

                            m_data.end_blit_ship_3_1[0] = False
                            m_data.end_blit_ship_3_2[0] = False

                        if self.SIZE_SHIP == 2:
                            self.X = self.X_START    
                            self.Y = self.Y_START

                            m_data.end_blit_ship_2_1[0] = False
                            m_data.end_blit_ship_2_2[0] = False
                            m_data.end_blit_ship_2_3[0] = False

                        if self.SIZE_SHIP == 1:
                            self.X = 415 + self.LIST_SHIP_1 + 18
                            self.Y = 360
                        self.set_ship(set_row= 7, set_cell_start= 9)
                    if m_data.list_map_player[7][9] == 5:
                        if self.SET_SHIP == False:
                            self.X = self.X_START    
                            self.Y = self.Y_START

                            if self.SIZE_SHIP == 3:
                                m_data.end_blit_ship_3_1[0] = False
                                m_data.end_blit_ship_3_2[0] = False

                            # 2
                            if self.SIZE_SHIP == 2:
                                m_data.end_blit_ship_2_1[0] = False
                                m_data.end_blit_ship_2_2[0] = False
                                m_data.end_blit_ship_2_3[0] = False

                            #1
                            if self.SIZE_SHIP == 1:
                                m_data.end_blit_ship_1_1[0] = False
                                m_data.end_blit_ship_1_2[0] = False
                                m_data.end_blit_ship_1_3[0] = False
                                m_data.end_blit_ship_1_4[0] = False

                # девʼятий рядок десята клітинка 
                elif self.Y <= 370 + cell.HEIGHT and 600 + cell.HEIGHT:
                    if m_data.list_map_player[8][9] == 0:
                        if self.SIZE_SHIP == 4:
                            self.X = self.X_START    
                            self.Y = self.Y_START
                            m_data.end_blit_ship_4[0] = False

                        if self.SIZE_SHIP == 3:
                            self.X = self.X_START    
                            self.Y = self.Y_START

                            m_data.end_blit_ship_3_1[0] = False
                            m_data.end_blit_ship_3_2[0] = False

                        if self.SIZE_SHIP == 2:
                            self.X = self.X_START    
                            self.Y = self.Y_START

                            m_data.end_blit_ship_2_1[0] = False
                            m_data.end_blit_ship_2_2[0] = False
                            m_data.end_blit_ship_2_3[0] = False

                        if self.SIZE_SHIP == 1:
                            self.X = 415 + self.LIST_SHIP_1 + 18
                            self.Y = 387
                        self.set_ship(set_row= 8, set_cell_start= 9)
                    if m_data.list_map_player[8][9] == 5:
                        if self.SET_SHIP == False:
                            self.X = self.X_START    
                            self.Y = self.Y_START

                            if self.SIZE_SHIP == 3:
                                m_data.end_blit_ship_3_1[0] = False
                                m_data.end_blit_ship_3_2[0] = False

                            # 2
                            if self.SIZE_SHIP == 2:
                                m_data.end_blit_ship_2_1[0] = False
                                m_data.end_blit_ship_2_2[0] = False
                                m_data.end_blit_ship_2_3[0] = False

                            #1
                            if self.SIZE_SHIP == 1:
                                m_data.end_blit_ship_1_1[0] = False
                                m_data.end_blit_ship_1_2[0] = False
                                m_data.end_blit_ship_1_3[0] = False
                                m_data.end_blit_ship_1_4[0] = False
                
                # десятий рядок десята клітинка     
                elif self.Y <= 395 + cell.HEIGHT and 600 + cell.HEIGHT:
                    if m_data.list_map_player[9][9] == 0:
                        if self.SIZE_SHIP == 4:
                            self.X = self.X_START    
                            self.Y = self.Y_START
                            m_data.end_blit_ship_4[0] = False

                        if self.SIZE_SHIP == 3:
                            self.X = self.X_START    
                            self.Y = self.Y_START

                            m_data.end_blit_ship_3_1[0] = False
                            m_data.end_blit_ship_3_2[0] = False

                        if self.SIZE_SHIP == 2:
                            self.X = self.X_START    
                            self.Y = self.Y_START

                            m_data.end_blit_ship_2_1[0] = False
                            m_data.end_blit_ship_2_2[0] = False
                            m_data.end_blit_ship_2_3[0] = False

                        if self.SIZE_SHIP == 1:
                            self.X = 415 + self.LIST_SHIP_1 + 18
                            self.Y = 414  
                        self.set_ship(set_row= 9, set_cell_start= 9)
                    if m_data.list_map_player[9][9] == 5:
                            self.X = self.X_START    
                            self.Y = self.Y_START

                            if self.SIZE_SHIP == 3:
                                m_data.end_blit_ship_3_1[0] = False
                                m_data.end_blit_ship_3_2[0] = False

                            # 2
                            if self.SIZE_SHIP == 2:
                                m_data.end_blit_ship_2_1[0] = False
                                m_data.end_blit_ship_2_2[0] = False
                                m_data.end_blit_ship_2_3[0] = False

                            #1
                            if self.SIZE_SHIP == 1:
                                m_data.end_blit_ship_1_1[0] = False
                                m_data.end_blit_ship_1_2[0] = False
                                m_data.end_blit_ship_1_3[0] = False
                                m_data.end_blit_ship_1_4[0] = False                  
                            
    def vertical_turn(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] == True:
            self.load_image(check_img= False)
            self.ROTATE = True
        
    def horizontal_turn(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] == True:
            if self.ROTATE == True:
                self.load_image(check_img= True) 
                self.ROTATE = False

ship_4 = Ship_4()

# 3
ship_3_1 = Ship_4(width1= 75, list_ship_4= m_data.list_x[2], y1= 180, name1= 'img/ship/ship_3.png', size_ship= 3)
ship_3_2 = Ship_4(width1= 75, list_ship_4= m_data.list_x[2], y1= 230, name1= 'img/ship/ship_3.png', size_ship= 3)

# 2
ship_2_1 = Ship_4(width1= 50, list_ship_4= m_data.list_x[1], y1= 180, name1= 'img/ship/ship_2.png', size_ship= 2)
ship_2_2 = Ship_4(width1= 50, list_ship_4= m_data.list_x[1], y1= 230, name1= 'img/ship/ship_2.png', size_ship= 2)
ship_2_3 = Ship_4(width1= 50, list_ship_4= m_data.list_x[1], y1= 280, name1= 'img/ship/ship_2.png', size_ship= 2)

# 1
ship_1_1 = Ship_4(width1= 25, list_ship_4= m_data.list_x[0], y1= 180, name1= 'img/ship/ship_1.png', size_ship= 1)
ship_1_2 = Ship_4(width1= 25, list_ship_4= m_data.list_x[0], y1= 230, name1= 'img/ship/ship_1.png', size_ship= 1)
ship_1_3 = Ship_4(width1= 25, list_ship_4= m_data.list_x[0], y1= 280, name1= 'img/ship/ship_1.png', size_ship= 1)
ship_1_4 = Ship_4(width1= 25, list_ship_4= m_data.list_x[0], y1= 330, name1= 'img/ship/ship_1.png', size_ship= 1)

