import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from rubberband import *

class example(QLabel):
    def __init__(self, parent=None):
        super().__init__()
        
        
        
        self.width_scale = 1920/1280
        self.height_scale = 1080/720
        
        self.pixmap = QPixmap('beachhouse.jpg')
        
        self.setScaledContents(True)
        
        #create painter instance with pixmap
        self.painterInstance = QPainter(self.pixmap)

        #set rectangle color and thickness
        self.penRectangle = QPen(Qt.red)
        
        
        #draw rectangle on painter
        self.painterInstance.setPen(self.penRectangle)
        self.painterInstance.drawRect(50,50,100,100)
        
        #set pixmap onto the label widget
        self.setPixmap(self.pixmap)
        
    def mousePressEvent(self, e):
        if(e.button() == Qt.LeftButton):
            print(self.geometry())
            self.origin = e.pos()
            self.press_x = e.pos().x()
            self.press_y = e.pos().y()

            self.rubberBand = my_band(QRubberBand.Rectangle, self)
            self.rubberBand.setGeometry(QRect(self.origin, QSize()))
            self.rubberBand.show()

            #self.palette = QPalette()
            #self.palette.setBrush(QPalette.Highlight, QBrush(Qt.red))
            #self.rubberBand.setPalette(self.palette)
            print(self.press_x, self.press_y)

    def mouseMoveEvent(self, e):
        if(e.buttons() == Qt.LeftButton):
            e.accept()
            self.rubberBand.setGeometry(QRect(self.origin, e.pos()).normalized())
            print(e.pos().x(), e.pos().y())    
        

    def mouseReleaseEvent(self, e):
        if(e.button() == Qt.LeftButton):
            self.release_x = e.pos().x()
            self.release_y = e.pos().y()
            print(self.release_x, self.release_y)
class my_band(QRubberBand):
    def __init__(self, shape, parent=None):
        super().__init__(shape, parent)
        self.initUI()
        
    def initUI(self):
        palette = QPalette()
        palette.setBrush(QPalette.Highlight, QBrush(Qt.red))
        self.setPalette(palette)
        
    
    def mousePressEvent(self, e):
        if e.button() == Qt.RightButton:
            print('hi')
           
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex  = example()
    ex.show()
    sys.exit(app.exec_())
