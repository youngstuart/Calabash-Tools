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
         
class matlib_ui(QtWidgets.QDialog):
    def __init__(self, parent=maya_main_window()):
        super(matlib_ui, self).__init__(parent)
        
        self.setWindowTitle("Material Library")
        self.setMinimumWidth(250)
        
        # Remove question mark
        self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)
        self.create_widgets()
        self.create_layout()
    
    def fixPath(path):
        return path.replace('\\','/')
    
    def getProjInfo():
        project = fixPath(pm.workspace.getPath())
        projInfo = {
        'project':project,
        'images':fixPath(os.path.join(project, 'images')),
        }
        return projInfo
    
    def getMaterials(self):
        projInfo = getProjInfo()
        mtlLib_path = fixPath(os.path.join(projInfo['images'], 'mtl_lib'))
        mtlLib = {'path':mtlLib_path,'materials':{}}
        materials = [(dir, os.path.join(mtlLib_path, dir)) for dir in os.listdir(mtlLib_path) if os.path.isdir(os.path.join(mtlLib_path, dir))]
        
        for material, path in materials:
            images = [img for img in os.listdir(path) if os.path.isfile(os.path.join(path, img))]
            mtlLib['materials'][material] = {'aovs':[]}
            for img in images:
                if len(img.split('.')) == 2:
                    mtlLib['materials'][material]['beauty'] = img
                else:
                    mtlLib['materials'][material]['aovs'].append(img)
        return mtlLib
    
    def make_thumbs(self, materials):
        thumbs = []
        for material in materials['materials']:
            img = os.path.join(materials['path'], material, materials['materials'][material]['beauty'])
            '''
            icon = QtGui.QIcon(img)
            self.btn = QtWidgets.QPushButton(material)
            self.btn.setIcon(icon)
            #self.btn.setIconSize(QtCore.QSize(200,200))
            self.btn.clicked.connect(lambda: self.printMe(img))
            thumbs.append(self.btn)
            '''
            
            image = QtGui.QImage(img)
            image = image.scaled(200,200)
            pixmap = QtGui.QPixmap()
            pixmap.convertFromImage(image)
            self.image_label = QtWidgets.QLabel(material)
            self.image_label.setPixmap(pixmap)
            thumbs.append(self.image_label)
            
            
        return thumbs
    def printMe(self, path):
        print(path)
    def create_widgets(self):
        self.navButton = QtWidgets.QPushButton("Navigation")

        self.previewButton = QtWidgets.QPushButton("Preview")
                
    def create_layout(self):
        projInfo = getProjInfo()
        mtlLib = os.walk(os.path.join(projInfo['images'], 'mtl_lib'))

        main_layout = QtWidgets.QHBoxLayout(self)
        
        gallery_layout = QtWidgets.QGridLayout()
        
        
        stupid_grid = [(0,0), (0,1), (1,0), (1,1)]
        thumbs = self.make_thumbs(self.getMaterials())

        for n in range(len(thumbs)):

            row, column = stupid_grid[n]
            gallery_layout.addWidget(thumbs[n], row, column)

        nav_layout = QtWidgets.QVBoxLayout()
        nav_layout.addWidget(self.navButton)
        

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
