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
    QPlainTextEdit, QPushButton, QSizePolicy, QStatusBar, QMessageBox,
    QTimeEdit, QWidget,QMenuBar)
import audio
import head_pose
import detection
import threading as th
from Exam2 import Ui_ExaminerWindow, AddQuestionWindow
from classStd import Ui_StudentWindow
from classmain import Ui_MainWindow
from classquestion import AddQuestionWindow
from run import runing
import sqlite3
class StudentWindow(QMainWindow, Ui_StudentWindow):
    def __init__(self):
        super(StudentWindow, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.register_student)
        self.examinerLoginButton.clicked.connect(self.examiner_login)
        self.pushButton2.clicked.connect(self.runing)
        
    def register_student(self):
        name = self.lineEdit.text()
        roll_no = self.lineEdit_2.text()
        # Save student details to database
        self.save_to_database(name, roll_no)
        
    def save_to_database(self, name, roll_no):
        # Connect to database
        conn = sqlite3.connect('students.db')
        c = conn.cursor()
        # Create table if not exists
        c.execute('''CREATE TABLE IF NOT EXISTS students (name TEXT, roll_no TEXT)''')
        # Insert data into table
        c.execute("INSERT INTO students (name, roll_no) VALUES (?, ?)", (name, roll_no))
        # Commit changes and close connection
        conn.commit()
        conn.close()
        print("Student registered successfully!")

    def examiner_login(self):
        # Connect to database
        conn = sqlite3.connect('students.db')
        c = conn.cursor()
        # Retrieve student details from the database
        c.execute("SELECT name, roll_no FROM students WHERE name = ? AND roll_no = ?", (self.lineEdit.text(), self.lineEdit_2.text()))
        result = c.fetchone()
        # Check if credentials are valid
        if result:
            QMessageBox.information(self, "Login", "Student login successful")
        else:
            QMessageBox.warning(self, "Login", "Invalid name or roll no")
        # Close connection
        conn.close()
    def runing():
        head_pose_thread = th.Thread(target=head_pose.pose)
        audio_thread = th.Thread(target=audio.sound)
        detection_thread = th.Thread(target=detection.run_detection)

        head_pose_thread.start()
        audio_thread.start()
        detection_thread.start()

        head_pose_thread.join()
        audio_thread.join()
        detection_thread.join()
class ExaminerWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ExaminerWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Examiner Window")
        self.initialize_database()
        self.ui.pushButton_2.clicked.connect(self.register_examiner)
        self.ui.pushButton.clicked.connect(self.login)
        self.ui.pushButton_3.clicked.connect(self.open_add_question_window)
    def open_add_question_window(self):
        self.add_question_window = AddQuestionWindow()
        self.add_question_window.show()
    def initialize_database(self):
        conn = sqlite3.connect("examiner.db")
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS examiners (
            id INTEGER PRIMARY KEY,
            username TEXT UNIQUE,
            password TEXT
        )
        """)
        conn.commit()
        conn.close()

    def register_examiner(self):
        username = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()
        conn = sqlite3.connect("examiner.db")
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO examiners (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
            self.ui.statusbar.showMessage("Examiner registered successfully.")
        except sqlite3.IntegrityError:
            self.ui.statusbar.showMessage("Username already exists. Please choose another username.")
        conn.close()

    def login(self):
        username = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()
        conn = sqlite3.connect("examiner.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM examiners WHERE username = ? AND password = ?", (username, password))
        examiner = cursor.fetchone()
        conn.close()
        if examiner:
            self.ui.statusbar.showMessage("Login successful.")
        else:
            self.ui.statusbar.showMessage("Invalid username or password.")

        
class AddQuestionWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = AddQuestionWindow()
        self.ui.setupUi(self)
        

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 320, 240)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.Student.clicked.connect(self.StudentWindow)
        self.ui.Examiner.clicked.connect(self.ExaminerWindow)
        # self.ui.pushButton.clicked.connect(self.open_add_question_window)

    def StudentWindow(self):
        self.Student_window = StudentWindow()
        self.Student_window.show()
        self.close()
    def ExaminerWindow(self):
        self.Examiner_window = ExaminerWindow()
        self.Examiner_window.show()
        self.close()
    def questions(self):
        self.Question_window = QuestionWindow()
        self.Question_window.show()
        self.close() 

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())


    

class StudentWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_StudentWindow()
        self.ui.setupUi(self)
class QuestionWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = AddQuestionWindow()
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
        
    def questions(self):
        self.Question_window = QuestionWindow()
        self.Question_window.show()
        self.close()  

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
