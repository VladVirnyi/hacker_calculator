import sys
from PySide6.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget

class HackerCalculator(QWidget):
    def __init__(self):
        super().__init__()

        widget = QWidget()
        self.setWindowTitle("Hacker Calculator")

        self.text_layout = QVBoxLayout()

        self.setLayout(self.text_layout)

        #first number input
        self.num1_input = QLineEdit()
        self.num1_input.setPlaceholderText("ENTER Y0UR F1RST NUMB3R")

        #second number input
        self.num2_input = QLineEdit()
        self.num2_input.setPlaceholderText("ENTER YOUR SECOND NUMB3R")

        #operation input
        self.op_input = QLineEdit()
        self.op_input.setPlaceholderText("ENTER 0PER@T1ON (+, -, *, /)")

        #calculate button
        self.calc_button = QPushButton("RUN EXPLOIT (CALCULATE)")
        self.calc_button.clicked.connect(self.calculate_result)

        self.result_label = QLabel("THE RESULT IS: ...")

        self.text_layout.addWidget(self.num1_input)
        self.text_layout.addWidget(self.num2_input)
        self.text_layout.addWidget(self.op_input)
        self.text_layout.addWidget(self.calc_button)
        self.text_layout.addWidget(self.result_label)

    def calculate_result(self):
        try:
            n1 = float(self.num1_input.text())
            n2 = float(self.num2_input.text())
            op = self.op_input.text()

            if op == "+":
                res = n1 + n2
            elif op == "-":
                res = n1 - n2
            elif op == "*":
                res = n1 * n2
            elif op == "/":
                res = n1 / n2 if n2 != 0 else "Error (Div by 0)"
            else:
                res = "Unknown OP"

            self.result_label.setText(f"THE RESULT IS: {res}")
            
        except ValueError:
            self.result_label.setText("ERROR: PL3AS3 ENT3R NUMB3RS")



if __name__ == "__main__":
    app = QApplication([])

    widget = HackerCalculator()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())
