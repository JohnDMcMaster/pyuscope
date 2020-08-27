#!/usr/bin/env python3

from uscope.gstwidget import GstVideoPipeline, gstwidget_main
from PyQt4.QtGui import QMainWindow, QHBoxLayout, QWidget


class TestGUI(QMainWindow):
    def __init__(self, source=None):
        QMainWindow.__init__(self)
        self.vidpip = GstVideoPipeline(source=source)
        self.initUI()
        self.vidpip.setupGst()
        self.vidpip.run()

    def initUI(self):
        self.setWindowTitle('pyv4l test')
        self.vidpip.setupWidgets()

        # ok
        # full widget only
        if 0:
            self.setCentralWidget(self.vidpip.full_widget)
        # bad
        # full widget only
        else:
            layout = QHBoxLayout()
            layout.addWidget(self.vidpip.full_widget)

            widget = QWidget()
            widget.setLayout(layout)
            self.setCentralWidget(widget)

        self.showMaximized()
        self.show()


if __name__ == '__main__':
    gstwidget_main(TestGUI)
