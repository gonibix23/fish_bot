from time import sleep
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from functools import partial
import core_functions as cf
import sys

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        self.sessions = []
        MainWindow.resize(683, 607)
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
        self.bait_label = QLabel(self.inputs)
        self.bait_label.setObjectName(u"bait_label")

        self.horizontalLayout_2.addWidget(self.bait_label)

        self.bait_field = QLineEdit(self.inputs)
        self.bait_field.setObjectName(u"bait_field")

        self.horizontalLayout_2.addWidget(self.bait_field)


        self.verticalLayout_3.addWidget(self.inputs)

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
        self.horizontalLayout.setContentsMargins(0, -1, 0, 9)
        self.bot_key_field = QLineEdit(self.bot_key_frame)
        self.bot_key_field.setObjectName(u"bot_key_field")

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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 661, 505))
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
        self.bait_label.setText(QCoreApplication.translate("MainWindow", u"Time between bait", None))
        self.boit_key_label.setText(QCoreApplication.translate("MainWindow", u"Bot Key", None))
        self.bot_create_button.setText(QCoreApplication.translate("MainWindow", u"Create New Bot Session", None))
    # retranslateUi

    @Slot()
    def create_bot_session(self):
        if self.bot_key_field.text() == '1':
            bot_session = QFrame(self.scrollAreaWidgetContents)
            bot_session.setObjectName(u"bot_session_"+str(len(self.sessions)))
            bot_session.setFrameShape(QFrame.StyledPanel)
            bot_session.setFrameShadow(QFrame.Raised)

            horizontalLayout = QHBoxLayout(bot_session)
            horizontalLayout.setObjectName(u"bot_session_"+str(len(self.sessions))+"_horizontalLayout")
            horizontalLayout.setContentsMargins(0, -1, 0, 0)

            lineEdit = QLineEdit(bot_session)
            lineEdit.setObjectName(u"bot_session_"+str(len(self.sessions))+"_input")
            lineEdit.setText(self.bot_key_field.text())

            horizontalLayout.addWidget(lineEdit)

            showKey = QPushButton(bot_session)
            showKey.setObjectName(u"bot_session_"+str(len(self.sessions))+"_showKey")
            showKey.setText("Show Key")
            #showKey.clicked.connect(self.show_key)

            horizontalLayout.addWidget(showKey)

            closeSession = QPushButton(bot_session)
            closeSession.setObjectName(u"bot_session_"+str(len(self.sessions))+"_closeSession")
            closeSession.setText("Close Session")
            session_thread = cf.thread_with_trace(target = cf.fishing_setup)
            session_thread.start()
            sessions_thread = session_thread.join()
            closeSession.clicked.connect(partial(self.close_session, bot_session, sessions_thread))

            horizontalLayout.addWidget(closeSession)

            self.sessions.append(bot_session)

            self.gridLayout.addWidget(bot_session, len(self.sessions), 0, 1, 1)

    @Slot()
    def close_session(self, bot_session, session_thread):
        session_thread[0].kill()
        session_thread[1].kill()
        bot_session.deleteLater()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QMainWindow()
    ui_app = Ui_MainWindow()
    ui_app.setupUi(window)
    window.show()
    sys.exit(app.exec())