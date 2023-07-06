import modules.main_modules.settings as m_settings
import modules.main_modules.data_base as m_data
import modules.cell.create_cell as m_cell
import modules.blit_el_ship.ship_4_blit as m_ship

class Model(m_settings.Settings):
    def __init__(self, width1= 0, height1= 0, x1= 0, y1= 0, file_name1= None):
        m_settings.Settings.__init__(self, width= width1, height= height1, x= x1, y= y1, file_name= file_name1)

    def create_model(self, set_column, set_row, width, height, file_name):
        x = self.X
        y = self.Y
        for count in range(set_column):
            for count in range(set_row):
                cell = m_cell.Cell(width1= width, height1= height, file_name1= file_name)
                cell.X = x
                cell.Y = y
                m_data.list_cells.append(cell)
                x = x + cell.WIDTH
            y = y + cell.HEIGHT
            x = self.X
        
