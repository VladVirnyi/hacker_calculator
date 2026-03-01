import sys
from PySide6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QHBoxLayout, QWidget

class HackerCalculator(QWidget):
    def __init__(self):
        super().__init__()

        widget = QWidget()
        self.setWindowTitle("Hacker Calculator")

        layout = QVBoxLayout()

        self.setLayout(layout)
        self.resize(400, 300)

        self.show()



if __name__ == "__main__":
    app = QApplication([])

    widget = HackerCalculator()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())
