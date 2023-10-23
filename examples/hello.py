# hello.py

"""Simple Hello, World example with PyQt6."""

import sys

# 1. Import QApplication and all the required widgets
from PyQt6.QtWidgets import QApplication, QLabel, QWidget

# 2. Create an instance of QApplication
"""
Here you can pass sys.argv to the constructor of QApplication, if there
are any command-line arguments you wish to pass to the application.
"""
app = QApplication([])

# 3. Create an instance of your application's GUI
window = QWidget()
window.setWindowTitle("PyQt App")
window.setGeometry(100, 100, 280, 80)
helloMsg = QLabel("<h1>Hello, World! ❤️</h1>", parent=window)
helloMsg.move(60, 15)

"""
Note:
To avoid memory leaks, you should always make sure that any QWidget object
has a parent, with the sole exception of your top-level windows.
"""

# 4. Show your application's GUI
window.show()

# 5. Run your application's event loop
sys.exit(app.exec())
