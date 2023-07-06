import modules.main_modules.settings as m_settings
import modules.main_modules.data_base as m_data
import modules.cell.model_cell as m_model

class Map(m_settings.Settings):
    def __init__(self, x1= 190, y1= 170):
        m_settings.Settings.__init__(self, x= x1, y= y1)
        
    def create_map(self):
        x = self.X
        y = self.Y
        
        for list_model in m_data.list_map_one:
            for model in list_model:
                if model == 0:
                    block = m_model.Model(x1= x, y1= y)
                    block.create_model(set_column= 2, set_row= 2, width= 27, height= 27, file_name= "img/cell/center_cell.png")
                    m_data.list_models.append(block)
                x = x + 54
            y = y + 54
            x = self.X

map1 = Map()
map1.create_map()