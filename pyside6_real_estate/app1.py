import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLineEdit, QPushButton
from PySide6.QtCore import Slot

class URLPrinterApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("URL Printer App")

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        self.url_line_edit = QLineEdit()
        layout.addWidget(self.url_line_edit)

        self.print_button = QPushButton("Print URL")
        self.print_button.clicked.connect(self.print_url)
        layout.addWidget(self.print_button)

        central_widget.setLayout(layout)

    @Slot()
    def print_url(self):
        url = self.url_line_edit.text()
        print("Entered URL:", url)

def main():
    app = QApplication(sys.argv)
    window = URLPrinterApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
