#!/usr/bin/env python3
"""
Demonstrates splitting the pipeline into:
-an image capture window
-saving .jpg or raw to disk
"""

from uscope.gstwidget import GstVideoPipeline, gstwidget_main, CbSink, Gst
from PyQt4.QtGui import QMainWindow


class TestGUI(QMainWindow):
    def __init__(self, source=None):
        QMainWindow.__init__(self)
        self.vidpip = GstVideoPipeline(source=source)
        self.initUI()
        # self.mysink = Gst.ElementFactory.make("mysink")
        # self.mysink = MySink()
        self.mysink = CbSink()
        self.vidpip.player.add(self.mysink)

        self.raw = 0
        if self.raw:
            totee = self.mysink
        else:
            print("Create jpegnec")
            self.jpegenc = Gst.ElementFactory.make("jpegenc")
            self.vidpip.player.add(self.jpegenc)
            totee = self.jpegenc

        def cb(buffer):
            print("got buffer, size %u" % len(buffer))
            if self.raw:
                open("raw.bin", "wb").write(buffer)
            else:
                open("raw.jpg", "wb").write(buffer)

        # Initialize this early so we can get control default values
        self.vidpip.setupGst(raw_tees=[totee])
        if not self.raw:
            print("raw add")
            assert self.jpegenc.link(self.mysink)

        self.mysink.cb = cb
        assert self.mysink
        self.vidpip.run()

    def initUI(self):
        self.setWindowTitle('Test')
        self.vidpip.setupWidgets()
        self.setCentralWidget(self.vidpip.full_widget)
        self.showMaximized()
        self.show()


if __name__ == '__main__':
    gstwidget_main(TestGUI)