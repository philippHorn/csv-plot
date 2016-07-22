import files
import sys
import os

from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication, QLabel, \
       QVBoxLayout, QPushButton, QDateTimeEdit, QGridLayout
from PyQt5.QtCore import Qt, QDateTime
from PyQt5.QtGui import QPixmap


class MainWindow(QWidget):
    
    def __init__(self, parent=None):
        super().__init__(parent) 
        self.files = files.get_files()
        self.height = 300
        self.checkboxes = []
        self.col_selects = []
        self.initUI()
        
        
    def initUI(self):  
        self.layout = QVBoxLayout()
        pic = QLabel()
        pic.setPixmap(QPixmap(os.getcwd() + "/logo3.jpg"))
        self.layout.addWidget(pic)

        self.flash_msg = QLabel("")
        self.flash_msg.setStyleSheet("QLabel { color : red; }")
        self.layout.addWidget(self.flash_msg)
        self.flash_msg.hide()

        self.layout.addWidget(QLabel("Wähle Größen:"))

        for file in self.files:
            checkbox = QCheckBox()
            checkbox.setText(str(file))
            self.layout.addWidget(checkbox)
            self.checkboxes.append(checkbox)

            col_select = Col_select(file.columns)
            col_select.hide()
            self.col_selects.append(col_select)
            self.layout.addWidget(col_select)

            checkbox.stateChanged.connect(self.toggle_checkbox(col_select))

        self._set_date_time_edit()
        button = QPushButton("Weiter")
        button.clicked.connect(self.plot) 
        self.layout.addWidget(button)

        self.setGeometry(300, 300, 200, self.height)
        self.setLayout(self.layout) 
        self.setWindowTitle('Csv Plotter')
        self.show()

    def _set_date_time_edit(self):
        gridLayout = QGridLayout()
        self.start = QDateTimeEdit()
        self.end = QDateTimeEdit()
        gridLayout.addWidget(QLabel("Startzeit"), 0, 0)
        gridLayout.addWidget(self.start, 0, 1)
        gridLayout.addWidget(QLabel("Endzeit"), 1, 0)
        gridLayout.addWidget(self.end, 1, 1)
        self.layout.addLayout(gridLayout)

    def _check_submission(self, files_, columns):
        msg = ""
        for idx, col in enumerate(columns):
            if col == []:
                msg = ("Bitte eine Größe zu folgender Kategorie auswählen: {}"
                        .format(files_[idx].quantity))
        if len(set((file.unit for file in files_))) != 1:
                msg = "Die Ausgewählten Größen haben unterschiedliche Einheiten."
                       
        if msg:
            self.flash_msg.setText(msg)
            self.flash_msg.show()
            return False
        self.flash_msg.hide()
        return True

    def plot(self):

        files_and_columns = [(file, col_select) for file, checkbox, col_select 
                            in zip(self.files, self.checkboxes, self.col_selects) 
                            if checkbox.isChecked()]
        files_ = [file for file, col in files_and_columns]
        columns = [col.get_selected() for file, col in files_and_columns]

        if not self._check_submission(files_, columns):
            return

        files.plot_files(self.start.dateTime().toPyDateTime(),
              self.end.dateTime().toPyDateTime(), files_, columns)

    def set_start(self, py_datetime):
        qt_datetime = _datetime_to_Qdatetime(py_datetime)
        if self.start.dateTime() < qt_datetime:
             self.start.setDateTime(qt_datetime)

    def set_end(self, py_datetime):
        qt_datetime = _datetime_to_Qdatetime(py_datetime)
        default = QDateTime.fromString("2000-01-01 00:00:00,0" , "yyyy-MM-dd HH:mm:ss,z")
        if self.end.dateTime() > qt_datetime or self.end.dateTime() == default:
             self.end.setDateTime(qt_datetime)


    def toggle_checkbox(self, cb):
        def wrapped():
            cb.show() if cb.isHidden() else cb.hide()
            self.height += 100 if cb.isHidden() else - 100
            self.resize(200, self.height)
            file_ind = self.col_selects.index(cb)
            file = self.files[file_ind]
            self.set_start(file.start)
            self.set_end(file.end)
        return wrapped

def _datetime_to_Qdatetime(date):   
    return QDateTime.fromTime_t(date.timestamp())

class Col_select(QWidget):
    def __init__(self, columns, parent=None):
        super().__init__(parent) 
        self.columns = columns
        self.checkboxes = []
        self.initUI()

    def initUI(self):  
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(30, 0, 0, 0)
        for column in self.columns:
            checkbox = QCheckBox()
            checkbox.setText(column)
            self.layout.addWidget(checkbox)
            self.checkboxes.append(checkbox)
        self.setLayout(self.layout) 

    def get_selected(self):
        return [col for col, checkbox in zip(self.columns, self.checkboxes)
                if checkbox.isChecked()]
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())