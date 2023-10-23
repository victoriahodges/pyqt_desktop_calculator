# dialog_example.py

"""Dialog-style application."""

import sys

from PyQt6.QtWidgets import (QApplication, QDialog, QDialogButtonBox,
                             QFormLayout, QLineEdit, QVBoxLayout)


class Window(QDialog):
    def __init__(self):
        # super() parent argument is set to None because this dialog
        # will be your main window.
        super().__init__(parent=None)
        self.setWindowTitle("QDialog")
        dialogLayout = QVBoxLayout()

        formLayout = QFormLayout()
        formLayout.addRow("Name:", QLineEdit())
        formLayout.addRow("Age:", QLineEdit())
        formLayout.addRow("Job:", QLineEdit())
        formLayout.addRow("Hobbies:", QLineEdit())

        dialogLayout.addLayout(formLayout)
        """
        Note that layout managers can be nested inside one another.
        You can nest layouts by calling .addLayout() on the container
        layout with the nested layout as an argument.
        """

        buttons = QDialogButtonBox()
        buttons.setStandardButtons(
            QDialogButtonBox.StandardButton.Cancel
            | QDialogButtonBox.StandardButton.Ok
        )
        dialogLayout.addWidget(buttons)

        self.setLayout(dialogLayout)


if __name__ == "__main__":
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())
