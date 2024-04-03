from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My app")

        button = QPushButton("Push me")

        self.setMinimumSize(100, 100)
        self.setMaximumSize(1000, 800)

        self.setCentralWidget(button)


app = QApplication([])

window = MainWindow()
window.show()

app.exec()
