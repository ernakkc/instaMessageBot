# Created by https://github.com/ernakkc 
# Instagram Messaging App

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Instagram Messaging App")
        # self.windowIcon = QIcon("icon.png")
        # self.setGeometry(100, 100, 600, 400)

        # Create a central widget
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Create a layout for the central widget
        self.layout = QHBoxLayout()
        self.central_widget.setLayout(self.layout)
        
        # Left Side Layout
        self.left_layout = QVBoxLayout()
        self.layout.addLayout(self.left_layout)
        
        acclist_label = QLabel("Account List")
        acclist_label.setAlignment(Qt.AlignCenter)
        acclist_label.setStyleSheet("font-size: 30px; font-weight: bold;")
        acclist_label.setFixedHeight(50)
        
        self.acclist = QVBoxLayout()
        self.acclist.setAlignment(Qt.AlignTop)
        self.acclist.setSpacing(10)
        self.acclist.setContentsMargins(0, 0, 0, 0)
        self.acclist.setSizeConstraint(QLayout.SetMinimumSize)
        self.acclist.addWidget(QLabel("Account 1"))
        self.acclist.addWidget(QLabel("Account 2"))
        self.acclist.addWidget(QLabel("Account 3"))


        itemSec_Label = QLabel("Yukarıdan Kullanmak İstediğiniz Hesapları Seçin")
        itemSec_Label.setAlignment(Qt.AlignCenter)
        itemSec_Label.setStyleSheet("font-size: 20px; font-weight: bold;")
        itemSec_Label.setFixedHeight(50)
        itemSec_Label.setStyleSheet("QLabel { color: blue; }")
        
        self.left_layout.addWidget(acclist_label)
        self.left_layout.addStretch()
        self.left_layout.addLayout(self.acclist)
        self.left_layout.addStretch()
        self.left_layout.addWidget(itemSec_Label)
        
        # Right Side Layout
        self.right_layout = QVBoxLayout()
        self.layout.addLayout(self.right_layout)
        
        

    def on_button_click(self):
        QMessageBox.information(self, "Button Clicked", "You clicked the button!")
        
        
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())