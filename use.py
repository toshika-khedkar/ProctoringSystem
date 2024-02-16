from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QTextEdit, QRadioButton, QButtonGroup, QDialog, QDialogButtonBox, QHBoxLayout
from PyQt5.QtCore import pyqtSignal

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

    def add_question(self):
        num_questions = int(self.num_questions_edit.text())
        self.max_questions += num_questions
        self.update_add_question_button()
        for i in range(len(self.questions), len(self.questions) + num_questions):
            question_dialog = AddQuestionDialog(self, i)
            question_dialog.question_accepted.connect(self.add_question_widget)
            question_dialog.exec_()

    def add_question_widget(self, question_id, question, options, correct_option):
        question_widget = QuestionWidget(question_id, question, options, correct_option)
        self.question_widgets_layout.addWidget(question_widget)
        self.questions.append((question_id, question, options, correct_option))
        self.update_add_question_button()

    def update_add_question_button(self):
        remaining_questions = self.max_questions - len(self.questions)
        self.add_question_button.setEnabled(remaining_questions > 0)
        if remaining_questions == 0:
            self.add_question_button.setText("All questions added")

class AddQuestionDialog(QDialog):
    question_accepted = pyqtSignal(int, str, list, int)

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

class QuestionWidget(QWidget):
    def __init__(self, question_id, question, options, correct_option):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel(f"Question ID: {question_id}"))
        layout.addWidget(QLabel(f"Question: {question}"))
        for i, option in enumerate(options):
            layout.addWidget(QLabel(f"{chr(65 + i)}. {option}"))
        layout.addWidget(QLabel(f"Correct Option: {chr(65 + correct_option)}"))

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = AddQuestionWindow()
    window.show()
    sys.exit(app.exec_())
