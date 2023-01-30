import os
import sys

import requests
from PyQt5.Qt import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QLabel

SCREEN_SIZE = [600, 450]


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


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.z = 17
        self.speed = 0.008
        self.coords_x = 37.530887
        self.coords_y = 55.703118
        self.prev_key = None
        self.map_type = 'map'
        self.getImage()
        self.initUI()

    def keyPressEvent(self, event):
        _key, _keys = self.keyevent_to_string(event)
        # раскомментируйте строку  ниже, чтобы увидеть что происходит
        print(f'------> {_key}, {event.text()}, {event.key()}, {_keys}')

        key = event.key()

        if self.prev_key:
            for k in self.prev_key:
                k.setStyleSheet("")
        if key == Qt.Key_PageUp:
            if self.z < 17:
                self.z += 1
        if key == Qt.Key_PageDown:
            if self.z > 0:
                self.z -= 1
        self.getImage()

        self.pixmap = QPixmap(self.map_file)
        self.image = QLabel(self)
        self.image.move(0, 0)
        self.image.resize(600, 450)
        self.image.setPixmap(self.pixmap)

    def keyevent_to_string(self, event):
        sequence = []
        for modifier, text in modmap.items():
            if event.modifiers() & modifier:
                sequence.append(text)
        key = keymap.get(event.key(), event.text())
        if key not in sequence:
            sequence.append(key)
        return '+'.join(sequence), sequence

    def getImage(self):
        map_request = f"http://static-maps.yandex.ru/1.x/?ll={self.coords_x},{self.coords_y}&z={self.z}&l=" \
                      f"{self.map_type}"
        response = requests.get(map_request)

        if not response:
            print("Ошибка выполнения запроса:")
            print(map_request)
            print("Http статус:", response.status_code, "(", response.reason, ")")
            sys.exit(1)

        # Запишем полученное изображение в файл.
        self.map_file = "map.png"
        with open(self.map_file, "wb+ ") as file:
            file.seek(0)
            file.write(response.content)

    def initUI(self):
        self.setGeometry(100, 100, *SCREEN_SIZE)
        self.setWindowTitle('Yandex.Maps API')

        # Изображение
        self.pixmap = QPixmap(self.map_file)
        self.image = QLabel(self)
        self.image.move(0, 0)
        self.image.resize(600, 450)
        self.image.setPixmap(self.pixmap)

    def closeEvent(self, event):
        """При закрытии формы подчищаем за собой"""
        os.remove(self.map_file)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
