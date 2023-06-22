import modules.main_modules.settings as m_settings
import modules.main_modules.data_base as m_data
import modules.cell.create_cell as m_cell

class Model_bot(m_settings.Settings):
    def __init__(self, width2= 0, height2= 0, x2= 0, y2= 0, file_name2= None):
       m_settings.Settings.__init__(self, width= width2, height= height2, x= x2, y= y2, file_name= file_name2)

    def create_model_bot(self, set_column, set_row, width, height, file_name):
        x = self.X
        y = self.Y
        for count in range(set_column):
            for count in range(set_row):
                cell_bot = m_cell.Cell(width1= width, height1= height, file_name1= file_name)
                cell_bot.X = x
                cell_bot.Y = y
                m_data.list_cells_bot.append(cell_bot)
                x = x + cell_bot.WIDTH
            y = y + cell_bot.HEIGHT
            x = self.X