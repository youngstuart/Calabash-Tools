import pymel.core as pm
# menuAction may change to be more specific, ex pipeman will be its own module
import menuActions, matlib_ui
reload(menuActions)
reload(matlib_ui)
def _null(*args):
    pass

class _shelf():
    '''A simple class to build shelves in maya. Since the build method is empty,
    it should be extended by the derived class to build the necessary shelf elements.
    '''

    def __init__(self, name="CalabashTools", iconPath=""):
        self.name = name

        self.iconPath = iconPath

        self.labelBackground = (0, 0, 0, 0)
        self.labelColour = (.9, .9, .9)

        self._cleanOldShelf()
        pm.setParent(self.name)
        self.build()

    def build(self):
        '''This method should be overwritten in derived classes to actually build the shelf
        elements. Otherwise, nothing is added to the shelf.'''
        pass

    def addButton(self, label, icon="commandButton.png", command=_null, doubleCommand=_null):
        '''Adds a shelf button with the specified label, command, double click command and image.'''
        pm.setParent(self.name)
        if icon:
            icon = self.iconPath + icon
        pm.shelfButton(width=37, height=37, image=icon, l=label, command=command, dcc=doubleCommand, imageOverlayLabel=label, olb=self.labelBackground, olc=self.labelColour)

    def addMenuItem(self, parent, label, command=_null, icon=""):
        '''Adds a shelf button with the specified label, command, double click command and image.'''
        if icon:
            icon = self.iconPath + icon
        return pm.menuItem(p=parent, l=label, c=command, i="")

    def addSubMenu(self, parent, label, icon=None):
        '''Adds a sub menu item with the specified label and icon to the specified parent popup menu.'''
        if icon:
            icon = self.iconPath + icon
        return pm.menuItem(p=parent, l=label, i=icon, subMenu=1)

    def _cleanOldShelf(self):
        '''Checks if the shelf exists and empties it if it does or creates it if it does not.'''
        if pm.shelfLayout(self.name, ex=1):
            if pm.shelfLayout(self.name, q=1, ca=1):
                for each in pm.shelfLayout(self.name, q=1, ca=1):
                    pm.deleteUI(each)
        else:
            pm.shelfLayout(self.name, p="ShelfLayout")

class cbtools_shelf(_shelf):
    def build(self):
        self.addButton(label='Pipeman', command=menuActions.pipeman)
        self.addButton(label='Publish', command=menuActions.publishAsset)
        self.addButton(label='VRToolbox', command=menuActions.vrayToolbox)
        self.addButton(label='MatLib', command=matlib_ui.showLib)

def makeMenu():
    main_window = pm.language.melGlobals['gMainWindow']

    menu_obj = 'cbToolsMenu'
    menu_label = 'Calabash Tools'

    if pm.menu(menu_obj, label=menu_label, exists=True, parent=main_window):
        pm.deleteUI(pm.menu(menu_obj, e=True, deleteAllItems=True))
    
    cbTools_menu = pm.menu(menu_obj, label=menu_label, parent=main_window, tearOff=True)
    pm.menuItem(label='Pipeman', command=menuActions.pipeman)
    pm.menuItem(label='Publish Asset', command=menuActions.publishAsset)
    pm.menuItem(label='VRay Toolbox', command= menuActions.vrayToolbox)
    pm.menuItem(label='MatLib', command=matlib_ui.showLib)

makeMenu()
cbtools_shelf()
