from system.core.controller import *


class Qoutes(Controller):
    def __init__(self, action):
        super(Qoutes, self).__init__(action)
    
        self.load_model('QoutesModel')
        self.db = self._app.db