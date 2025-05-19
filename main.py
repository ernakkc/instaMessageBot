# Created by https://github.com/ernakkc 
# Instagram Messaging App

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

from utils.accountConf import load_account_config, isHaveProxy

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Settings
        self.accounts = load_account_config("accounts.json")
        self.accountsSize = len(self.accounts)
        
    
        self.setWindowTitle("Instagram Messaging App")
        # self.windowIcon = QIcon("icon.png")
        # self.setGeometry(100, 100, 600, 400)

        # Create a central widget
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Create a layout for the central widget
        self.layout = QHBoxLayout()
        self.central_widget.setLayout(self.layout)
        
        # ------------------------------------------ Left Side Layout ------------------------------------------
        self.left_layout = QVBoxLayout()
        self.layout.addLayout(self.left_layout)
        
        self.acclist_label = QLabel("Account List")
        self.acclist_label.setAlignment(Qt.AlignCenter)
        self.acclist_label.setStyleSheet("font-size: 30px; font-weight: bold;")
        self.acclist_label.setFixedHeight(50)
        
        self.acclist = QVBoxLayout()
        self.acclist.setAlignment(Qt.AlignTop)
        self.acclist.setSpacing(10)
        self.acclist.setContentsMargins(0, 0, 0, 0)
        self.acclist.setSizeConstraint(QLayout.SetMinimumSize)
        
        self.listItems = []
        for account in self.accounts:
            accountItem = QHBoxLayout()
            accountItem.setAlignment(Qt.AlignTop)
            accountItem.setSpacing(10)
            accountItem.setContentsMargins(0, 0, 0, 0)
            accountItem.setSizeConstraint(QLayout.SetMinimumSize)
            accountItem.addWidget(QCheckBox(account["username"]))
            if isHaveProxy(account):
                accountItem.addWidget(QLabel("Proxy: " + account["proxy"]))
            else:
                accountItem.addWidget(QLabel("Proxy: None"))
            self.acclist.addLayout(accountItem)
            self.listItems.append(accountItem)
            
        self.acclist.addStretch()
        self.selectAllButton = QPushButton("Hepsini Seç")
        self.selectAllButton.setStyleSheet("background-color: lightblue; font-size: 15px; font-weight: bold;")
        self.selectAllButton.clicked.connect(self.selectAll)
        self.acclist.addWidget(self.selectAllButton)
        
        self.deselectAllButton = QPushButton("Hepsini Kaldır")
        self.deselectAllButton.setStyleSheet("background-color: lightcoral; font-size: 15px; font-weight: bold;")
        self.deselectAllButton.clicked.connect(self.deselectAll)
        self.acclist.addWidget(self.deselectAllButton)

        itemSec_Label = QLabel("Yukarıdan Kullanmak İstediğiniz Hesapları Seçin")
        itemSec_Label.setAlignment(Qt.AlignCenter)
        itemSec_Label.setStyleSheet("font-size: 20px; font-weight: bold;")
        itemSec_Label.setFixedHeight(50)
        itemSec_Label.setStyleSheet("QLabel { color: blue; }")
        
        self.left_layout.addWidget(self.acclist_label)
        self.left_layout.addLayout(self.acclist)
        self.left_layout.addWidget(itemSec_Label)
        
        # ------------------------------------------ Right Side Layout ------------------------------------------
        self.right_layout = QVBoxLayout()
        self.layout.addStretch()
        self.layout.addLayout(self.right_layout)
        
        self.right_layout.setAlignment(Qt.AlignTop)
        self.right_layout.setSpacing(10)
        
        # 3 mesaj girilebilecek alan
        self.messages_label = QLabel("Mesajlar")
        self.messages_label.setAlignment(Qt.AlignCenter)
        self.messages_label.setStyleSheet("font-size: 30px; font-weight: bold;")
        self.messages_label.setFixedHeight(50)
        self.right_layout.addWidget(self.messages_label)
        
        self.messages = QVBoxLayout()
        self.messages.setAlignment(Qt.AlignTop)
        self.messages.setSpacing(10)
        self.messages.setContentsMargins(0, 0, 0, 0)
        self.messages.setSizeConstraint(QLayout.SetMinimumSize)
        self.messages.addWidget(QLabel("Mesaj 1:"))
        self.messages.addWidget(QLineEdit())
        self.messages.addWidget(QLabel("Mesaj 2:"))
        self.messages.addWidget(QLineEdit())
        self.messages.addWidget(QLabel("Mesaj 3:"))
        self.messages.addWidget(QLineEdit())
        self.right_layout.addLayout(self.messages)
        
        self.randomButton = QCheckBox("Mesajları Rastgele Gönder \n(Seçilmezse 1. Mesaj Gönderilir)")
        self.randomButton.setStyleSheet("background-color: lightgreen; font-size: 15px; font-weight: bold; border-radius: 5px; ")
        self.randomButton.clicked.connect(self.on_button_click)
        self.right_layout.addWidget(self.randomButton)
        
        self.right_layout.addStretch()
        
        logIslem_Label = QLabel("Log İşlemleri")
        logIslem_Label.setAlignment(Qt.AlignCenter)
        logIslem_Label.setStyleSheet("font-size: 20px; font-weight: bold;")
        self.right_layout.addWidget(logIslem_Label)

        self.right_layout.addWidget(QLabel("Hesap Kayıtları"))
        self.logHesapLayout = QHBoxLayout()
        self.logHesapLayout.setAlignment(Qt.AlignTop)
        self.logHesapLayout.setSpacing(10)
        
        self.hesapLogCombo = QComboBox()
        self.hesapLogCombo.setStyleSheet("font-size: 15px; font-weight: bold;")
        for hesap in self.accounts:
            self.hesapLogCombo.addItem(hesap["username"])
        self.hesapLogCombo.setCurrentIndex(0)
        self.hesapLogCombo.setFixedHeight(20)
        self.hesapLogCombo.setFixedWidth(200)
        self.hesapLogCombo.setInsertPolicy(QComboBox.NoInsert)
        self.hesapLogCombo.setDuplicatesEnabled(False)
        self.logHesapLayout.addWidget(self.hesapLogCombo)
        
        self.hesapLogButton = QPushButton("İndir")
        self.hesapLogButton.setStyleSheet("background-color: white; font-size: 15px; font-weight: bold; border-radius: 5px; padding: 5px; border: 1px solid black;")
        self.hesapLogButton.clicked.connect(self.on_button_click)
        self.logHesapLayout.addWidget(self.hesapLogButton)
        self.logHesapLayout.addStretch()
        
        self.right_layout.addLayout(self.logHesapLayout)
        
        self.right_layout.addWidget(QLabel("Genel Kayıtlar"))
        self.logGunlukButton = QPushButton("Günlük Kayıtları İndir")
        self.logGunlukButton.setStyleSheet("background-color: white; font-size: 15px; font-weight: bold; border-radius: 5px; padding: 5px; border: 1px solid black;")
        self.logGunlukButton.clicked.connect(self.on_button_click)
        self.right_layout.addWidget(self.logGunlukButton)
        
        self.logGenelButton = QPushButton("Genel Kayıtları İndir")
        self.logGenelButton.setStyleSheet("background-color: white; font-size: 15px; font-weight: bold; border-radius: 5px; padding: 5px; border: 1px solid black;")
        self.logGenelButton.clicked.connect(self.on_button_click)
        self.right_layout.addWidget(self.logGenelButton)
        
        # ------------------------------------------ Runtime Layout ------------------------------------------
        self.runtime_layout = QVBoxLayout()
        self.runtime_layout.setAlignment(Qt.AlignTop)
        self.layout.addStretch()
        self.layout.addLayout(self.runtime_layout)
        
        Calisma_Label = QLabel("Çalışma İşlemleri")
        Calisma_Label.setAlignment(Qt.AlignCenter)
        Calisma_Label.setStyleSheet("font-size: 20px; font-weight: bold;")
        self.runtime_layout.addWidget(Calisma_Label)
        
        
    def selectAll(self):
        for element in self.listItems:
            checkbox = element.itemAt(0).widget()
            if isinstance(checkbox, QCheckBox):
                checkbox.setChecked(True)

    def deselectAll(self):
        for element in self.listItems:
            checkbox = element.itemAt(0).widget()
            if isinstance(checkbox, QCheckBox):
                checkbox.setChecked(False)

    def on_button_click(self):
        QMessageBox.information(self, "Button Clicked", "You clicked the button!")
        
        
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())