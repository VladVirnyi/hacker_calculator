import sys
import os
from PySide6.QtCore import QObject, Slot, Signal, Property
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine

class HackerCalculator(QObject): #changed from QWidget to QObject
    def __init__(self):
        super().__init__()
        self._result = "THE RESULT IS: ..."

    #signal to notify QML when the result changes
    resultChanged = Signal(str)

    #property to expose the result to QML
    @Property(str, notify=resultChanged)
    def result(self):
        return self._result

    @Slot(str, str, str)  # @Slot decorator to make this method callable from QML
    def calculate(self, n1, n2, op):
        try:
            num1 = float(n1)
            num2 = float(n2)
            
            if op == "+": res = num1 + num2
            elif op == "-": res = num1 - num2
            elif op == "*": res = num1 * num2
            elif op == "/": res = num1 / num2 if num2 != 0 else "Error"
            else: res = "Unknown OP"
            
            self._result = f"THE RESULT IS: {res}"
        except ValueError:
            self._result = "ERROR: ENTER NUMBERS"
        
        self.resultChanged.emit(self._result)
    
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



def main():
    app = QGuiApplication(sys.argv) # Does not work in Windows for now
    engine = QQmlApplicationEngine()

    calculator = HackerCalculator()

    engine.rootContext().setContextProperty("calculator", calculator)

    qml_file = os.path.join(os.path.dirname(__file__), "design.qml")
    engine.load(qml_file)

    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
