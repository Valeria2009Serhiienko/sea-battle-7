import pygame
import modules.main_modules.settings as m_settings
import modules.main_modules.data_base as m_data
pygame.init()

# 4
class Ship_4(m_settings.Settings):
    def __init__(self, 
                width1 = 100, 
                height1 = 25, 
                x1 = 770, 
                y1 = 180,
                list_ship_4 = m_data.list_x[3], 
                list_ship_3 = m_data.list_x[2], 
                list_ship_2 = m_data.list_x[1], 
                list_ship_1 = m_data.list_x[0], 
                name1 = 'img/ship/ship_4.png',
                direction_x1 = 0, 
                direction_y1 = 0,
                size_ship = 4
            ):
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

    def rotate(self, range_Y_1, range_Y_2, number_X, number_Y):
        for cell in m_data.list_cells:
            if self.ROTATE:
                if self.Y <= range_Y_1 + cell.HEIGHT and range_Y_2 + cell.HEIGHT:
                    self.X = number_X
                    self.Y = number_Y + self.LIST_SHIP_4 

    def set_ship(self, set_row, set_cell_start):
        #
        number_ship = self.SIZE_SHIP
        cell_start = set_cell_start
        #
        # умова горизонтального розміщення корабля та заповнення списку відповідно розташуванню корабля
        if self.ROTATE == False:
            m_data.list_map_player[set_row][cell_start] = number_ship
            # цикл що задає цифри розміру корабля замість ноликів 
            for count in range(number_ship - 1):
                cell_start += 1
                m_data.list_map_player[set_row][cell_start] = number_ship
            # умова що перевіряє нулевий рядок та займає комірки 5 все навколо коробля
            if set_row == 0:
                # умова що перевіряє, якщо довжина списка не перевищена, то за кораблем ставимо зайнято 5
                if len(m_data.list_map_player[set_row]) > cell_start + 1:
                    m_data.list_map_player[set_row][cell_start + 1] = 5
                # умова що перевіряє, якщо стартова комірка розташування корабля більша за нуль, то перед кораблем ставимо зайнято 5
                if set_cell_start > 0:
                    m_data.list_map_player[set_row][cell_start - (number_ship)] = 5
                # 
                cell_start = set_cell_start
                for count in range(number_ship + 1):
                    # умова що перевіряє, якщо довжина списка не перевищена, то під кораблем ставимо зайнято 5
                    if len(m_data.list_map_player[set_row]) > cell_start:
                        m_data.list_map_player[set_row + 1][cell_start] = 5
                        cell_start += 1
                    else:
                        # умова що перевіряє, якщо довжина списка перевищена, то під кораблем, 
                        # індекс що менше на одиницю за стортовий ставимо зайнято 5, а також в тому ж самому рядку що стоїть корабель
                        m_data.list_map_player[set_row][cell_start - (number_ship + 1)] = 5
                        m_data.list_map_player[set_row + 1][cell_start - (number_ship + 1)] = 5
            # рядки від 1 до 8, 0 рядок перший, 9 рядок - останній
            if set_row > 0 and set_row < 9:
                if len(m_data.list_map_player[set_row]) > cell_start + 1:
                    m_data.list_map_player[set_row][cell_start + 1] = 5
                if set_cell_start > 0:
                    m_data.list_map_player[set_row][cell_start - (number_ship)] = 5
                    m_data.list_map_player[set_row + 1][cell_start - (number_ship)] = 5
                    m_data.list_map_player[set_row - 1][cell_start - (number_ship)] = 5
                cell_start = set_cell_start
                for count in range(number_ship + 1):
                    if len(m_data.list_map_player[set_row]) > cell_start:
                        m_data.list_map_player[set_row + 1][cell_start] = 5
                        m_data.list_map_player[set_row - 1][cell_start] = 5
                        cell_start += 1
                    else:
                        m_data.list_map_player[set_row][cell_start - (number_ship + 1)] = 5
                        m_data.list_map_player[set_row + 1][cell_start - (number_ship + 1)] = 5
                        m_data.list_map_player[set_row - 1][cell_start - (number_ship + 1)] = 5
            # для останнього рядка
            if set_row == 9:
                if len(m_data.list_map_player[set_row]) > cell_start + 1:
                    m_data.list_map_player[set_row][cell_start + 1] = 5
                if set_cell_start > 0:
                    m_data.list_map_player[set_row][cell_start - (number_ship)] = 5
                    m_data.list_map_player[set_row - 1][cell_start - (number_ship)] = 5
                cell_start = set_cell_start
                for count in range(number_ship + 1):
                    if len(m_data.list_map_player[set_row]) > cell_start:
                        m_data.list_map_player[set_row - 1][cell_start] = 5
                        cell_start += 1
                    else:
                        m_data.list_map_player[set_row][cell_start - (number_ship + 1)] = 5
                        m_data.list_map_player[set_row - 1][cell_start - (number_ship + 1)] = 5
        #
        if self.FLAG == 0:
            for i in m_data.list_map_player:
                print(i)
            print("\n")
            self.FLAG = 1

    def collision_ship_4(self):
        for cell in m_data.list_cells:
            # стовбчик перший
            if self.X >= 350 and self.X <= 350 + cell.WIDTH:
                # ряд перший перша комірка
                if self.Y <= 170 + cell.HEIGHT and 375 + cell.HEIGHT:
                    if m_data.list_map_player[0][0] == 0:
                        self.X = 350 + self.LIST_SHIP_4 
                        self.Y = 171
                        self.set_ship(set_row= 0, set_cell_start= 0)
                    if m_data.list_map_player[0][0] == 5:
                        self.X = self.X_START
                        self.Y = self.Y_START

                # ряд другий перша комірка 
                elif self.Y <= 195 + cell.HEIGHT and 375 + cell.HEIGHT:
                    if m_data.list_map_player[1][0] == 0:
                        self.X = 350 + self.LIST_SHIP_4
                        self.Y = 198 
                        self.set_ship(set_row= 1, set_cell_start= 0)
                # ряд третій перша комірка 
                elif self.Y <= 220 + cell.HEIGHT and 375 + cell.HEIGHT:
                    self.X = 350 + self.LIST_SHIP_4
                    self.Y = 225
                    self.set_ship(set_row= 2, set_cell_start= 0)
                # ряд четвертий перша комірка 
                elif self.Y <= 245 + cell.HEIGHT and 375 + cell.HEIGHT:
                    self.X = 350 + self.LIST_SHIP_4
                    self.Y = 252
                    self.set_ship(set_row= 3, set_cell_start= 0)

                # ряд пʼятий перша комірка 
                elif self.Y <= 270 + cell.HEIGHT and 375 + cell.HEIGHT:
                    self.X = 350 + self.LIST_SHIP_4
                    self.Y = 279 
                    self.set_ship(set_row= 4, set_cell_start= 0)

                # ряд шостий перша комірка 
                elif self.Y <= 295 + cell.HEIGHT and 375 + cell.HEIGHT:
                    self.X = 350 + self.LIST_SHIP_4
                    self.Y = 306
                    self.set_ship(set_row= 5, set_cell_start= 0)
                            
                # ряд сьомий перша комірка 
                elif self.Y <= 320 + cell.HEIGHT and 375 + cell.HEIGHT:
                    self.X = 350 + self.LIST_SHIP_4
                    self.Y = 333
                    self.set_ship(set_row= 6, set_cell_start= 0)

                 # ряд восьмий перша комірка    
                elif  self.Y <= 345 + cell.HEIGHT and 375 + cell.HEIGHT:
                    self.X = 350 + self.LIST_SHIP_4
                    self.Y = 333
                    self.set_ship(set_row= 7, set_cell_start= 0)


                # ряд девʼятий перша комірка             
                elif  self.Y <= 370 + cell.HEIGHT and 375 + cell.HEIGHT:
                    self.X = 350 + self.LIST_SHIP_4
                    self.Y = 387
                    self.set_ship(set_row= 8, set_cell_start= 0)

                # ряд десятий перша комірка            
                elif  self.Y <= 395 + cell.HEIGHT and 375 + cell.HEIGHT:
                    self.X = 350 + self.LIST_SHIP_4
                    self.Y = 414
                    self.set_ship(set_row= 9, set_cell_start= 0)

                    # self.rotate(range_Y_1= 395, range_Y_2= 375, number_X= 351, number_Y= 333)
            # друга клітинка 
            if self.X >= 375 and self.X <= 375 + cell.WIDTH:
                # ряд перший друга комірка
                if self.Y <= 170 + cell.HEIGHT and 400 + cell.HEIGHT:
                    self.X = 375 + self.LIST_SHIP_4 + 2
                    self.Y = 171

                # ряд другий друга комірка
                elif self.Y <= 195 + cell.HEIGHT and 400 + cell.HEIGHT:
                    self.X = 375 + self.LIST_SHIP_4 
                    self.Y = 198


                # ряд третій друга комірка
                elif self.Y <= 220 + cell.HEIGHT and 400 + cell.HEIGHT:
                    self.X = 375 + self.LIST_SHIP_4  
                    self.Y = 225

                # ряд четвертий друга комірка
                elif self.Y <= 245 + cell.HEIGHT and 400 + cell.HEIGHT:
                    self.X = 375 + self.LIST_SHIP_4 + 2 
                    self.Y = 252

                    

                # ряд пʼятий друга комірка        
                elif self.Y <= 270 + cell.HEIGHT and 400 + cell.HEIGHT:
                    self.X = 375 + self.LIST_SHIP_4 + 2  
                    self.Y = 279

                # ряд шостий друга комірка
                elif  self.Y <= 295 + cell.HEIGHT and 400 + cell.HEIGHT:
                    self.X = 375 + self.LIST_SHIP_4 + 2  
                    self.Y = 306


                # ряд сьомий друга комірка
                elif self.Y <= 320 + cell.HEIGHT and 400 + cell.HEIGHT:
                    self.X = 375 + self.LIST_SHIP_4 + 2  
                    self.Y = 333

                # ряд восьмий друга комірка
                elif  self.Y <= 345 + cell.HEIGHT and 400 + cell.HEIGHT:
                    self.X = 375 + self.LIST_SHIP_4 + 2  
                    self.Y = 360


                # ряд девʼятий друга комірка
                elif self.Y <= 370 + cell.HEIGHT and 400 + cell.HEIGHT:
                    self.X = 375 + self.LIST_SHIP_4 + 2 
                    self.Y = 387

                # ряд десятий друга комірка
                elif  self.Y <= 395 + cell.HEIGHT and 400 + cell.HEIGHT:
                    self.X = 375 + self.LIST_SHIP_4 + 2  
                    self.Y = 414  
                    
            # третя клітинка 
            if self.X >= 400 and self.X <= 400 + cell.WIDTH:
                # ряд перший третя комірка
                if self.Y <= 170 + cell.HEIGHT and 425 + cell.HEIGHT:
                    self.X = 400 + self.LIST_SHIP_4 + 4 
                    self.Y = 171
                            
                    
                # ряд другий третя клітинка
                elif self.Y <= 195 + cell.HEIGHT and 425 + cell.HEIGHT:
                    self.X = 400 + self.LIST_SHIP_4 + 4
                    self.Y = 198


                # ряд третій третя клітинка
                elif self.Y <= 220 + cell.HEIGHT and 425 + cell.HEIGHT:
                    self.X = 400 + self.LIST_SHIP_4 + 4 
                    self.Y = 225

                # ряд четвертий третя клітинка
                elif self.Y <= 245 + cell.HEIGHT and 425 + cell.HEIGHT:
                    self.X = 400 + self.LIST_SHIP_4 + 4 
                    self.Y = 252


                # ряд пʼятий третя клітинка
                elif self.Y <= 270 + cell.HEIGHT and 425 + cell.HEIGHT:
                    self.X = 400 + self.LIST_SHIP_4 + 4 
                    self.Y = 279


                # ряд шостий третя клітинка
                elif  self.Y <= 295 + cell.HEIGHT and 425 + cell.HEIGHT:
                    self.X = 400 + self.LIST_SHIP_4 + 4 
                    self.Y = 306
                    
                # ряд сьомий третя клітинка
                elif self.Y <= 320 + cell.HEIGHT and 425 + cell.HEIGHT:
                    self.X = 400 + self.LIST_SHIP_4 + 4 
                    self.Y = 333

                # ряд восьмий третя клітинка    
                elif  self.Y <= 345 + cell.HEIGHT and 425 + cell.HEIGHT:
                    self.X = 400 + self.LIST_SHIP_4 + 4 
                    self.Y = 360
                
                # ряд девʼятий третя клітинка
                elif self.Y <= 370 + cell.HEIGHT and 425 + cell.HEIGHT:
                    self.X = 400 + self.LIST_SHIP_4 + 4
                    self.Y = 387

                # ряд десятий третя клітинка
                elif  self.Y <= 395 + cell.HEIGHT and 425 + cell.HEIGHT:
                    self.X = 400 + self.LIST_SHIP_4 + 4 
                    self.Y = 414 
                    
            # четверта клітинка
            if self.X >= 425 and self.X <= 425 + cell.WIDTH:
                # ряд перший четверта клітинка
                if self.Y <= 170 + cell.HEIGHT and 450 + cell.HEIGHT:
                    self.X = 425 + self.LIST_SHIP_4 + 6
                    self.Y = 171

                # ряд другий четверта клітинка
                elif self.Y <= 195 + cell.HEIGHT and 450 + cell.HEIGHT:
                    self.X = 425 + self.LIST_SHIP_4 + 6
                    self.Y = 198

                 # ряд третій четверта клітинка
                elif self.Y <= 220 + cell.HEIGHT and 450 + cell.HEIGHT:
                    self.X = 425 + self.LIST_SHIP_4 + 6
                    self.Y = 225

                 # ряд четвертий четверта клітинка
                elif self.Y <= 245 + cell.HEIGHT and 450 + cell.HEIGHT:
                    self.X = 425 + self.LIST_SHIP_4 + 6
                    self.Y = 252

                # ряд пʼятий четверта клітинка
                elif self.Y <= 270 + cell.HEIGHT and 450 + cell.HEIGHT:
                    self.X = 425 + self.LIST_SHIP_4 + 6
                    self.Y = 279

                # ряд шостий четверта клітинка
                elif self.Y <= 295 + cell.HEIGHT and 450 + cell.HEIGHT:
                    self.X = 425 + self.LIST_SHIP_4 + 6
                    self.Y = 306
                    
                # ряд сьомий четверта клітинка
                elif self.Y <= 320 + cell.HEIGHT and 450 + cell.HEIGHT:
                    self.X = 425 + self.LIST_SHIP_4 + 6
                    self.Y = 333

                # ряд восьмий четверта клітинка     
                elif self.Y <= 345 + cell.HEIGHT and 450 + cell.HEIGHT:
                    self.X = 425 + self.LIST_SHIP_4 + 6
                    self.Y = 360

                # ряд девʼятий четверта клітинка
                elif self.Y <= 370 + cell.HEIGHT and 450 + cell.HEIGHT:
                    self.X = 425 + self.LIST_SHIP_4 + 6
                    self.Y = 387

                # ряд десятий четверта клітинка
                elif  self.Y <= 395 + cell.HEIGHT and 450 + cell.HEIGHT:
                    self.X = 425 + self.LIST_SHIP_4 + 6
                    self.Y = 414
                    

            # пʼята клітинка
            if self.X >= 450 and self.X <= 450 + cell.WIDTH:
                # ряд перший пʼята клітинка
                if self.Y <= 170 + cell.HEIGHT and 475 + cell.HEIGHT:
                    self.X = 450 + self.LIST_SHIP_4 + 8
                    self.Y = 171

                # ряд другий пʼята клітинка
                elif self.Y <= 195 + cell.HEIGHT and 475 + cell.HEIGHT:
                    self.X = 450 + self.LIST_SHIP_4 + 8 
                    self.Y = 198

                # ряд третій пʼята клітинка
                elif self.Y <= 220 + cell.HEIGHT and 475 + cell.HEIGHT:
                    self.X = 450 + self.LIST_SHIP_4 + 8 
                    self.Y = 225

                # ряд ччетвертий  пʼята клітинка
                elif self.Y <= 245 + cell.HEIGHT and 475 + cell.HEIGHT:
                    self.X = 450 + self.LIST_SHIP_4 + 8 
                    self.Y = 252

                # ряд пʼятий  пʼята клітинка
                elif self.Y <= 270 + cell.HEIGHT and 475 + cell.HEIGHT:
                    self.X = 450 + self.LIST_SHIP_4 + 8 
                    self.Y = 279

                # ряд шостий пʼята клітинка
                elif  self.Y <= 295 + cell.HEIGHT and 475 + cell.HEIGHT:
                    self.X = 450 + self.LIST_SHIP_4 + 8 
                    self.Y = 306

                # ряд сьомий пʼята клітинка
                elif  self.Y <= 320 + cell.HEIGHT and 475 + cell.HEIGHT:
                    self.X = 450 + self.LIST_SHIP_4 + 8
                    self.Y = 333
                
                # ряд восьмий пʼята клітинка
                elif  self.Y <= 345 + cell.HEIGHT and 475 + cell.HEIGHT:
                    self.X = 450 + self.LIST_SHIP_4 + 8 
                    self.Y = 360

                # ряд девʼятий пʼята клітинка
                elif  self.Y <= 370 + cell.HEIGHT and 475 + cell.HEIGHT:
                    self.X = 450 + self.LIST_SHIP_4 + 8 
                    self.Y = 387

                # ряд десятий пʼята клітинка
                elif  self.Y <= 395 + cell.HEIGHT and 475 + cell.HEIGHT:
                    self.X = 450 + self.LIST_SHIP_4 + 8 
                    self.Y = 414
                    
            # шоста клітинка
            if self.X >= 475 and self.X <= 475 + cell.WIDTH:
                # ряд перший шоста клітинка
                if self.Y <= 170 + cell.HEIGHT and 500 + cell.HEIGHT:
                    self.X = 475 + self.LIST_SHIP_4 + 10
                    self.Y = 171

                # ряд другий шоста клітинка
                elif self.Y <= 195 + cell.HEIGHT and 500 + cell.HEIGHT:
                    self.X = 475 + self.LIST_SHIP_4 + 10 
                    self.Y = 198

                # ряд третій шоста клітинка
                elif self.Y <= 220 + cell.HEIGHT and 500 + cell.HEIGHT:
                    self.X = 475 + self.LIST_SHIP_4 + 10 
                    self.Y = 225

                # ряд четвертий  шоста клітинка
                elif self.Y <= 245 + cell.HEIGHT and 500 + cell.HEIGHT:
                    self.X = 475 + self.LIST_SHIP_4 + 10 
                    self.Y = 252

                # ряд пʼятий шоста клітинка
                elif self.Y <= 270 + cell.HEIGHT and 500 + cell.HEIGHT:
                    self.X = 475 + self.LIST_SHIP_4 + 10 
                    self.Y = 279

                # ряд шостий шоста клітинка
                elif  self.Y <= 295 + cell.HEIGHT and 500 + cell.HEIGHT:
                    self.X = 475 + self.LIST_SHIP_4 + 10 
                    self.Y = 306

                # ряд сьомий шоста клітинка
                elif  self.Y <= 320 + cell.HEIGHT and 500 + cell.HEIGHT:
                    self.X = 475 + self.LIST_SHIP_4 + 10 
                    self.Y = 333

               # ряд восьмий шоста клітинка
                elif  self.Y <= 345 + cell.HEIGHT and 500 + cell.HEIGHT:
                    self.X = 475 + self.LIST_SHIP_4 + 10 
                    self.Y = 360
                
                # ряд девʼятий шоста клітинка
                elif  self.Y <= 370 + cell.HEIGHT and 500 + cell.HEIGHT:
                    self.X = 475 + self.LIST_SHIP_4 + 10
                    self.Y = 387

                # ряд десятий шоста клітинка
                elif  self.Y <= 395 + cell.HEIGHT and 500 + cell.HEIGHT:
                    self.X = 475 + self.LIST_SHIP_4 + 10 
                    self.Y = 414
                    
            # сьомий стовбчик
            if self.X >= 500 and self.X <= 500 + cell.WIDTH:
                # перший рядок сьома клітинка
                if self.Y <= 170 + cell.HEIGHT and 525 + cell.HEIGHT:
                    self.X = 500 + self.LIST_SHIP_4 + 12
                    self.Y = 171
                    self.set_ship(set_row= 0, set_cell_start= 6)
    
                # другий рядок сьома клітинка
                elif self.Y <= 195 + cell.HEIGHT and 525 + cell.HEIGHT:
                    self.X = 500 + self.LIST_SHIP_4 + 12
                    self.Y = 198
                    self.set_ship(set_row= 1, set_cell_start= 6)


                # третій рядок сьома клітинка
                elif self.Y <= 220 + cell.HEIGHT and 525 + cell.HEIGHT:
                    self.X = 500 + self.LIST_SHIP_4 + 12
                    self.Y = 225

                # четвертий рядок сьома клітинка
                elif self.Y <= 245 + cell.HEIGHT and 525 + cell.HEIGHT:
                    self.X = 500 + self.LIST_SHIP_4 + 12
                    self.Y = 252
                    self.set_ship(set_row= 3, set_cell_start= 6)

                # пʼятий  рядок сьома клітинка
                elif self.Y <= 270 + cell.HEIGHT and 525 + cell.HEIGHT:
                    self.X = 500 + self.LIST_SHIP_4 + 12
                    self.Y = 279

                # шостий рядок сьома клітинка
                elif  self.Y <= 295 + cell.HEIGHT and 525 + cell.HEIGHT:
                    self.X = 500 + self.LIST_SHIP_4 + 12
                    self.Y = 306

                # сьомий рядок сьома клітинка
                elif  self.Y <= 320 + cell.HEIGHT and 525 + cell.HEIGHT:
                    self.X = 500 + self.LIST_SHIP_4 + 12
                    self.Y = 333
                    
               # восьмий рядок сьома клітинка
                elif  self.Y <= 345 + cell.HEIGHT and 525 + cell.HEIGHT:
                    self.X = 500 + self.LIST_SHIP_4 + 12
                    self.Y = 360
                
                # девʼятий рядок сьома клітинка
                elif  self.Y <= 370 + cell.HEIGHT and 525 + cell.HEIGHT:
                    self.X = 500 + self.LIST_SHIP_4 + 12
                    self.Y = 387

                # десятий рядок сьома клітинка
                elif  self.Y <= 395 + cell.HEIGHT and 525 + cell.HEIGHT:
                    self.X = 500 + self.LIST_SHIP_4 + 12
                    self.Y = 414
                    self.set_ship(set_row= 9, set_cell_start= 6)

            # восьма клітнка
            if self.X >= 525 and self.X <= 525 + cell.WIDTH:
                # перший рядок восьма клітинка
                if self.Y <= 170 + cell.HEIGHT and 550 + cell.HEIGHT:
                    self.X = 500 + self.LIST_SHIP_4 + 14 
                    self.Y = 171
                
                # другий рядок восьма клітинка
                elif self.Y <= 195 + cell.HEIGHT and 550 + cell.HEIGHT:
                    self.X = 500 + self.LIST_SHIP_4 + 14 
                    self.Y = 198
                
                # третій рядок восьма клітинка
                elif self.Y <= 220 + cell.HEIGHT and 550 + cell.HEIGHT:
                    self.X = 500 + self.LIST_SHIP_4 + 14
                    self.Y = 225

                # четвертий рядок восьма клітинка
                elif self.Y <= 245 + cell.HEIGHT and 550 + cell.HEIGHT:
                    self.X = 500 + self.LIST_SHIP_4 + 14 
                    self.Y = 252

                # пʼятий рядок восьма клітинка
                elif  self.Y <= 270 + cell.HEIGHT and 550 + cell.HEIGHT:
                    self.X = 500 + self.LIST_SHIP_4 + 14 
                    self.Y = 279
                
                # шостий рядок восьма клітинка
                elif  self.Y <= 295 + cell.HEIGHT and 550 + cell.HEIGHT:
                    self.X = 500 + self.LIST_SHIP_4 + 14 
                    self.Y = 306
                        
                # сьомий рядок восьма клітинка
                elif  self.Y <= 320 + cell.HEIGHT and 550 + cell.HEIGHT:
                    self.X = 500 + self.LIST_SHIP_4 + 14 
                    self.Y = 333

                # восьмий рядок восьма клітинка
                elif self.Y <= 345 + cell.HEIGHT and 550 + cell.HEIGHT:
                    self.X = 500 + self.LIST_SHIP_4 + 14
                    self.Y = 360

                # девʼятий рядок восьма клітинка
                elif self.Y <= 370 + cell.HEIGHT and 550 + cell.HEIGHT:
                    self.X = 500 + self.LIST_SHIP_4 + 14 
                    self.Y = 387

                # десятий рядок восьма клітинка
                elif self.Y <= 395 + cell.HEIGHT and 550 + cell.HEIGHT:
                    self.X = 500 + self.LIST_SHIP_4 + 14 
                    self.Y = 414

            # девʼята клітинка
            if self.X >= 550 and self.X <= 550 + cell.WIDTH:
                # перший рядок девʼята клітинка
                if self.Y <= 170 + cell.HEIGHT and 575 + cell.HEIGHT:
                    self.X = 500 + self.LIST_SHIP_4 + 16
                    self.Y = 171


                # другий рядок девʼята клітинка 
                elif self.Y <= 195 + cell.HEIGHT and 575 + cell.HEIGHT:
                    self.X = 500 + self.LIST_SHIP_4 + 16
                    self.Y = 198
 
            
                # третій рядок девʼята клітинка
                elif self.Y <= 220 + cell.HEIGHT and 575 + cell.HEIGHT:
                    self.X = 500 + self.LIST_SHIP_4 + 16
                    self.Y = 225

                # четвертий рядок девʼята клітинка
                elif self.Y <= 245 + cell.HEIGHT and 575 + cell.HEIGHT:
                    self.X = 500 + self.LIST_SHIP_4 + 16
                    self.Y = 252

            
                # пʼятий рядок девʼята клітинка
                elif self.Y <= 270 + cell.HEIGHT and 575 + cell.HEIGHT:
                    self.X = 500 + self.LIST_SHIP_4 + 16
                    self.Y = 279
                
                # шостий рядок девʼята клітинка
                elif self.Y <= 295 + cell.HEIGHT and 575 + cell.HEIGHT:
                    self.X = 500 + self.LIST_SHIP_4 + 16 
                    self.Y = 306

                # сьомий рядок девʼята клітинка
                elif self.Y <= 320 + cell.HEIGHT and 575 + cell.HEIGHT:
                    self.X = 500 + self.LIST_SHIP_4 + 16 
                    self.Y = 333
                     
                # восьмий рядок девʼята клітинка
                elif  self.Y <= 345 + cell.HEIGHT and 575 + cell.HEIGHT:
                    self.X = 500 + self.LIST_SHIP_4 + 16 
                    self.Y = 360
                    
                # девʼятий рядок девʼята клітинка
                elif  self.Y <= 370 + cell.HEIGHT and 575 + cell.HEIGHT:
                    self.X = 500 + self.LIST_SHIP_4 + 16 
                    self.Y = 387
                
                # десятий рядок девʼята клітинка
                elif  self.Y <= 395 + cell.HEIGHT and 575 + cell.HEIGHT:
                    self.X = 500 + self.LIST_SHIP_4 + 16
                    self.Y = 414

            # десята клітинка
            if self.X >= 575 and self.X <= 575 + cell.WIDTH: 
                # перший рядок десята клітинка               
                if self.Y <= 170 + cell.HEIGHT and 600 + cell.HEIGHT:
                    self.X = 500 + self.LIST_SHIP_4 + 18 
                    self.Y = 171
                # другий рядок десята клітинка 
                elif self.Y <= 195 + cell.HEIGHT and 600 + cell.HEIGHT:
                   self.X = 500 + self.LIST_SHIP_4 + 18 
                   self.Y = 198
                # третій рядок десята клітинка 
                elif  self.Y <= 220 + cell.HEIGHT and 600 + cell.HEIGHT:
                    self.X = 500 + self.LIST_SHIP_4 + 18 
                    self.Y = 225
                # четвертий рядок десята клітинка 
                elif  self.Y <= 245 + cell.HEIGHT and 600 + cell.HEIGHT:
                    self.X = 500 + self.LIST_SHIP_4 + 18 
                    self.Y = 252
                # пʼятий рядок десята клітинка 
                elif  self.Y <= 270 + cell.HEIGHT and 600 + cell.HEIGHT:
                    self.X = 500 + self.LIST_SHIP_4 + 18 
                    self.Y = 279
                # шостий рядок десята клітинка 
                elif  self.Y <= 295 + cell.HEIGHT and 600 + cell.HEIGHT:
                    self.X = 500 + self.LIST_SHIP_4 + 18 
                    self.Y = 306
                # сьомий рядок десята клітинка       
                elif  self.Y <= 320 + cell.HEIGHT and 600 + cell.HEIGHT:
                    self.X = 500 + self.LIST_SHIP_4 + 18 
                    self.Y = 333
                # восьмий рядок десята клітинка 
                elif self.Y <= 345 + cell.HEIGHT and 600 + cell.HEIGHT:
                    self.X = 500 + self.LIST_SHIP_4 + 18 
                    self.Y = 360
                # девʼятий рядок десята клітинка 
                elif self.Y <= 370 + cell.HEIGHT and 600 + cell.HEIGHT:
                    self.X = 500 + self.LIST_SHIP_4 + 18 
                    self.Y = 387
                # десятий рядок десята клітинка     
                elif self.Y <= 395 + cell.HEIGHT and 600 + cell.HEIGHT:
                    self.X = 500 + self.LIST_SHIP_4 + 18 
                    self.Y = 414                           

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

