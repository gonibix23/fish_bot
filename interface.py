from time import sleep
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from functools import partial
import core_functions as cf
import sys, psutil, datetime, pymongo

class Ui_MainWindow(object):

    usage = None

    def setupUi(self, MainWindow):

        self.sessions = []
        self.bait_file = "bait.jpg"

        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(692, 566)
        font = QFont()
        MainWindow.setFont(font)
        MainWindow.setCursor(QCursor(Qt.CrossCursor))
        MainWindow.setMouseTracking(False)
        MainWindow.setLocale(QLocale(QLocale.English, QLocale.UnitedKingdom))
        MainWindow.setIconSize(QSize(24, 24))
        MainWindow.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.inputs = QFrame(self.centralwidget)
        self.inputs.setObjectName(u"inputs")
        self.inputs.setFrameShape(QFrame.StyledPanel)
        self.inputs.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.inputs)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)

        self.fast_mode_checkbox = QCheckBox(self.inputs)
        self.fast_mode_checkbox.setObjectName(u"fast_mode_checkbox")

        self.horizontalLayout_2.addWidget(self.fast_mode_checkbox)

        self.bait_time_label = QLabel(self.inputs)
        self.bait_time_label.setObjectName(u"bait_time_label")

        self.horizontalLayout_2.addWidget(self.bait_time_label)

        self.bait_time_field = QLineEdit(self.inputs)
        self.bait_time_field.setObjectName(u"bait_time_field")

        self.horizontalLayout_2.addWidget(self.bait_time_field)

        self.bait_key_label = QLabel(self.inputs)
        self.bait_key_label.setObjectName(u"bait_key_label")

        self.horizontalLayout_2.addWidget(self.bait_key_label)

        self.bait_key_field = QLineEdit(self.inputs)
        self.bait_key_field.setObjectName(u"bait_key_field")

        self.horizontalLayout_2.addWidget(self.bait_key_field)

        self.fish_key_label = QLabel(self.inputs)
        self.fish_key_label.setObjectName(u"fish_key_label")

        self.horizontalLayout_2.addWidget(self.fish_key_label)

        self.fish_key_field = QLineEdit(self.inputs)
        self.fish_key_field.setObjectName(u"fish_key_field")

        self.horizontalLayout_2.addWidget(self.fish_key_field)

        self.bait_file_button = QPushButton(self.inputs)
        self.bait_file_button.setObjectName(u"bait_file_button")
        self.bait_file_button.clicked.connect(self.browse_file)

        self.horizontalLayout_2.addWidget(self.bait_file_button)

        self.verticalLayout_3.addWidget(self.inputs)

        self.computer_usage = QFrame(self.centralwidget)
        self.computer_usage.setObjectName(u"computer_usage")
        self.computer_usage.setFrameShape(QFrame.StyledPanel)
        self.computer_usage.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.computer_usage)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.cpu_usage_perc_label = QLabel(self.computer_usage)
        self.cpu_usage_perc_label.setObjectName(u"cpu_usage_perc_label")

        self.horizontalLayout_3.addWidget(self.cpu_usage_perc_label)

        self.cpu_usage_perc_num = QLabel(self.computer_usage)
        self.cpu_usage_perc_num.setObjectName(u"cpu_usage_perc_num")

        self.horizontalLayout_3.addWidget(self.cpu_usage_perc_num)

        self.ram_usage_perc_label = QLabel(self.computer_usage)
        self.ram_usage_perc_label.setObjectName(u"ram_usage_perc_label")

        self.horizontalLayout_3.addWidget(self.ram_usage_perc_label)

        self.ram_usage_perc_num = QLabel(self.computer_usage)
        self.ram_usage_perc_num.setObjectName(u"ram_usage_perc_num")

        self.horizontalLayout_3.addWidget(self.ram_usage_perc_num)

        self.ram_usage_gb_label = QLabel(self.computer_usage)
        self.ram_usage_gb_label.setObjectName(u"ram_usage_gb_label")

        self.horizontalLayout_3.addWidget(self.ram_usage_gb_label)

        self.ram_usage_gb_num = QLabel(self.computer_usage)
        self.ram_usage_gb_num.setObjectName(u"ram_usage_gb_num")

        self.horizontalLayout_3.addWidget(self.ram_usage_gb_num)

        self.hwid_label = QLabel(self.computer_usage)
        self.hwid_label.setObjectName(u"hwid_label")
        self.hwid_label.setTextInteractionFlags(Qt.TextSelectableByMouse)

        self.horizontalLayout_3.addWidget(self.hwid_label)

        Ui_MainWindow.usage = cf.thread_with_trace(target = self.update_usage)
        Ui_MainWindow.usage.start()

        self.verticalLayout_3.addWidget(self.computer_usage)

        self.bot_creator_frame = QFrame(self.centralwidget)
        self.bot_creator_frame.setObjectName(u"bot_creator_frame")
        self.bot_creator_frame.setFrameShape(QFrame.StyledPanel)
        self.bot_creator_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.bot_creator_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.bot_key_frame = QFrame(self.bot_creator_frame)
        self.bot_key_frame.setObjectName(u"bot_key_frame")
        self.bot_key_frame.setFrameShape(QFrame.StyledPanel)
        self.bot_key_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.bot_key_frame)
        self.horizontalLayout.setSpacing(8)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)

        self.show_key_button = QPushButton(self.bot_key_frame)
        self.show_key_button.setObjectName(u"show_key_button")
        self.show_key_button.clicked.connect(self.show_key)

        self.horizontalLayout.addWidget(self.show_key_button)

        self.bot_key_field = QLineEdit(self.bot_key_frame)
        self.bot_key_field.setObjectName(u"bot_key_field")
        self.bot_key_field.setEchoMode(QLineEdit.Password)

        self.horizontalLayout.addWidget(self.bot_key_field)


        self.boit_key_label = QLabel(self.bot_key_frame)
        self.boit_key_label.setObjectName(u"boit_key_label")

        self.horizontalLayout.addWidget(self.boit_key_label)

        self.bot_create_button = QPushButton(self.bot_key_frame)
        self.bot_create_button.setObjectName(u"bot_create_button")
        self.bot_create_button.clicked.connect(self.create_bot_session)

        self.horizontalLayout.addWidget(self.bot_create_button)


        self.verticalLayout_2.addWidget(self.bot_key_frame)

        self.bot_thread_list = QScrollArea(self.bot_creator_frame)
        self.bot_thread_list.setObjectName(u"bot_thread_list")
        self.bot_thread_list.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 670, 450))
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName(u"gridLayout")
        self.bot_thread_list.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.bot_thread_list)


        self.verticalLayout_3.addWidget(self.bot_creator_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Where is my fish!", None))
        self.fast_mode_checkbox.setText(QCoreApplication.translate("MainWindow", u"Fast Mode", None))
        self.bait_time_label.setText(QCoreApplication.translate("MainWindow", u"Time between bait", None))
        self.bait_time_field.setText(QCoreApplication.translate("MainWindow", u"300", None))
        self.bait_key_label.setText(QCoreApplication.translate("MainWindow", u"Bait Key", None))
        self.bait_key_field.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.fish_key_label.setText(QCoreApplication.translate("MainWindow", u"Fish Key", None))
        self.fish_key_field.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.bait_file_button.setText(QCoreApplication.translate("MainWindow", u"Bait File", None))
        self.cpu_usage_perc_label.setText(QCoreApplication.translate("MainWindow", u"CPU Usage(%)", None))
        self.cpu_usage_perc_num.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.ram_usage_perc_label.setText(QCoreApplication.translate("MainWindow", u"RAM Usage(%)", None))
        self.ram_usage_perc_num.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.ram_usage_gb_label.setText(QCoreApplication.translate("MainWindow", u"RAM Usage(GB)", None))
        self.ram_usage_gb_num.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.hwid_label.setText(QCoreApplication.translate("MainWindow", u"HWID: "+cf.GetUUID(), None))
        self.boit_key_label.setText(QCoreApplication.translate("MainWindow", u"Bot Key", None))
        self.show_key_button.setText(QCoreApplication.translate("MainWindow", u"Show Key", None))
        self.bot_create_button.setText(QCoreApplication.translate("MainWindow", u"Create New Bot Session", None))
    # retranslateUi

    @Slot()
    def create_bot_session(self):
        if self.check_connection():
            bot_session = QFrame(self.scrollAreaWidgetContents)
            bot_session.setObjectName(str(len(self.sessions)))
            bot_session.setFrameShape(QFrame.StyledPanel)
            bot_session.setFrameShadow(QFrame.Raised)
            horizontalLayout = QHBoxLayout(bot_session)
            horizontalLayout.setObjectName(u"bot_session_"+str(len(self.sessions))+"_horizontalLayout")
            horizontalLayout.setContentsMargins(0, -1, 0, 0)

            lineEdit = QLabel(bot_session)
            lineEdit.setObjectName(u"bot_session_"+str(len(self.sessions))+"_input")
            lineEdit.setText("Bot Session "+str(len(self.sessions))+" - "+str(datetime.datetime.now()))

            horizontalLayout.addWidget(lineEdit)

            closeSession = QPushButton(bot_session)
            closeSession.setObjectName(u"bot_session_"+str(len(self.sessions))+"_closeSession")
            closeSession.setText("Close Session")
            session_thread = cf.thread_with_trace(target = cf.fishing_setup, args = (self.bait_key_field.text(), self.fish_key_field.text(), self.bait_file, self.fast_mode_checkbox.isChecked()))
            session_thread.start()
            sessions_thread = session_thread.join()
            closeSession.clicked.connect(partial(self.close_session, bot_session))

            horizontalLayout.addWidget(closeSession)

            self.sessions.append([bot_session, sessions_thread])

            self.gridLayout.addWidget(bot_session, len(self.sessions), 0, 1, 1)

    @Slot()
    def close_session(self, bot_session):
        self.sessions[int(bot_session.objectName())][1][0].kill()
        self.sessions[int(bot_session.objectName())][1][1].kill()
        bot_session.deleteLater()
    
    def update_usage(self):
        while True:
            self.cpu_usage_perc_num.setText(str(psutil.cpu_percent(4)))
            self.ram_usage_perc_num.setText(str(psutil.virtual_memory()[2]))
            self.ram_usage_gb_num.setText(str(round(psutil.virtual_memory()[3]/1000000000, 2)))
            sleep(1)

    def browse_file(self):
        f_dialog = QFileDialog.getOpenFileName(QFileDialog(), "Select File", "C:/", "JPG Files (*.jpg *.jpge)")
        self.bait_file = f_dialog[0]

    def show_key(self):
        if self.bot_key_field.echoMode() == QLineEdit.Password:
            self.bot_key_field.setEchoMode(QLineEdit.Normal)
        else:
            self.bot_key_field.setEchoMode(QLineEdit.Password)

    def check_connection(self):
        try:
            log = pymongo.MongoClient("localhost:27017", username = "customer", password = "EWkpCLr!Ju!(ABqcexHCj@JHzY5mF68DQLtycH%wW%&Wz$r#PuT!XJbT@csawt9F", authSource="fish_bot", authMechanism='SCRAM-SHA-256').get_database("fish_bot").get_collection("keys").find({"key":str(self.bot_key_field.text())}).next()
            if log["HWID"] == cf.GetUUID():
                return True
            else:
                return False
        except:
            return False

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QMainWindow()
    ui_app = Ui_MainWindow()
    ui_app.setupUi(window)
    window.show()
    app.exec()
    Ui_MainWindow.usage.kill()
    sys.exit()