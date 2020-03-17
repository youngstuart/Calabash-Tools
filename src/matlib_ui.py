from PySide2 import QtCore
from PySide2 import QtWidgets
from PySide2 import QtGui
from shiboken2 import wrapInstance

import maya.OpenMayaUI as om

# https://gist.github.com/Boon-in-Oz/5134664a13cffb6f67075edfe2ff6f8a
# https://stackoverflow.com/questions/55820951/qt-flowlayout-example-how-to-get-sizehint-to-be-called-when-layout-changes/57214129#57214129

def maya_main_window():
    main_window_ptr = om.MQtUtil.mainWindow()
    return wrapInstance(long(main_window_ptr), QtWidgets.QWidget)


class FlowLayout(QtWidgets.QLayout):
    def __init__(self, parent=None, margin=0, spacing=-1):
        super(FlowLayout, self).__init__(parent)

        if parent is not None:
            self.setMargin(margin)

        self.setSpacing(spacing)

        self.itemList = []

    def __del__(self):
        item = self.takeAt(0)
        while item:
            item = self.takeAt(0)

    def addItem(self, item):
        self.itemList.append(item)

    def count(self):
        return len(self.itemList)

    def itemAt(self, index):
        if index >= 0 and index < len(self.itemList):
            return self.itemList[index]

        return None

    def takeAt(self, index):
        if index >= 0 and index < len(self.itemList):
            return self.itemList.pop(index)

        return None

    def expandingDirections(self):
        return QtCore.Qt.Orientations(QtCore.Qt.Orientation(0))

    def hasHeightForWidth(self):
        return True

    def heightForWidth(self, width):
        height = self.doLayout(QtCore.QRect(0, 0, width, 0), True)
        return height

    def setGeometry(self, rect):
        super(FlowLayout, self).setGeometry(rect)
        self.doLayout(rect, False)

    def sizeHint(self):
        return self.minimumSize()

    def minimumSize(self):
        size = QtCore.QSize()

        for item in self.itemList:
            size = size.expandedTo(item.minimumSize())

        size += QtCore.QSize(2 * self.contentsMargins().top(), 2 * self.contentsMargins().top())
        return size

    def doLayout(self, rect, testOnly):
        x = rect.x()
        y = rect.y()
        lineHeight = 0

        for item in self.itemList:
            wid = item.widget()
            spaceX = self.spacing() + wid.style().layoutSpacing(QtGui.QSizePolicy.PushButton, QtGui.QSizePolicy.PushButton, QtCore.Qt.Horizontal)
            spaceY = self.spacing() + wid.style().layoutSpacing(QtGui.QSizePolicy.PushButton, QtGui.QSizePolicy.PushButton, QtCore.Qt.Vertical)
            nextX = x + item.sizeHint().width() + spaceX
            if nextX - spaceX > rect.right() and lineHeight > 0:
                x = rect.x()
                y = y + lineHeight + spaceY
                nextX = x + item.sizeHint().width() + spaceX
                lineHeight = 0

            if not testOnly:
                item.setGeometry(QtCore.QRect(QtCore.QPoint(x, y), item.sizeHint()))

            x = nextX
            lineHeight = max(lineHeight, item.sizeHint().height())

        return y + lineHeight - rect.y()
              
class matlib_ui(QtWidgets.QDialog):
    def __init__(self, parent=maya_main_window()):
        super(matlib_ui, self).__init__(parent)
        
        self.setWindowTitle("Material Library")
        self.setMinimumWidth(250)
        
        # Remove question mark
        self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)
        self.create_widgets()
        self.create_layout()
        
            
    def create_widgets(self):
        self.navButton = QtWidgets.QPushButton("Navigation")
        self.previewButton = QtWidgets.QPushButton("Preview")
        
        
    def create_layout(self):
        main_layout = QtWidgets.QHBoxLayout(self)
        
        nav_layout = QtWidgets.QVBoxLayout()
        nav_layout.addWidget(self.navButton)
        

        gallery_layout = FlowLayout()

        gallery_layout.addWidget(QtWidgets.QPushButton(QtGui.QIcon("C:\Users\guest1\Desktop\scratch\cbtools2\Calabash-Tools\src\icons"), ''))
        main_layout.addLayout(gallery_layout)
        preview_layout = QtWidgets.QVBoxLayout()
        preview_layout.addWidget(self.previewButton)
        
        main_layout.addLayout(nav_layout)
        main_layout.addLayout(gallery_layout)
        main_layout.addLayout(preview_layout)
        
        
if __name__ == "__main__":
    
    try:
        matlib.close()
        matlib.deleteLater()
    except:
        pass
        
    matlib = matlib_ui()
    matlib.show()
