import pygame 
import modules.blit_el_ship.blit_elements as m_elements
import modules.main_modules.data_base as m_data
import modules.cell.model_cell as m_model
import modules.cell.create_map as m_map
import modules.cell.create_cell as m_cell
import modules.cell.model_cell_bot as m_model_bot
import modules.cell.create_map_bot as m_map_bot
import modules.blit_el_ship.create_bot as m_bot 
import modules.blit_el_ship.ship_4_blit as m_ship
import modules.blit_el_ship.create_bot as m_bot 

pygame.init()

sc_width = 1000
sc_height = 650
screen = pygame.display.set_mode((sc_width,sc_height))
pygame.display.set_caption('Морський бій')

button_start = False
button_ready = False

button_turn = False
turn_4 = False

# 4
moving_ship_4 = False
start_pos_ship_4_X = m_ship.ship_4.X
start_pos_ship_4_Y = m_ship.ship_4.Y
blit_ship_4 = False 

# 3_1
moving_ship_3_1 = False
start_pos_ship_3_1_X = m_ship.ship_3_1.X
start_pos_ship_3_1_Y = m_ship.ship_3_1.Y
blit_ship_3_1 = False
end_blit_ship_3_1 = [False]

# 3_2
moving_ship_3_2 = False
start_pos_ship_3_2_X = m_ship.ship_3_2.X
start_pos_ship_3_2_Y = m_ship.ship_3_2.Y
blit_ship_3_2 = False
end_blit_ship_3_2 = False

# 2_1 
moving_ship_2_1 = False
start_pos_ship_2_1_X = m_ship.ship_2_1.X
start_pos_ship_2_1_Y = m_ship.ship_2_1.Y
blit_ship_2_1 = False
end_blit_ship_2_1 = False

#2_2
moving_ship_2_2 = False
start_pos_ship_2_2_X = m_ship.ship_2_2.X
start_pos_ship_2_2_Y = m_ship.ship_2_2.Y
blit_ship_2_2 = False
end_blit_ship_2_2 = False

# 2_3 
moving_ship_2_3 = False
start_pos_ship_2_3_X = m_ship.ship_2_3.X
start_pos_ship_2_3_Y = m_ship.ship_2_3.Y
blit_ship_2_3 = False
end_blit_ship_2_3 = False

# 1_1
moving_ship_1_1 = False
start_pos_ship_1_1_X = m_ship.ship_1_1.X
start_pos_ship_1_1_Y = m_ship.ship_1_1.Y
blit_ship_1_1 = False
end_blit_ship_1_1 = False

# 1_2
moving_ship_1_2 = False
start_pos_ship_1_2_X = m_ship.ship_1_2.X
start_pos_ship_1_2_Y = m_ship.ship_1_2.Y
blit_ship_1_2 = False
end_blit_ship_1_2 = False

# 1_3
moving_ship_1_3 = False
start_pos_ship_1_3_X = m_ship.ship_1_3.X
start_pos_ship_1_3_Y = m_ship.ship_1_3.Y
blit_ship_1_3 = False
end_blit_ship_1_3 = False

# 1_4
moving_ship_1_4 = False
start_pos_ship_1_4_X = m_ship.ship_1_4.X
start_pos_ship_1_4_Y = m_ship.ship_1_4.Y
blit_ship_1_4 = False
end_blit_ship_1_4 = False

game = True
while game:  
    m_elements.bg.blit_sprite(screen= screen)
    m_elements.start.blit_sprite(screen= screen)

    m_ship.ship_4.vertical_turn()
    m_ship.ship_4.horizontal_turn()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

        # start 
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            X_Y_start = event.pos  
            if 387 <= X_Y_start[0] <= 621 and 270 <= X_Y_start[1] <= 330:
                button_start = True

        # ready 
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            X_Y_ready = event.pos  
            if m_elements.ready.X <= X_Y_ready[0] <= m_elements.ready.X + m_elements.ready.WIDTH and m_elements.ready.Y <= X_Y_ready[1] <= m_elements.ready.Y + m_elements.ready.HEIGHT:
                button_ready = True

        # 4 
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:       
            X_Y_ship_4 = event.pos
            if m_ship.ship_4.X <= X_Y_ship_4[0] <= m_ship.ship_4.X + m_ship.ship_4.WIDTH and m_ship.ship_4.Y <= X_Y_ship_4[1] <= m_ship.ship_4.Y + m_ship.ship_4.HEIGHT:
                if m_data.end_blit_ship_4[0] == False:
                    moving_ship_4 = True
                
        if event.type == pygame.MOUSEMOTION and event.buttons[0] == 1:
            if moving_ship_4:
                m_ship.ship_4.X = event.pos[0]
                m_ship.ship_4.Y = event.pos[1]

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if moving_ship_4:
                if m_ship.ship_4.X < 190 or m_ship.ship_4.X > 465 or m_ship.ship_4.Y < 170 or m_ship.ship_4.Y > 444:
                    m_ship.ship_4.X = start_pos_ship_4_X 
                    m_ship.ship_4.Y = start_pos_ship_4_Y 
                    moving_ship_4 = False
                else:
                    m_data.end_blit_ship_4[0] = True
                    moving_ship_4 = False

                    m_ship.ship_4.collision_ship_4()

                    # 3_1 
                    if m_data.end_blit_ship_4[0]:
                        blit_ship_3_1 = True
                    
        # 3
        if blit_ship_3_1: 
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                X_Y_ship_3_1 = event.pos
                if m_ship.ship_3_1.X <= X_Y_ship_3_1[0] <= m_ship.ship_3_1.X + m_ship.ship_3_1.WIDTH and 180 <= X_Y_ship_3_1[1] <= 205:
                    if m_data.end_blit_ship_3_1[0] == False:  
                        moving_ship_3_1 = True

            if event.type == pygame.MOUSEMOTION and event.buttons[0] == 1:
                if moving_ship_3_1:
                    m_ship.ship_3_1.X = event.pos[0]
                    m_ship.ship_3_1.Y = event.pos[1]
            
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if moving_ship_3_1:
                    if m_ship.ship_3_1.X < 190 or m_ship.ship_3_1.X > 465 or m_ship.ship_3_1.Y < 180 or m_ship.ship_3_1.Y > 444:
                        m_ship.ship_3_1.X = start_pos_ship_3_1_X
                        m_ship.ship_3_1.Y = start_pos_ship_3_1_Y  
                        moving_ship_3_1 = False
                    else:
                        m_data.end_blit_ship_3_1[0] = True
                        moving_ship_3_1 = False

                        m_ship.ship_3_1.collision_ship_4()

                        blit_ship_3_2 = True

        if blit_ship_3_2:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                X_Y_ship_3_2 = event.pos
                if m_ship.ship_3_2.X <= X_Y_ship_3_2[0] <= m_ship.ship_3_2.X + m_ship.ship_3_1.WIDTH and 230 <= X_Y_ship_3_2[1] <= 255:
                    if m_data.end_blit_ship_3_2[0] == False:  
                        moving_ship_3_2 = True

            if event.type == pygame.MOUSEMOTION and event.buttons[0] == 1:
                if moving_ship_3_2:
                    m_ship.ship_3_2.X = event.pos[0]
                    m_ship.ship_3_2.Y = event.pos[1]

            if event.type == pygame.MOUSEBUTTONUP and event.button == 1: 
                if moving_ship_3_2:
                    if m_ship.ship_3_2.X < 190 or m_ship.ship_3_2.X > 465 or m_ship.ship_3_2.Y < 180 or m_ship.ship_3_2.Y > 444:
                        m_ship.ship_3_2.X = start_pos_ship_3_2_X
                        m_ship.ship_3_2.Y = start_pos_ship_3_2_Y 
                        moving_ship_3_2 = False
                    else:
                        m_data.end_blit_ship_3_2[0] = True
                        moving_ship_3_2 = False   
                        
                        m_ship.ship_3_2.collision_ship_4()

                        # 2_1
                        if m_data.end_blit_ship_3_2[0]:
                            blit_ship_2_1 = True

        # 2
        if blit_ship_2_1:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                X_Y_ship_2_1 = event.pos
                if m_ship.ship_2_1.X <= X_Y_ship_2_1[0] <= m_ship.ship_2_1.X + m_ship.ship_2_1.WIDTH and 180 <= X_Y_ship_2_1[1] <= 205:
                    if m_data.end_blit_ship_2_1[0] == False: 
                        moving_ship_2_1 = True

            if event.type == pygame.MOUSEMOTION and event.buttons[0] == 1:
                if moving_ship_2_1:
                    m_ship.ship_2_1.X = event.pos[0]
                    m_ship.ship_2_1.Y = event.pos[1]

            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if moving_ship_2_1:
                    if m_ship.ship_2_1.X < 190 or m_ship.ship_2_1.X > 465 or m_ship.ship_2_1.Y < 180 or m_ship.ship_2_1.Y > 444:
                        m_ship.ship_2_1.X = start_pos_ship_2_1_X
                        m_ship.ship_2_1.Y = start_pos_ship_2_1_Y 
                        moving_ship_2_1 = False
                    else:
                        m_data.end_blit_ship_2_1[0] = True
                        moving_ship_2_1 = False   
                        m_ship.ship_2_1.collision_ship_4()

                        # 2_2
                        blit_ship_2_2 = True
        
        if blit_ship_2_2:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                X_Y_ship_2_2 = event.pos
                if m_ship.ship_2_2.X <= X_Y_ship_2_2[0] <= m_ship.ship_2_2.X + m_ship.ship_2_2.WIDTH and 230 <= X_Y_ship_2_2[1] <= 255:
                    if m_data.end_blit_ship_2_2[0] == False:  
                        moving_ship_2_2 = True

            if event.type == pygame.MOUSEMOTION and event.buttons[0] == 1:
                if moving_ship_2_2:
                    m_ship.ship_2_2.X = event.pos[0]
                    m_ship.ship_2_2.Y = event.pos[1]

            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if moving_ship_2_2:
                    if m_ship.ship_2_2.X < 190 or m_ship.ship_2_2.X > 465 or m_ship.ship_2_2.Y < 180 or m_ship.ship_2_2.Y > 444:
                        m_ship.ship_2_2.X = start_pos_ship_2_2_X
                        m_ship.ship_2_2.Y = start_pos_ship_2_2_Y 
                        moving_ship_2_2 = False
                    else:
                        m_data.end_blit_ship_2_2[0] = True
                        moving_ship_2_2 = False   

                        m_ship.ship_2_2.collision_ship_4()
                        
                        # 2_3
                        blit_ship_2_3 = True
        
        if blit_ship_2_3:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                X_Y_ship_2_3 = event.pos
                if m_ship.ship_2_3.X <= X_Y_ship_2_3[0] <= m_ship.ship_2_3.X + m_ship.ship_2_3.WIDTH and 280 <= X_Y_ship_2_3[1] <= 305:
                    if m_data.end_blit_ship_2_3[0] == False:  
                        moving_ship_2_3 = True

            if event.type == pygame.MOUSEMOTION and event.buttons[0] == 1:
                if moving_ship_2_3:
                    m_ship.ship_2_3.X = event.pos[0]
                    m_ship.ship_2_3.Y = event.pos[1]

            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if moving_ship_2_3:
                    if m_ship.ship_2_3.X < 190 or m_ship.ship_2_3.X > 465 or m_ship.ship_2_3.Y < 180 or m_ship.ship_2_3.Y > 444:
                        m_ship.ship_2_3.X = start_pos_ship_2_3_X
                        m_ship.ship_2_3.Y = start_pos_ship_2_3_Y 
                        moving_ship_2_3 = False
                    else:
                        m_data.end_blit_ship_2_3[0] = True
                        moving_ship_2_3 = False  

                        m_ship.ship_2_3.collision_ship_4() 

                        # 1_1
                        if m_data.end_blit_ship_2_3[0]:
                            blit_ship_1_1 = True
        
        # 1               
        if blit_ship_1_1:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                X_Y_ship_1_1 = event.pos
                if m_ship.ship_1_1.X <= X_Y_ship_1_1[0] <= m_ship.ship_1_1.X + m_ship.ship_1_1.WIDTH and 180 <= X_Y_ship_1_1[1] <= 205:
                    if m_data.end_blit_ship_1_1[0] == False:  
                        moving_ship_1_1 = True

            if event.type == pygame.MOUSEMOTION and event.buttons[0] == 1:
                if moving_ship_1_1:
                    m_ship.ship_1_1.X = event.pos[0]
                    m_ship.ship_1_1.Y = event.pos[1]

            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if moving_ship_1_1:
                    if m_ship.ship_1_1.X < 190 or m_ship.ship_1_1.X > 465 or m_ship.ship_1_1.Y < 180 or m_ship.ship_1_1.Y > 444:
                        m_ship.ship_1_1.X = start_pos_ship_1_1_X
                        m_ship.ship_1_1.Y = start_pos_ship_1_1_Y 
                        moving_ship_1_1 = False
                    else:
                        m_data.end_blit_ship_1_1[0] = True
                        moving_ship_1_1 = False   

                        m_ship.ship_1_1.collision_ship_4() 
                        # 1_2
                        blit_ship_1_2 = True

        if blit_ship_1_2:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                X_Y_ship_1_2 = event.pos
                if m_ship.ship_1_2.X <= X_Y_ship_1_2[0] <= m_ship.ship_1_2.X + m_ship.ship_1_2.WIDTH and 230 <= X_Y_ship_1_2[1] <= 255:
                    if m_data.end_blit_ship_1_2[0] == False:  
                        moving_ship_1_2 = True

            if event.type == pygame.MOUSEMOTION and event.buttons[0] == 1:
                if moving_ship_1_2:
                    m_ship.ship_1_2.X = event.pos[0]
                    m_ship.ship_1_2.Y = event.pos[1]

            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if moving_ship_1_2:
                    if m_ship.ship_1_2.X < 190 or m_ship.ship_1_2.X > 465 or m_ship.ship_1_2.Y < 180 or m_ship.ship_1_2.Y > 444:
                        m_ship.ship_1_2.X = start_pos_ship_1_2_X
                        m_ship.ship_1_2.Y = start_pos_ship_1_2_Y 
                        moving_ship_1_2 = False
                    else:
                        m_data.end_blit_ship_1_2[0] = True
                        moving_ship_1_2 = False   

                        m_ship.ship_1_2.collision_ship_4()
                        # 1_3
                        blit_ship_1_3 = True

        if blit_ship_1_3:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                X_Y_ship_1_3 = event.pos
                if m_ship.ship_1_3.X <= X_Y_ship_1_3[0] <= m_ship.ship_1_3.X + m_ship.ship_1_3.WIDTH and 280 <= X_Y_ship_1_3[1] <= 305:
                    if m_data.end_blit_ship_1_3[0] == False:  
                        moving_ship_1_3 = True

            if event.type == pygame.MOUSEMOTION and event.buttons[0] == 1:
                if moving_ship_1_3:
                    m_ship.ship_1_3.X = event.pos[0]
                    m_ship.ship_1_3.Y = event.pos[1]

            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if moving_ship_1_3:
                    if m_ship.ship_1_3.X < 190 or m_ship.ship_1_3.X > 465 or m_ship.ship_1_3.Y < 180 or m_ship.ship_1_3.Y > 444:
                        m_ship.ship_1_3.X = start_pos_ship_1_3_X
                        m_ship.ship_1_3.Y = start_pos_ship_1_3_Y 
                        moving_ship_1_3 = False
                    else:
                        m_data.end_blit_ship_1_3[0] = True
                        moving_ship_1_3 = False   
                        
                        m_ship.ship_1_3.collision_ship_4()

                        # 1_4
                        blit_ship_1_4 = True
                
        if blit_ship_1_4:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                X_Y_ship_1_4 = event.pos
                if m_ship.ship_1_4.X <= X_Y_ship_1_4[0] <= m_ship.ship_1_4.X + m_ship.ship_1_4.WIDTH and 330 <= X_Y_ship_1_4[1] <= 355:
                    if m_data.end_blit_ship_1_4[0] == False:  
                        moving_ship_1_4 = True

            if event.type == pygame.MOUSEMOTION and event.buttons[0] == 1:
                if moving_ship_1_4:
                    m_ship.ship_1_4.X = event.pos[0]
                    m_ship.ship_1_4.Y = event.pos[1]

            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if moving_ship_1_4:
                    if m_ship.ship_1_4.X < 190 or m_ship.ship_1_4.X > 625 or m_ship.ship_1_4.Y < 180 or m_ship.ship_1_4.Y > 444:
                        m_ship.ship_1_4.X = start_pos_ship_1_4_X
                        m_ship.ship_1_4.Y = start_pos_ship_1_4_Y 
                        moving_ship_1_4 = False
                    else:
                        m_data.end_blit_ship_1_4[0] = True
                        moving_ship_1_4 = False

                        if m_data.end_blit_ship_1_4[0]:
                            m_ship.ship_4.READY = True
                            
                        m_ship.ship_1_4.collision_ship_4()
        
    if button_start:
        m_elements.bg.blit_sprite(screen= screen)

        for cell in m_data.list_cells:
            cell.blit_sprite(screen= screen)

        m_ship.ship_4.blit_sprite(screen= screen)

        if blit_ship_3_1:
            m_ship.ship_3_1.blit_sprite(screen= screen)
            m_ship.ship_3_2.blit_sprite(screen= screen)

        if blit_ship_2_1:
            m_ship.ship_2_1.blit_sprite(screen= screen)
            m_ship.ship_2_2.blit_sprite(screen= screen)
            m_ship.ship_2_3.blit_sprite(screen= screen)

        if blit_ship_1_1:
            m_ship.ship_1_1.blit_sprite(screen= screen)
            m_ship.ship_1_2.blit_sprite(screen= screen)                                   
            m_ship.ship_1_3.blit_sprite(screen= screen)
            m_ship.ship_1_4.blit_sprite(screen= screen)
    
        if m_ship.ship_4.READY: 
            m_elements.ready.blit_sprite(screen= screen)
            if button_ready:
                for cell in m_data.list_cells_bot:
                    cell.blit_sprite(screen= screen)
                    m_bot.bot.set_ship_bot()

                    m_bot.ship_3_1.set_ship_bot()
                    m_bot.ship_3_2.set_ship_bot()

                    m_bot.ship_2_1.set_ship_bot()
                    m_bot.ship_2_2.set_ship_bot()
                    m_bot.ship_2_3.set_ship_bot()

                    m_bot.ship_1_1.set_ship_bot()
                    m_bot.ship_1_2.set_ship_bot()
                    m_bot.ship_1_3.set_ship_bot()
                    m_bot.ship_1_4.set_ship_bot()


    pygame.display.flip()
    
