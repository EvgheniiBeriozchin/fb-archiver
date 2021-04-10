import sys, os
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication, QWidget, QListWidget, QListWidgetItem, QPushButton, QVBoxLayout, QHBoxLayout


class FileManagerWidget(QWidget):
    
    def __init__(self, parent=None):
        super(FileManagerWidget, self).__init__(parent)
        
        self.path = "./"
        self.path_counter = 0
        
        self.ids_list_widget = QListWidget()
        self.paths_list_widget = QListWidget()
        self.types_list_widget = QListWidget()
        self.select_button = QPushButton("Select")
        self.select_button.clicked.connect(self.select)
        
        last_column_layout = QVBoxLayout()
        last_column_layout.addWidget(self.types_list_widget, 4)
        last_column_layout.addWidget(self.select_button, 1)
        last_column_layout_wrapper = QWidget()
        last_column_layout_wrapper.setLayout(last_column_layout)
        
        content_layout = QHBoxLayout()
        content_layout.addWidget(self.ids_list_widget, 1)
        content_layout.addWidget(self.paths_list_widget, 3)
        content_layout.addWidget(last_column_layout_wrapper, 1)
        
        self.update_layout()
        self.setLayout(content_layout)
        
    def select(self):
        selected_items = self.paths_list_widget.selectedItems()
        if len(selected_items) != 1:
            return
        else:
            if selected_items[0].text() == "..":
                if self.path_counter == 0:
                    return
                self.path_counter -= 1
            else:
                self.path_counter += 1
             
            if self.path_counter == 0:
                self.path = "./"
            else:
                self.path += "/" + selected_items[0].text()
                
        self.update_layout()
            
        
    def update_layout(self):
        if not os.path.isdir(self.path):
            self.trigger_file_selected()
            
        self.clear_lists()
        
        file_list = os.listdir(self.path)
        file_list.append("..")
        for i, item in enumerate(file_list):
            self.create_item(str(i), item, "FD" if os.path.isdir(self.path + "/" + item) else "FL")
    
    def clear_lists(self):
        self.ids_list_widget.clear()
        self.paths_list_widget.clear()
        self.types_list_widget.clear()
        
    def create_item(self, item_id, item, item_type):
        self.ids_list_widget.addItem(self.create_widget_item(item_id))
        self.paths_list_widget.addItem(self.create_widget_item(item))
        self.types_list_widget.addItem(self.create_widget_item(item_type))
        
    def create_widget_item(self, text):
        item = QListWidgetItem()
        item.setText(text)
        item.setTextAlignment(Qt.AlignCenter)
        
        return item
        
    def trigger_file_selected(self):
        print("File selected")
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = FileManagerWidget()
    w.show()
    
    with open("style.qss", "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)
    
    sys.exit(app.exec_())    