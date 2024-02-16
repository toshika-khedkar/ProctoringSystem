from PySide6.QtCore import QCoreApplication, QMetaObject
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QLabel, QLineEdit, QPlainTextEdit, QStatusBar, QTimeEdit
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPlainTextEdit, QPushButton, QSizePolicy, QStatusBar,
    QTimeEdit, QWidget,QMenuBar)




class Ui_StudentWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(616, 566)
        MainWindow.setStyleSheet(u"background-color: rgb(236, 236, 236);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(170, 40, 351, 61))  # Corrected geometry setting
        self.label.setStyleSheet(u"font: 700 9pt \"Arial\";\n"
"font: 24pt \"Segoe UI\";")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 140, 49, 16))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 170, 49, 16))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"Register")
        self.pushButton.setGeometry(QRect(270, 480, 75, 24))
        self.pushButton2 = QPushButton(self.centralwidget)
        self.pushButton2.setObjectName(u"Start")
        self.pushButton2.setGeometry(QRect(370, 500, 75, 24))
        self.pushButton2.clicked
        self.timer = QTimeEdit(self.centralwidget)
        self.timer.setObjectName(u"timer")
        self.timer.setGeometry(QRect(490, 20, 118, 22))
        self.timer.setDateTime(QDateTime(QDate(1999, 12, 31), QTime(2, 0, 0)))
        self.timer.setMaximumTime(QTime(2, 0, 0))
        self.timer.setCurrentSectionIndex(0)
        self.timer.setTime(QTime(2, 0, 0))
        self.plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(50, 310, 511, 111))
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(100, 140, 221, 22))
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(100, 170, 221, 22))
        
        # Add button for examiner login
        self.examinerLoginButton = QPushButton(self.centralwidget)
        self.examinerLoginButton.setObjectName(u"studentLoginButton")
        self.examinerLoginButton.setGeometry(QRect(400, 480, 150, 24))
        self.examinerLoginButton.setText("Student Login")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Register as student", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Roll no:", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"REGISTER", None))
        self.pushButton2.setText(QCoreApplication.translate("MainWindow", u"Start Test", None))
        self.plainTextEdit.setPlainText(QCoreApplication.translate("MainWindow", u"Instructions:\n"
"This is a Proctored test so please ensure your Webcam is working and turn on the camera before starting the assessment.\n"
"Note that we have enabled the AI proctoring features and any detection of the below activities can result in disqualification from further considerations in the hiring process", None))
        self.examinerLoginButton.setText(QCoreApplication.translate("MainWindow", u"Student Login", None))