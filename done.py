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


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(320, 240)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Student = QPushButton(self.centralwidget)
        self.Student.setObjectName(u"Student")
        self.Student.setGeometry(QRect(50, 120, 75, 24))
        self.Examiner = QPushButton(self.centralwidget)
        self.Examiner.setObjectName(u"Examiner")
        self.Examiner.setGeometry(QRect(200, 120, 75, 24))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 25, 281, 41))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(28)
        font.setBold(True)
        self.label.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 320, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Student.setText(QCoreApplication.translate("MainWindow", u"Student", None))
        self.Examiner.setText(QCoreApplication.translate("MainWindow", u"Examiner", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"REGISTRATION", None))
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
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(270, 480, 75, 24))
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
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"START", None))
        self.plainTextEdit.setPlainText(QCoreApplication.translate("MainWindow", u"Instructions:\n"
"This is a Proctored test so please ensure your Webcam is working and turn on the camera before starting the assessment.\n"
"Note that we have enabled the AI proctoring features and any detection of the below activities can result in disqualification from further considerations in the hiring process", None))




class Ui_ExaminerWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(617, 566)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(140, 40, 351, 61))
        self.label.setStyleSheet(u"font: 700 9pt \"Arial\";\n"
"font: 24pt \"Segoe UI\";")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(50, 200, 49, 16))
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(110, 140, 221, 22))
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(110, 200, 221, 22))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 140, 49, 16))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(260, 350, 75, 24))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Register as Examiner", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Exam:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"START", None))
class StudentWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_StudentWindow()
        self.ui.setupUi(self)
class ExaminerWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ExaminerWindow()
        self.ui.setupUi(self)
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 320, 240)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.Student.clicked.connect(self.StudentWindow)
        self.ui.Examiner.clicked.connect(self.ExaminerWindow)

    def StudentWindow(self):
        self.Student_window = StudentWindow()
        self.Student_window.show()
        self.close()
    def ExaminerWindow(self):
        self.Examiner_window = ExaminerWindow()
        self.Examiner_window.show()
        self.close()

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
from PySide6.QtCore import QCoreApplication, QMetaObject
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QLabel, QLineEdit, QPlainTextEdit, QStatusBar, QTimeEdit

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
        self.label.setGeometry(QCoreApplication.translate("MainWindow", QRect(170, 40, 351, 61)))
        self.label.setStyleSheet(u"font: 700 9pt \"Arial\";\n"
"font: 24pt \"Segoe UI\";")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QCoreApplication.translate("MainWindow", QRect(40, 140, 49, 16)))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QCoreApplication.translate("MainWindow", QRect(40, 170, 49, 16)))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QCoreApplication.translate("MainWindow", QRect(270, 480, 75, 24)))
        self.timer = QTimeEdit(self.centralwidget)
        self.timer.setObjectName(u"timer")
        self.timer.setGeometry(QCoreApplication.translate("MainWindow", QRect(490, 20, 118, 22)))
        self.timer.setDateTime(QDateTime(QDate(1999, 12, 31), QTime(2, 0, 0)))
        self.timer.setMaximumTime(QTime(2, 0, 0))
        self.timer.setCurrentSectionIndex(0)
        self.timer.setTime(QTime(2, 0, 0))
        self.plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QCoreApplication.translate("MainWindow", QRect(50, 310, 511, 111)))
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QCoreApplication.translate("MainWindow", QRect(100, 140, 221, 22)))
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QCoreApplication.translate("MainWindow", QRect(100, 170, 221, 22)))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Register as student", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Roll no:", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"START", None))
        self.plainTextEdit.setPlainText(QCoreApplication.translate("MainWindow", u"Instructions:\n"
"This is a Proctored test so please ensure your Webcam is working and turn on the camera before starting the assessment.\n"
"Note that we have enabled the AI proctoring features and any detection of the below activities can result in disqualification from further considerations in the hiring process", None))

class StudentWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_StudentWindow()
        self.ui.setupUi(self)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 320, 240)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.Student.clicked.connect(self.StudentWindow)

    def StudentWindow(self):
        self.Student_window = StudentWindow()
        self.Student_window.show()
        self.close()

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
