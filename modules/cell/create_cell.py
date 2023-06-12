import modules.main_modules.settings as m_settings

class Cell(m_settings.Settings):
    def __init__(self, width1 = 0, height1= 0, x1= 0, y1= 0, file_name1= None):
        m_settings.Settings.__init__(self, width= width1, height= height1, x= x1, y = y1, file_name= file_name1)
        self.load_image()
