import pygame
import modules.main_modules.data_base as m_data
import modules.blit_el_ship.ship_4_blit as m_ship
import random
pygame.init()

class Bot(m_ship.Ship_4):
    def __init__(self):
        m_ship.Ship_4.__init__(self)

        self.RANDOM_NUMBER = 0
        self.COUNT = True 
    #def who_turn(x,y, number):
    #if step[0] == 'cross':
    #    screen.blit(list_cross[0], (x,y))
    #    step[0] = 'zero'    
    #    list_cell[number] = 1
    #elif step[0] == 'zero':
    #    screen.blit(zero_img, (x,y))
    #    step[0] = 'cross'  
    #    list_cell[number] = 2

    def who_turn(self):
        if m_data.step[0] == 'player':
            pass
        elif m_data.step[0] == 'bot':
            pass

    def random_number_bot(self, set_num_1, set_num_2):
        bot_number = random.randint(set_num_1, set_num_2)
        while bot_number == 1 or bot_number == 2 or bot_number == 3 or bot_number == 4:
            bot_number = random.randint(set_num_1, set_num_2)
            #m_data.list_map_bot1.append(bot_number)

            #index = m_data.list_map_bot.index()
            #m_data.list_map_bot.append(index)

            for i in range(10):
                m_data.list_map_bot1.append(bot_number)

            if self.COUNT:
                for i in m_data.list_map_bot1:
                    print(i)
                print("\n")
                self.COUNT = False

        self.RANDOM_bot_number = bot_number
bot = Bot()
#bot.random_number_bot(set_num_1= 1, set_num_2= 4)


    
    


        
    