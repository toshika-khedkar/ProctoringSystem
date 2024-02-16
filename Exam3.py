from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QTextEdit, QRadioButton, QButtonGroup, QDialog, QDialogButtonBox, QHBoxLayout
import sqlite3
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QTextEdit, QRadioButton, QButtonGroup, QDialog, QDialogButtonBox, QHBoxLayout

from classquestion import AddQuestionWindow  
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

from PySide6.QtCore import Signal
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

        # Connect the button click event to open AddQuestionWindow
        self.pushButton.clicked.connect(self.open_add_question_window)

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

    def open_add_question_window(self):
        self.add_question_window = AddQuestionWindow()
        self.add_question_window.show()
class AddQuestionWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add MCQ Questions")

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.num_questions_label = QLabel("Enter number of questions:", self)
        self.layout.addWidget(self.num_questions_label)

        self.num_questions_edit = QLineEdit(self)
        self.layout.addWidget(self.num_questions_edit)

        self.add_question_button = QPushButton("Add Question", self)
        self.add_question_button.clicked.connect(self.add_question)
        self.layout.addWidget(self.add_question_button)

        self.question_widgets_layout = QVBoxLayout()
        self.layout.addLayout(self.question_widgets_layout)

        self.questions = []
        self.max_questions = 0

        # Connect to the SQLite database
        self.conn = sqlite3.connect('questions.db')
        self.cursor = self.conn.cursor()

        # Create the Questions table if it doesn't exist
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Questions (
                                id INTEGER PRIMARY KEY,
                                question TEXT,
                                option_a TEXT,
                                option_b TEXT,
                                option_c TEXT,
                                option_d TEXT,
                                correct_option TEXT
                            )''')
        self.conn.commit()

    def add_question(self):
        num_questions = int(self.num_questions_edit.text())
        self.max_questions += num_questions
        self.update_add_question_button()
        for i in range(len(self.questions), len(self.questions) + num_questions):
            question_dialog = AddQuestionDialog(self, i)
            question_dialog.question_accepted.connect(self.add_question_to_database)
            question_dialog.exec_()

    def add_question_to_database(self, question_id, question, options, correct_option):
        # Insert the question and options into the database
        self.cursor.execute('''INSERT INTO Questions (question, option_a, option_b, option_c, option_d, correct_option)
                               VALUES (?, ?, ?, ?, ?, ?)''', (question, options[0], options[1], options[2], options[3], correct_option))
        self.conn.commit()

        # Update the UI to display the added question
        self.add_question_widget(question_id, question, options, correct_option)

    def update_add_question_button(self):
        remaining_questions = self.max_questions - len(self.questions)
        self.add_question_button.setEnabled(remaining_questions > 0)
        if remaining_questions == 0:
            self.add_question_button.setText("All questions added")

    def closeEvent(self, event):
        # Close the database connection when the window is closed
        self.conn.close()
        event.accept()

class AddQuestionDialog(QDialog):
    question_accepted = Signal(int, str, list, int)

    def __init__(self, parent=None, question_id=0):
        super().__init__(parent)
        self.setWindowTitle("Add Question")

        self.question_id = question_id

        self.layout = QVBoxLayout(self)

        self.question_label = QLabel("Enter Question:", self)
        self.layout.addWidget(self.question_label)

        self.question_textedit = QTextEdit(self)
        self.layout.addWidget(self.question_textedit)

        self.options_layout = QVBoxLayout()
        self.layout.addLayout(self.options_layout)

        self.option_group = QButtonGroup()
        self.correct_option = None

        for i in range(4):
            option_layout = QHBoxLayout()
            self.options_layout.addLayout(option_layout)

            option_textedit = QLineEdit(self)
            option_layout.addWidget(option_textedit)

            option_radio = QRadioButton(chr(65 + i), self)
            option_layout.addWidget(option_radio)

            self.option_group.addButton(option_radio, i)

        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)
        button_box.accepted.connect(self.accept_dialog)
        button_box.rejected.connect(self.reject)
        self.layout.addWidget(button_box)

    def accept_dialog(self):
        question = self.question_textedit.toPlainText()
        options = [option_layout.itemAt(0).widget().text() for option_layout in (self.options_layout.itemAt(i) for i in range(self.options_layout.count()))]
        self.correct_option = self.option_group.checkedId()
        self.question_accepted.emit(self.question_id, question, options, self.correct_option)
        self.accept()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = AddQuestionWindow()
    window.show()
    sys.exit(app.exec_())
