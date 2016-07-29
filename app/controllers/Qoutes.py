from system.core.controller import *


class Qoutes(Controller):
    def __init__(self, action):
        super(Qoutes, self).__init__(action)
    
        self.load_model('QoutesModel')
        self.db = self._app.db

    def success(self):
    	show = self.models['QoutesModel.py'].show_qoutes()
        return self.load_view('qoutes/success.html', shows = show)