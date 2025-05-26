# Created by https://github.com/ernakkc 
# Instagram Messaging App

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

from time import sleep
from random import randint, choice
from datetime import datetime

from utils.log import log_general, log_account

from utils.accountConf import load_account_config, isHaveProxy
from utils.browser import Browser
from utils.targetData import isTargetDataExist, getTargetData, setTargetData

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Settings
        self.accounts = load_account_config("accounts.json")
        self.accountsSize = len(self.accounts)
        
        log_general("Uygulama başlatıldı.")
    
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
        self.messages.addWidget(QTextEdit())
        self.messages.addWidget(QLabel("Mesaj 2:"))
        self.messages.addWidget(QTextEdit())
        self.messages.addWidget(QLabel("Mesaj 3:"))
        self.messages.addWidget(QTextEdit())
        self.right_layout.addLayout(self.messages)
        
        self.randomButton = QCheckBox("Mesajları Rastgele Gönder \n(Seçilmezse 1. Mesaj Gönderilir)")
        self.randomButton.setStyleSheet("background-color: lightgreen; font-size: 15px; font-weight: bold; border-radius: 5px; ")
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
        self.hesapLogButton.clicked.connect(self.accLogDownload)
        self.logHesapLayout.addWidget(self.hesapLogButton)
        self.logHesapLayout.addStretch()
        
        self.right_layout.addLayout(self.logHesapLayout)
        
        self.right_layout.addWidget(QLabel("Genel Kayıtlar"))
        self.logGunlukButton = QPushButton("Günlük Kayıtları İndir")
        self.logGunlukButton.setStyleSheet("background-color: white; font-size: 15px; font-weight: bold; border-radius: 5px; padding: 5px; border: 1px solid black;")
        self.logGunlukButton.clicked.connect(self.log_gunluk_download)
        self.right_layout.addWidget(self.logGunlukButton)
        
        self.logGenelButton = QPushButton("Genel Kayıtları İndir")
        self.logGenelButton.setStyleSheet("background-color: white; font-size: 15px; font-weight: bold; border-radius: 5px; padding: 5px; border: 1px solid black;")
        self.logGenelButton.clicked.connect(self.log_genel_download)
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
        
        usernamesLabel = QLabel("Hedef Kullanıcı İsim(ler)i\nHer birini Enter ile ayırın\n Başında @ işareti olmasına gerek yoktur")
        usernamesLabel.setAlignment(Qt.AlignCenter)
        usernamesLabel.setStyleSheet("font-size: 15px; font-weight: bold;")
        self.runtime_layout.addWidget(usernamesLabel)
        self.usernamesTextEdit = QTextEdit()
        self.usernamesTextEdit.setStyleSheet("font-size: 10px; font-weight: bold; border-radius: 5px; padding: 5px; border: 1px solid black;")
        self.usernamesTextEdit.setFixedWidth(300)
        self.runtime_layout.addWidget(self.usernamesTextEdit)
        self.usernamesTextEdit.setPlaceholderText("Kullanıcı Adı Giriniz")
        self.usernamesTextEdit.setAlignment(Qt.AlignLeft)
                
        self.startButton = QPushButton("Başlat")
        self.startButton.setStyleSheet("background-color: lightgreen; font-size: 15px; font-weight: bold; border-radius: 5px; padding: 5px; border: 1px solid black;")
        self.startButton.clicked.connect(self.start)
        self.runtime_layout.addWidget(self.startButton)
        
        # Çalışma esnasında logları göstermek için bir alan
        self.logOutput = QTextEdit()
        self.logOutput.setReadOnly(True)
        self.logOutput.setStyleSheet("font-size: 10px; font-weight: bold; border-radius: 5px; padding: 5px; border: 1px solid black;")
        self.logOutput.setFixedHeight(200)
        self.runtime_layout.addWidget(self.logOutput)
        self.logOutput.setPlaceholderText("Başlattıktan sonra uygulamaya tıklamayın !")
        
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
                
    def accLogDownload(self):
        username = self.hesapLogCombo.currentText()
        if not username:
            QMessageBox.warning(self, "Uyarı", "Lütfen bir hesap seçin.")
            return
        # username to id
        account_id = None
        for account in self.accounts:
            if account["username"] == username:
                account_id = account["id"]
                break
        log_account(account_id, "Hesap log dosyası indiriliyor...")
        # nereye kaydedileceğini sor
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self, "Hesap Log Dosyasını Kaydet", f"account_{account_id}.log", "Log Files (*.log);;All Files (*)", options=options)
        if fileName:
            log_account(account_id, "Hesap log dosyası kaydediliyor...")
        if fileName:
            with open(fileName, "w", encoding="utf-8") as file:
                log_file_path = f"logs/account_{account_id}.log"
                try:
                    with open(log_file_path, "r", encoding="utf-8") as log_file:
                        file.write(log_file.read())
                except FileNotFoundError:
                    QMessageBox.warning(self, "Hata", "Hesap log dosyası bulunamadı.")
                    return
            log_account(account_id, f"Hesap log dosyası {fileName} olarak kaydedildi.")

    def log_gunluk_download(self):
        log_general("Günlük log dosyası indiriliyor...")
        today = datetime.now().strftime("%Y-%m-%d")
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self, "Günlük Log Dosyasını Kaydet", f"general_{today}.log", "Log Files (*.log);;All Files (*)", options=options)
        if fileName:
            with open(fileName, "w", encoding="utf-8") as file:
                log_file_path = f"logs/general.log"
                acclogs_file_path = [f"logs/account_{account['id']}.log" for account in self.accounts]
                try:
                    with open(log_file_path, "r", encoding="utf-8") as log_file:
                        log_file_content = log_file.readlines()
                        for line in log_file_content:
                            if line.startswith(today):
                                file.write(line)
                    for acclog_file in acclogs_file_path:
                        with open(acclog_file, "r", encoding="utf-8") as acclog_file:
                            acclog_file_content = acclog_file.readlines()
                            for line in acclog_file_content:
                                if line.startswith(today):
                                    file.write(line)
                except FileNotFoundError:
                    QMessageBox.warning(self, "Hata", "Günlük log dosyası bulunamadı.")
                    return
            log_general(f"Günlük log dosyası {fileName} olarak kaydedildi.")         

    def log_genel_download(self):
        log_general("Genel log dosyası indiriliyor...")
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self, "Genel Log Dosyasını Kaydet", "general.log", "Log Files (*.log);;All Files (*)", options=options)
        if fileName:
            with open(fileName, "w", encoding="utf-8") as file:
                log_file_path = f"logs/general.log"
                acclogs_file_path = [f"logs/account_{account['id']}.log" for account in self.accounts]
                try:
                    with open(log_file_path, "r", encoding="utf-8") as log_file:
                        file.write(log_file.read())
                    for acclog_file in acclogs_file_path:
                        with open(acclog_file, "r", encoding="utf-8") as acclog_file:
                            file.write(acclog_file.read())
                except FileNotFoundError:
                    QMessageBox.warning(self, "Hata", "Genel log dosyası bulunamadı.")
                    return
            log_general(f"Genel log dosyası {fileName} olarak kaydedildi.")

    def start(self):
        targetUsernames = self.usernamesTextEdit.toPlainText().strip().split("\n")
        targetUsernames = [username.strip() for username in targetUsernames if username.strip()]
        if not targetUsernames or len(targetUsernames) == 0:
            QMessageBox.warning(self, "Uyarı", "Lütfen hedef kullanıcı adlarını girin.")
            return
        
        # ------------------------------------ MESAJ / MESAJLAR ------------------------------------
        # -----------------------------------------------------------------------------------------------
        if self.randomButton.isChecked():
            QMessageBox.information(self, "Bilgi", "Mesajlar rastgele gönderilecek.")
            messages = []
            for i in range(self.messages.count()):
                widget = self.messages.itemAt(i).widget()
                if isinstance(widget, QTextEdit):
                    messages.append(widget.toPlainText())
            if not messages or len(messages) == 0:
                QMessageBox.warning(self, "Uyarı", "Lütfen en az bir mesaj girin.")
                return
            log_general(f"Rastgele mesajlar seçildi.")
        else:
            QMessageBox.information(self, "Bilgi", "1. mesaj gönderilecek.")
            messages = [self.messages.itemAt(1).widget().toPlainText().strip()]
            if not messages or len(messages) == 0:
                QMessageBox.warning(self, "Uyarı", "Lütfen en az bir mesaj girin.")
                return
            log_general(f"1. mesaj seçildi.") 
        log_general(f"Mesajlar: {', '.join(messages)}")
        
        selected_accounts = []
        for element in self.listItems:
            checkbox = element.itemAt(0).widget()
            if isinstance(checkbox, QCheckBox) and checkbox.isChecked():
                index = self.listItems.index(element)
                selected_accounts.append(self.accounts[index])
        if len(selected_accounts) == 0:
            QMessageBox.warning(self, "Uyarı", "Lütfen en az bir hesap seçin.")
            return
        
        print(messages)
        exit()
        # ------------------------------------ TEKLİ HESAP İŞLEMLERİ ------------------------------------
        # ----------------------------------------------------------------------------------------------- 
        if len(selected_accounts) == 1:
            QMessageBox.information(self, "Bilgi", "Tek bir hesap seçildi, bu hesapla işlem yapılacak.")
            accID = selected_accounts[0]["id"]
            log_account(accID, "Tek hesap ile işlem başlatılıyor.")
            log_account(accID, "Hesap bilgileri: " + str(selected_accounts[0]))
            log_account(accID, f"Hedef kullanıcı adları: {', '.join(targetUsernames)}")
            log_account(accID, f"Mesajlar: {', '.join(messages)}")
            log_account(accID, "İşlem başlatılıyor...")
            
            browser = Browser(selected_accounts[0]["proxy"], selected_accounts[0]["id"], selected_accounts[0]["username"], selected_accounts[0]["password"])
            browser.start()
            for targetUsername in targetUsernames:
                log_account(accID, f"{targetUsername} kullanıcısı ile işlem başlatılıyor.")
                if not isTargetDataExist(targetUsername):
                    setTargetData(targetUsername, {"isPrivate": False, "requested": False})
                if browser.isPrivateAccount(targetUsername):
                    log_account(accID, f"{targetUsername} hesabı özel, istek gönderiliyor...")
                    browser.sendRequest(targetUsername)
                else:
                    log_account(accID, f"{targetUsername} hesabı özel değil, mesaj gönderiliyor...")
                    mesaj = choice(messages)
                    browser.sendMessage(targetUsername, mesaj)
                sleep(randint(2,5))
                log_account(accID, f"Mesaj gönderildi. Hedef kullanıcı: {targetUsername}, Mesaj: {mesaj}")
            QMessageBox.information(self, "Bilgi", "İşlem tamamlandı.")
            return
        # ------------------------------------ ÇOKLU HESAP İŞLEMLERİ ------------------------------------
        # -----------------------------------------------------------------------------------------------
        else:
            QMessageBox.information(self, "Bilgi", f"{len(selected_accounts)} hesap seçildi, bu hesaplarla işlem yapılacak.")
            for account in selected_accounts:
                accID = account["id"]
                log_account(accID, "Çoklu hesap ile işlem başlatılıyor.")
                log_account(accID, "Hesap bilgileri: " + str(account))
                log_account(accID, f"Hedef kullanıcı adları: {', '.join(targetUsernames)}")
                log_account(accID, f"Mesajlar: {', '.join(messages)}")
                log_account(accID, "İşlem başlatılıyor...")
                browser = Browser(account["proxy"], account["id"], account["username"], account["password"])
                browser.start()
                # hesaplara usernameleri bölüştür
                for id, targetUsername in enumerate(targetUsernames):
                    if id % len(selected_accounts) == selected_accounts.index(account):
                        log_account(accID, f"{targetUsername} kullanıcısı ile işlem başlatılıyor.")
                        if not isTargetDataExist(targetUsername):
                            setTargetData(targetUsername, {"isPrivate": False, "requested": False})
                        if browser.isPrivateAccount(targetUsername):
                            log_account(accID, f"{targetUsername} hesabı özel, istek gönderiliyor...")
                            browser.sendRequest(targetUsername)
                        else:
                            log_account(accID, f"{targetUsername} hesabı özel değil, mesaj gönderiliyor...")
                            mesaj = choice(messages)
                            browser.sendMessage(targetUsername, mesaj)
                        sleep(randint(2,5))
                        log_account(accID, f"Mesaj gönderildi. Hedef kullanıcı: {targetUsername}, Mesaj: {mesaj}")
            QMessageBox.information(self, "Bilgi", "İşlem tamamlandı.")
            return
        
        
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())