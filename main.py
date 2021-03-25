import sys
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication, QWidget, QListWidget, QListWidgetItem, QLineEdit, QLabel, QPushButton, QVBoxLayout, QHBoxLayout

from statistics import count_from_path

_placeholder = "Potato"

class Widget(QWidget):
    
    def __init__(self, parent=None):
        super(Widget, self).__init__(parent)

        self.list1_widget = QListWidget()
        self.list1_items = []
        
        self.list2_widget = QListWidget()
        self.list2_items = []
        
        for i in range(10):
            item1 = QListWidgetItem()
            item1.setTextAlignment(Qt.AlignCenter)
            self.list1_items.append(item1)
            self.list1_widget.addItem(item1)
            
            item2 = QListWidgetItem()
            item2.setTextAlignment(Qt.AlignCenter)
            self.list2_items.append(item2)
            self.list2_widget.addItem(item2)

        self.edit = QLineEdit("Write the path here..")
        button = QPushButton("Enter")
        button.clicked.connect(self.accept_input)
        
        lists_layout = QHBoxLayout()
        lists_layout.addWidget(self.list1_widget, 1)
        lists_layout.addWidget(self.list2_widget, 1)
        lists_widget_wrapper = QWidget()
        lists_widget_wrapper.setLayout(lists_layout)
        
        content_layout = QVBoxLayout()
        content_layout.addWidget(self.edit)
        content_layout.addWidget(lists_widget_wrapper)
        content_layout.addWidget(button)
       
        self.setLayout(content_layout)

    def accept_input(self):
        self.set_list(count_from_path(self.edit.text()))
        
    def set_list(self, items):
        items1 = items[0]
        items2 = items[1]
        
        if len(items1) != 10 or len(items1) != 10:
            return
        
        for i in range(10):
            self.list1_items[i].setText(items1[i])
            self.list2_items[i].setText(items2[i])
        

if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    w = Widget()
    w.show()
    
    with open("style.qss", "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)
    # Run the main Qt loop
    sys.exit(app.exec_())