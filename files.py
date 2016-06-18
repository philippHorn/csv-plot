import files
import sys
from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication, QLabel, \
       QVBoxLayout, QPushButton, QDateTimeEdit, QGridLayout
from PyQt5.QtCore import Qt, QDateTime


class MainWindow(QWidget):
    
    def __init__(self, parent=None):
        super().__init__(parent) 
        self.files = files.get_files()
        self.checkboxes = []
        self.col_selects = []
        self.initUI()
        
        
    def initUI(self):  
        self.layout = QVBoxLayout()

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


    def plot(self):
        files_and_columns = [(file, col_select) for file, checkbox, col_select 
                            in zip(self.files, self.checkboxes, self.col_selects) 
                            if checkbox.isChecked()]
        files_ = [file for file, col in files_and_columns]
        columns = [col.get_selected() for file, col in files_and_columns]

        files.plot_files(self.start.dateTime().toPyDateTime(),
              self.end.dateTime().toPyDateTime(), files_, columns)
        


    def toggle_checkbox(self, cb):
        def wrapped():
            cb.show() if cb.isHidden() else cb.hide()
            file_ind = self.col_selects.index(cb)
            file = self.files[file_ind]
            # self.start.setDateTimeRange (_datetime_to_Qdatetime(file.start), 
            #     _datetime_to_Qdatetime(file.end))
            # self.end.setDateTimeRange (_datetime_to_Qdatetime(file.start), 
            #     _datetime_to_Qdatetime(file.end))
            self.start.setDateTime(_datetime_to_Qdatetime(file.start))
            self.end.setDateTime(_datetime_to_Qdatetime(file.end))
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