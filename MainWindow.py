from PyQt5 import QtGui, QtCore, QtWidgets, uic
import logging
from Button import *
from BtnDb import BtnDb
from LogData import LogData

debug_logger = logging.getLogger(__name__)


class Main(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self, parent=None)
        self.ui = uic.loadUi('main.ui', self)
        self.ui.show()
        self.btn_array = ButtonArray()

        # Add button to the btn array
        for btn in self.create_buttons():
            self.btn_array.add_btn(btn)

    def on_btn_clicked(self, text):
        """
        Common slot for all
        :return:
        """
        db_logger = LogData()
        db_logger.add_data(text)

        print (text)

    ### All methods RPC methods ###
    def get_btns(self):
        debug_logger.debug(str(self.btn_array))
        return str(self.btn_array)

    def set_btn_text(self, id, text):
        try:
            self.btn_array[id].setText(text)
        except KeyError:
            pass

    ### RPC Calback Methods End ###

    def create_dispatcher(self):
        dispatcher = {'get_btns':     self.get_btns,
                      'set_btn_text': self.set_btn_text,
                      'update_image': self.update_btn,
                      'get_log_data': self.get_log_data}
        return dispatcher

    def update_btn(self, id, text, file_name):
        # Add to the database
        btn_db = BtnDb()
        btn_db.add_data(id, text, file_name)
        btn = self.btn_array.get_btn(int(id))
        btn.set_text(text)
        btn.set_pic(QtGui.QIcon(file_name), QtCore.QSize(btn.btn_width(), btn.btn_height()))
        btn.set_uri(file_name)

    def recreate_btn(self, id):
        pass

    def get_log_data(self):
        db_logger = LogData()
        return db_logger.get_data()

    def create_buttons(self):
        qbtns = [self.ui.btn1,
                 self.ui.btn2,
                 self.ui.btn3,
                 self.ui.btn4,
                 self.ui.btn5,
                 self.ui.btn6,
                 self.ui.btn7,
                 self.ui.btn8,
                 self.ui.btn9,
                 self.ui.btn10,
                 self.ui.btn11,
                 self.ui.btn12]

        btn_db = BtnDb()
        row = btn_db.get_btns()
        btns = []
        for i, btn in enumerate(row):
            btns.append(Button.builder()
                        .btn(qbtns[int(btn[0])])
                        .id(int(btn[0]))
                        .text(btn[1])
                        .pic(QtGui.QIcon(btn[2]))
                        .uri(btn[2])
                        .icon_size(QtCore.QSize(qbtns[i].width(), qbtns[i].height()))
                        .callback(self.on_btn_clicked)
                        .build())

        return btns
