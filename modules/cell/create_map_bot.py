import modules.main_modules.settings as m_settings
import modules.main_modules.data_base as m_data
import modules.cell.model_cell_bot as m_model_bot

class Map_bot(m_settings.Settings):
    def __init__(self, x2= 545, y2= 170):
        m_settings.Settings.__init__(self, x= x2, y= y2)

    def create_map_bot(self):
        x = self.X
        y = self.Y

        for list_model in m_data.list_map_two_bot:
            for model in list_model:
                if model == 0:
                    model_bot = m_model_bot.Model_bot(x2= x, y2= y)
                    model_bot.create_model_bot(set_column= 2, set_row= 2, width= 27, height= 27, file_name= "img/cell/center_cell.png")
                    m_data.list_models_bot.append(model_bot)
                x = x + 54
            y = y + 54
            x = self.X
            
map_bot = Map_bot()
map_bot.create_map_bot()
                
            