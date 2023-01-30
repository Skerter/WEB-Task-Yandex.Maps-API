import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(854, 526)
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.keyboard = QtWidgets.QLabel(self.centralwidget)
        self.keyboard.setGeometry(QtCore.QRect(0, -30, 681, 351))
        self.keyboard.setText("")
        self.keyboard.setPixmap(QtGui.QPixmap("_im.png"))
        self.keyboard.setObjectName("keyboard")
        self.f1 = QtWidgets.QLabel(self.centralwidget)
        self.f1.setGeometry(QtCore.QRect(70, 20, 21, 31))
        self.f1.setObjectName("f1")
        self.f4 = QtWidgets.QLabel(self.centralwidget)
        self.f4.setGeometry(QtCore.QRect(200, 20, 21, 31))
        self.f4.setObjectName("f4")
        self.f3 = QtWidgets.QLabel(self.centralwidget)
        self.f3.setGeometry(QtCore.QRect(160, 20, 21, 31))
        self.f3.setObjectName("f3")
        self.f2 = QtWidgets.QLabel(self.centralwidget)
        self.f2.setGeometry(QtCore.QRect(110, 20, 21, 31))
        self.f2.setObjectName("f2")
        self.esc = QtWidgets.QLabel(self.centralwidget)
        self.esc.setGeometry(QtCore.QRect(30, 20, 21, 31))
        self.esc.setObjectName("esc")
        self.f5 = QtWidgets.QLabel(self.centralwidget)
        self.f5.setGeometry(QtCore.QRect(240, 20, 21, 31))
        self.f5.setObjectName("f5")
        self.f6 = QtWidgets.QLabel(self.centralwidget)
        self.f6.setGeometry(QtCore.QRect(290, 20, 21, 31))
        self.f6.setObjectName("f6")
        self.f7 = QtWidgets.QLabel(self.centralwidget)
        self.f7.setGeometry(QtCore.QRect(330, 20, 21, 31))
        self.f7.setObjectName("f7")
        self.W = QtWidgets.QLabel(self.centralwidget)
        self.W.setGeometry(QtCore.QRect(140, 90, 21, 31))
        self.W.setObjectName("W")
        self.S = QtWidgets.QLabel(self.centralwidget)
        self.S.setGeometry(QtCore.QRect(150, 130, 21, 31))
        self.S.setObjectName("S")
        self.A = QtWidgets.QLabel(self.centralwidget)
        self.A.setGeometry(QtCore.QRect(110, 130, 21, 31))
        self.A.setObjectName("A")
        self.D = QtWidgets.QLabel(self.centralwidget)
        self.D.setGeometry(QtCore.QRect(190, 130, 21, 31))
        self.D.setObjectName("D")
        self.Ctrl = QtWidgets.QLabel(self.centralwidget)
        self.Ctrl.setGeometry(QtCore.QRect(30, 220, 21, 31))
        self.Ctrl.setObjectName("Ctrl")
        self.Alt = QtWidgets.QLabel(self.centralwidget)
        self.Alt.setGeometry(QtCore.QRect(160, 220, 21, 31))
        self.Alt.setObjectName("Alt")
        self.Win = QtWidgets.QLabel(self.centralwidget)
        self.Win.setGeometry(QtCore.QRect(110, 220, 21, 31))
        self.Win.setObjectName("Win")
        self.ShifL = QtWidgets.QLabel(self.centralwidget)
        self.ShifL.setGeometry(QtCore.QRect(30, 180, 41, 31))
        self.ShifL.setObjectName("ShifL")
        self.Enter = QtWidgets.QLabel(self.centralwidget)
        self.Enter.setGeometry(QtCore.QRect(560, 130, 41, 31))
        self.Enter.setObjectName("Enter")
        self.Backspace = QtWidgets.QLabel(self.centralwidget)
        self.Backspace.setGeometry(QtCore.QRect(560, 50, 91, 31))
        self.Backspace.setObjectName("Backspace")
        self.dlt = QtWidgets.QLabel(self.centralwidget)
        self.dlt.setGeometry(QtCore.QRect(590, 20, 21, 31))
        self.dlt.setObjectName("dlt")
        self.Tab = QtWidgets.QLabel(self.centralwidget)
        self.Tab.setGeometry(QtCore.QRect(30, 90, 41, 31))
        self.Tab.setObjectName("Tab")
        self.A_10 = QtWidgets.QLabel(self.centralwidget)
        self.A_10.setGeometry(QtCore.QRect(30, 50, 21, 31))
        self.A_10.setObjectName("A_10")
        self.ShiftR = QtWidgets.QLabel(self.centralwidget)
        self.ShiftR.setGeometry(QtCore.QRect(540, 180, 41, 31))
        self.ShiftR.setObjectName("ShiftR")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 854, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "skolkovo"))
        self.f1.setText(_translate("MainWindow", "F1"))
        self.f4.setText(_translate("MainWindow", "F4"))
        self.f3.setText(_translate("MainWindow", "F3"))
        self.f2.setText(_translate("MainWindow", "F2"))
        self.esc.setText(_translate("MainWindow", "Esc"))
        self.f5.setText(_translate("MainWindow", "F5"))
        self.f6.setText(_translate("MainWindow", "F6"))
        self.f7.setText(_translate("MainWindow", "F7"))
        self.W.setText(_translate("MainWindow", "W"))
        self.S.setText(_translate("MainWindow", "S"))
        self.A.setText(_translate("MainWindow", "A"))
        self.D.setText(_translate("MainWindow", "D"))
        self.Ctrl.setText(_translate("MainWindow", "Ctrl"))
        self.Alt.setText(_translate("MainWindow", "Alt"))
        self.Win.setText(_translate("MainWindow", "Win"))
        self.ShifL.setText(_translate("MainWindow", "Shift"))
        self.Enter.setText(_translate("MainWindow", "Enter"))
        self.Backspace.setText(_translate("MainWindow", "Backspace"))
        self.dlt.setText(_translate("MainWindow", "Dlt"))
        self.Tab.setText(_translate("MainWindow", "Tab"))
        self.A_10.setText(_translate("MainWindow", "`"))
        self.ShiftR.setText(_translate("MainWindow", "Shift"))


keymap = {}
for key, value in vars(Qt).items():
    if isinstance(value, Qt.Key):
        keymap[value] = key.partition('_')[2]

modmap = {
    Qt.ControlModifier: keymap[Qt.Key_Control],
    Qt.AltModifier: keymap[Qt.Key_Alt],
    Qt.ShiftModifier: keymap[Qt.Key_Shift],
    Qt.MetaModifier: keymap[Qt.Key_Meta],
    Qt.GroupSwitchModifier: keymap[Qt.Key_AltGr],
    Qt.KeypadModifier: keymap[Qt.Key_NumLock],
}


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.prev_key = []

    def keyPressEvent(self, event):
        _key, _keys = self.keyevent_to_string(event)
        # раскомментируйте строку  ниже, чтобы увидеть что происходит
        print(f'------> {_key}, {event.text()}, {event.key()}, {_keys}')

        key = event.key()

        if self.prev_key:
            for k in self.prev_key:
                k.setStyleSheet("")

        if _keys[0] == 'Control' and key == Qt.Key_W:
            print(f'Нажали: {_key}')
            self.W.setStyleSheet("background-color: #ccc; color: red;")
            self.Ctrl.setStyleSheet("background-color: #ccc; color: red;")
            self.prev_key = [self.Ctrl, self.W]
            # ...
        elif _keys[0] == 'Alt' and key == Qt.Key_W:
            print(f'Нажали: {_key}')
            self.W.setStyleSheet("background-color: #ccc; color: red;")
            self.Alt.setStyleSheet("background-color: #ccc; color: red;")
            self.prev_key = [self.Alt, self.W]
            # ...
        elif _keys[0] == 'Shift' and key == Qt.Key_W:
            print(f'Нажали: {_key}')
            self.W.setStyleSheet("background-color: #ccc; color: red;")
            self.ShifL.setStyleSheet("background-color: #ccc; color: red;")
            self.prev_key = [self.ShifL, self.W]
            # ...

        elif key == Qt.Key_W:
            print('Нажали: w')
            self.W.setStyleSheet("background-color: #ccc; color: red;")
            self.prev_key = [self.W, ]
        elif key == Qt.Key_A:
            print('Нажали: a')
            self.A.setStyleSheet("background-color: #ccc; color: red;")
            self.prev_key = [self.A, ]
        elif key == Qt.Key_S:
            print('Нажали: s')
            self.S.setStyleSheet("background-color: #ccc; color: red;")
            self.prev_key = [self.S, ]
        elif key == Qt.Key_D:
            print('Нажали: d')
            self.D.setStyleSheet("background-color: #ccc; color: red;")
            self.prev_key = [self.D, ]
            # ...
        elif key == Qt.Key_Escape:
            print('Нажали: Escape')
            self.esc.setStyleSheet("background-color: #ccc; color: red;")
            self.prev_key = [self.esc, ]
        elif key == Qt.Key_Tab:
            print('Нажали: Tab')
            self.Tab.setStyleSheet("background-color: #ccc; color: red;")
            self.prev_key = [self.Tab, ]
        elif key == Qt.Key_Backspace:
            print('Нажали: Backspace')
            self.Backspace.setStyleSheet("background-color: #ccc; color: red;")
            self.prev_key = [self.Backspace, ]
        elif key == Qt.Key_Enter:  # Обычно находится на клавиатуре.
            print('Нажали: Enter')
            self.Enter.setStyleSheet("background-color: #ccc; color: red;")
            self.prev_key = [self.Enter, ]
        elif key == Qt.Key_Return:
            print('Нажали: Enter/Return')
            self.Enter.setStyleSheet("background-color: #ccc; color: red;")
            self.prev_key = [self.Enter, ]
        elif key == Qt.Key_QuoteLeft:
            print('Нажали: A_10/QuoteLeft(`)')
            self.A_10.setStyleSheet("background-color: #ccc; color: red;")
            self.prev_key = [self.A_10, ]
        elif key == Qt.Key_Delete:
            print('Нажали: Delete')
            self.dlt.setStyleSheet("background-color: #ccc; color: red;")
            self.prev_key = [self.dlt, ]
        elif key == Qt.Key_Shift:
            print('Нажали: Shift')
            self.ShifL.setStyleSheet("background-color: #ccc; color: red;")
            self.ShiftR.setStyleSheet("background-color: #ccc; color: red;")
            self.prev_key = [self.ShifL, self.ShiftR]
        elif key == Qt.Key_Control:  # В macOS это соответствует клавишам Command.
            print('Нажали: Ctrl')
            self.Ctrl.setStyleSheet("background-color: #ccc; color: red;")
            self.prev_key = [self.Ctrl, ]
        elif key == Qt.Key_Alt:
            print('Нажали: Alt')
            self.Alt.setStyleSheet("background-color: #ccc; color: red;")
            self.prev_key = [self.Alt, ]
        elif key == Qt.Key_Meta:
            print('Нажали: Windows ')
            self.Win.setStyleSheet("background-color: #ccc; color: red;")
            self.prev_key = [self.Win, ]

    def keyevent_to_string(self, event):
        sequence = []
        for modifier, text in modmap.items():
            if event.modifiers() & modifier:
                sequence.append(text)
        key = keymap.get(event.key(), event.text())
        if key not in sequence:
            sequence.append(key)
        return '+'.join(sequence), sequence


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = Example()
    w.show()
    sys.exit(app.exec_())