# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\young\Documents\maya\modules\calabash\scripts\pipeman\pipeman_ui.ui'
#
# Created: Sun Aug 11 12:27:37 2019
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_mainUI(object):
    def setupUi(self, mainUI):
        mainUI.setObjectName("mainUI")
        mainUI.resize(563, 532)
        self.gridLayout = QtWidgets.QGridLayout(mainUI)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_8 = QtWidgets.QLabel(mainUI)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_15.addWidget(self.label_8)
        self.comboBox_mayaproject = QtWidgets.QComboBox(mainUI)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_mayaproject.sizePolicy().hasHeightForWidth())
        self.comboBox_mayaproject.setSizePolicy(sizePolicy)
        self.comboBox_mayaproject.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.comboBox_mayaproject.setMaxVisibleItems(100)
        self.comboBox_mayaproject.setObjectName("comboBox_mayaproject")
        self.horizontalLayout_15.addWidget(self.comboBox_mayaproject)
        self.gridLayout.addLayout(self.horizontalLayout_15, 0, 0, 1, 1)
        self.tabWidget_pipeman = QtWidgets.QTabWidget(mainUI)
        self.tabWidget_pipeman.setObjectName("tabWidget_pipeman")
        self.pipeman_anim = QtWidgets.QWidget()
        self.pipeman_anim.setObjectName("pipeman_anim")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.pipeman_anim)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_3 = QtWidgets.QLabel(self.pipeman_anim)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_7.addWidget(self.label_3)
        self.verticalLayout_11.addLayout(self.horizontalLayout_7)
        self.treeWidget_shots = QtWidgets.QTreeWidget(self.pipeman_anim)
        self.treeWidget_shots.setObjectName("treeWidget_shots")
        self.treeWidget_shots.headerItem().setText(0, "1")
        self.treeWidget_shots.header().setVisible(False)
        self.verticalLayout_11.addWidget(self.treeWidget_shots)
        self.horizontalLayout_19.addLayout(self.verticalLayout_11)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_4 = QtWidgets.QLabel(self.pipeman_anim)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.label_4)
        self.verticalLayout_13.addLayout(self.horizontalLayout_6)
        self.treeWidget_animVersions = QtWidgets.QTreeWidget(self.pipeman_anim)
        self.treeWidget_animVersions.setMinimumSize(QtCore.QSize(0, 0))
        self.treeWidget_animVersions.setLineWidth(1)
        self.treeWidget_animVersions.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.treeWidget_animVersions.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.treeWidget_animVersions.setAlternatingRowColors(True)
        self.treeWidget_animVersions.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.treeWidget_animVersions.setIndentation(10)
        self.treeWidget_animVersions.setItemsExpandable(True)
        self.treeWidget_animVersions.setAnimated(True)
        self.treeWidget_animVersions.setWordWrap(True)
        self.treeWidget_animVersions.setExpandsOnDoubleClick(True)
        self.treeWidget_animVersions.setObjectName("treeWidget_animVersions")
        self.treeWidget_animVersions.header().setCascadingSectionResizes(True)
        self.treeWidget_animVersions.header().setDefaultSectionSize(0)
        self.treeWidget_animVersions.header().setHighlightSections(False)
        self.treeWidget_animVersions.header().setMinimumSectionSize(0)
        self.treeWidget_animVersions.header().setSortIndicatorShown(True)
        self.treeWidget_animVersions.header().setStretchLastSection(False)
        self.verticalLayout_13.addWidget(self.treeWidget_animVersions)
        self.horizontalLayout_19.addLayout(self.verticalLayout_13)
        self.verticalLayout_14.addLayout(self.horizontalLayout_19)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.anim_comments = QtWidgets.QTreeWidget(self.pipeman_anim)
        self.anim_comments.setAnimated(True)
        self.anim_comments.setWordWrap(True)
        self.anim_comments.setColumnCount(3)
        self.anim_comments.setObjectName("anim_comments")
        self.horizontalLayout_18.addWidget(self.anim_comments)
        self.verticalLayout_14.addLayout(self.horizontalLayout_18)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_anim_openlatest = QtWidgets.QPushButton(self.pipeman_anim)
        self.pushButton_anim_openlatest.setObjectName("pushButton_anim_openlatest")
        self.horizontalLayout_2.addWidget(self.pushButton_anim_openlatest)
        self.pushButton_anim_makelive = QtWidgets.QPushButton(self.pipeman_anim)
        self.pushButton_anim_makelive.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.pushButton_anim_makelive.setObjectName("pushButton_anim_makelive")
        self.horizontalLayout_2.addWidget(self.pushButton_anim_makelive)
        self.verticalLayout_14.addLayout(self.horizontalLayout_2)
        self.tabWidget_pipeman.addTab(self.pipeman_anim, "")
        self.pipeman_assets = QtWidgets.QWidget()
        self.pipeman_assets.setObjectName("pipeman_assets")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.pipeman_assets)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.pipeman_assets)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.treeWidget_assets = QtWidgets.QTreeWidget(self.pipeman_assets)
        self.treeWidget_assets.setMinimumSize(QtCore.QSize(0, 0))
        self.treeWidget_assets.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.treeWidget_assets.setAnimated(True)
        self.treeWidget_assets.setHeaderHidden(True)
        self.treeWidget_assets.setObjectName("treeWidget_assets")
        self.verticalLayout_3.addWidget(self.treeWidget_assets)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_2 = QtWidgets.QLabel(self.pipeman_assets)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_10.addWidget(self.label_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_10)
        self.treeWidget_versions = QtWidgets.QTreeWidget(self.pipeman_assets)
        self.treeWidget_versions.setMinimumSize(QtCore.QSize(0, 0))
        self.treeWidget_versions.setLineWidth(1)
        self.treeWidget_versions.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.treeWidget_versions.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.treeWidget_versions.setAlternatingRowColors(True)
        self.treeWidget_versions.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.treeWidget_versions.setIndentation(10)
        self.treeWidget_versions.setItemsExpandable(True)
        self.treeWidget_versions.setAnimated(True)
        self.treeWidget_versions.setWordWrap(True)
        self.treeWidget_versions.setExpandsOnDoubleClick(True)
        self.treeWidget_versions.setObjectName("treeWidget_versions")
        self.treeWidget_versions.header().setCascadingSectionResizes(True)
        self.treeWidget_versions.header().setDefaultSectionSize(0)
        self.treeWidget_versions.header().setHighlightSections(False)
        self.treeWidget_versions.header().setMinimumSectionSize(0)
        self.treeWidget_versions.header().setSortIndicatorShown(True)
        self.treeWidget_versions.header().setStretchLastSection(False)
        self.verticalLayout_4.addWidget(self.treeWidget_versions)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_15.addLayout(self.horizontalLayout)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.asset_comments = QtWidgets.QTreeWidget(self.pipeman_assets)
        self.asset_comments.setAnimated(True)
        self.asset_comments.setWordWrap(True)
        self.asset_comments.setColumnCount(3)
        self.asset_comments.setObjectName("asset_comments")
        self.horizontalLayout_12.addWidget(self.asset_comments)
        self.verticalLayout_15.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.pushButton_asset_openlatest = QtWidgets.QPushButton(self.pipeman_assets)
        self.pushButton_asset_openlatest.setObjectName("pushButton_asset_openlatest")
        self.horizontalLayout_21.addWidget(self.pushButton_asset_openlatest)
        self.pushButton_makelive = QtWidgets.QPushButton(self.pipeman_assets)
        self.pushButton_makelive.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.pushButton_makelive.setObjectName("pushButton_makelive")
        self.horizontalLayout_21.addWidget(self.pushButton_makelive)
        self.verticalLayout_15.addLayout(self.horizontalLayout_21)
        self.tabWidget_pipeman.addTab(self.pipeman_assets, "")
        self.arborist = QtWidgets.QWidget()
        self.arborist.setObjectName("arborist")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.arborist)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_7 = QtWidgets.QLabel(self.arborist)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_11.addWidget(self.label_7)
        self.lineEdit_arb_projPath = QtWidgets.QLineEdit(self.arborist)
        self.lineEdit_arb_projPath.setText("")
        self.lineEdit_arb_projPath.setPlaceholderText("")
        self.lineEdit_arb_projPath.setObjectName("lineEdit_arb_projPath")
        self.horizontalLayout_11.addWidget(self.lineEdit_arb_projPath)
        self.pushButton_arb_projBrowse = QtWidgets.QPushButton(self.arborist)
        self.pushButton_arb_projBrowse.setObjectName("pushButton_arb_projBrowse")
        self.horizontalLayout_11.addWidget(self.pushButton_arb_projBrowse)
        self.verticalLayout_2.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_5 = QtWidgets.QLabel(self.arborist)
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_13.addWidget(self.label_5)
        self.textEdit_arb_commands = QtWidgets.QTextEdit(self.arborist)
        self.textEdit_arb_commands.setObjectName("textEdit_arb_commands")
        self.horizontalLayout_13.addWidget(self.textEdit_arb_commands)
        self.pushButton_arb_exe = QtWidgets.QPushButton(self.arborist)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_arb_exe.sizePolicy().hasHeightForWidth())
        self.pushButton_arb_exe.setSizePolicy(sizePolicy)
        self.pushButton_arb_exe.setObjectName("pushButton_arb_exe")
        self.horizontalLayout_13.addWidget(self.pushButton_arb_exe)
        self.verticalLayout_2.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.textBrowser = QtWidgets.QTextBrowser(self.arborist)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setMinimumSize(QtCore.QSize(0, 160))
        self.textBrowser.setMaximumSize(QtCore.QSize(16777215, 125))
        self.textBrowser.setObjectName("textBrowser")
        self.horizontalLayout_14.addWidget(self.textBrowser)
        self.verticalLayout_2.addLayout(self.horizontalLayout_14)
        self.tabWidget_pipeman.addTab(self.arborist, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_16.addWidget(self.label_9)
        self.comboBox_gondo_compproject = QtWidgets.QComboBox(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_gondo_compproject.sizePolicy().hasHeightForWidth())
        self.comboBox_gondo_compproject.setSizePolicy(sizePolicy)
        self.comboBox_gondo_compproject.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.comboBox_gondo_compproject.setObjectName("comboBox_gondo_compproject")
        self.horizontalLayout_16.addWidget(self.comboBox_gondo_compproject)
        self.verticalLayout_5.addLayout(self.horizontalLayout_16)
        self.verticalLayout_10.addLayout(self.verticalLayout_5)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem)
        self.pushButton_gondo_setlinks = QtWidgets.QPushButton(self.tab)
        self.pushButton_gondo_setlinks.setObjectName("pushButton_gondo_setlinks")
        self.horizontalLayout_20.addWidget(self.pushButton_gondo_setlinks)
        self.verticalLayout_10.addLayout(self.horizontalLayout_20)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_10 = QtWidgets.QLabel(self.tab)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_6.addWidget(self.label_10)
        self.listWidget_gondo_shots = QtWidgets.QListWidget(self.tab)
        self.listWidget_gondo_shots.setObjectName("listWidget_gondo_shots")
        self.verticalLayout_6.addWidget(self.listWidget_gondo_shots)
        self.horizontalLayout_17.addLayout(self.verticalLayout_6)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_11 = QtWidgets.QLabel(self.tab)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_7.addWidget(self.label_11)
        self.listWidget_gondo_layers = QtWidgets.QListWidget(self.tab)
        self.listWidget_gondo_layers.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.listWidget_gondo_layers.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.listWidget_gondo_layers.setWordWrap(True)
        self.listWidget_gondo_layers.setSelectionRectVisible(True)
        self.listWidget_gondo_layers.setObjectName("listWidget_gondo_layers")
        self.verticalLayout_7.addWidget(self.listWidget_gondo_layers)
        self.horizontalLayout_17.addLayout(self.verticalLayout_7)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.treeWidget_gondo_versions = QtWidgets.QTreeWidget(self.tab)
        self.treeWidget_gondo_versions.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.treeWidget_gondo_versions.setObjectName("treeWidget_gondo_versions")
        self.verticalLayout_8.addWidget(self.treeWidget_gondo_versions)
        self.horizontalLayout_17.addLayout(self.verticalLayout_8)
        self.verticalLayout_10.addLayout(self.horizontalLayout_17)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_13 = QtWidgets.QLabel(self.tab)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_9.addWidget(self.label_13)
        self.listWidget_gondo_copylist = QtWidgets.QListWidget(self.tab)
        self.listWidget_gondo_copylist.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.listWidget_gondo_copylist.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked)
        self.listWidget_gondo_copylist.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.listWidget_gondo_copylist.setObjectName("listWidget_gondo_copylist")
        self.verticalLayout_9.addWidget(self.listWidget_gondo_copylist)
        self.pushButton_gondo_copy = QtWidgets.QPushButton(self.tab)
        self.pushButton_gondo_copy.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.pushButton_gondo_copy.setObjectName("pushButton_gondo_copy")
        self.verticalLayout_9.addWidget(self.pushButton_gondo_copy)
        self.verticalLayout_10.addLayout(self.verticalLayout_9)
        self.tabWidget_pipeman.addTab(self.tab, "")
        self.gridLayout.addWidget(self.tabWidget_pipeman, 1, 0, 1, 1)

        self.retranslateUi(mainUI)
        self.tabWidget_pipeman.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(mainUI)

    def retranslateUi(self, mainUI):
        mainUI.setWindowTitle(QtWidgets.QApplication.translate("mainUI", "Pipeman 2.0", None, -1))
        self.label_8.setText(QtWidgets.QApplication.translate("mainUI", "Maya Project:", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("mainUI", "Shot", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("mainUI", "Versions", None, -1))
        self.treeWidget_animVersions.setSortingEnabled(True)
        self.treeWidget_animVersions.headerItem().setText(0, QtWidgets.QApplication.translate("mainUI", "Version", None, -1))
        self.treeWidget_animVersions.headerItem().setText(1, QtWidgets.QApplication.translate("mainUI", "Status", None, -1))
        self.anim_comments.setSortingEnabled(True)
        self.anim_comments.headerItem().setText(0, QtWidgets.QApplication.translate("mainUI", "Version", None, -1))
        self.anim_comments.headerItem().setText(1, QtWidgets.QApplication.translate("mainUI", "Comment", None, -1))
        self.anim_comments.headerItem().setText(2, QtWidgets.QApplication.translate("mainUI", "Date", None, -1))
        self.pushButton_anim_openlatest.setText(QtWidgets.QApplication.translate("mainUI", "Open Latest", None, -1))
        self.pushButton_anim_makelive.setText(QtWidgets.QApplication.translate("mainUI", "Make Live", None, -1))
        self.tabWidget_pipeman.setTabText(self.tabWidget_pipeman.indexOf(self.pipeman_anim), QtWidgets.QApplication.translate("mainUI", "Animation", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("mainUI", "Assets", None, -1))
        self.treeWidget_assets.setSortingEnabled(True)
        self.treeWidget_assets.headerItem().setText(0, QtWidgets.QApplication.translate("mainUI", "Type", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("mainUI", "Versions", None, -1))
        self.treeWidget_versions.setSortingEnabled(True)
        self.treeWidget_versions.headerItem().setText(0, QtWidgets.QApplication.translate("mainUI", "Version", None, -1))
        self.treeWidget_versions.headerItem().setText(1, QtWidgets.QApplication.translate("mainUI", "Status", None, -1))
        self.asset_comments.setSortingEnabled(True)
        self.asset_comments.headerItem().setText(0, QtWidgets.QApplication.translate("mainUI", "Version", None, -1))
        self.asset_comments.headerItem().setText(1, QtWidgets.QApplication.translate("mainUI", "Comment", None, -1))
        self.asset_comments.headerItem().setText(2, QtWidgets.QApplication.translate("mainUI", "Date", None, -1))
        self.pushButton_asset_openlatest.setText(QtWidgets.QApplication.translate("mainUI", "Open Latest", None, -1))
        self.pushButton_makelive.setText(QtWidgets.QApplication.translate("mainUI", "Make Live", None, -1))
        self.tabWidget_pipeman.setTabText(self.tabWidget_pipeman.indexOf(self.pipeman_assets), QtWidgets.QApplication.translate("mainUI", "Assets", None, -1))
        self.label_7.setText(QtWidgets.QApplication.translate("mainUI", "Project Destination:", None, -1))
        self.pushButton_arb_projBrowse.setText(QtWidgets.QApplication.translate("mainUI", "Browse", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("mainUI", "Commands:", None, -1))
        self.pushButton_arb_exe.setText(QtWidgets.QApplication.translate("mainUI", "Execute", None, -1))
        self.textBrowser.setHtml(QtWidgets.QApplication.translate("mainUI", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Each line is a command.  Each line must begin with a project name.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Example:</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">Create a project \'Starkist\', a spot \'SK_BPouch_shots\' with 5 shots, a character asset \'Charlie\', and add a shot to spot \'\'Chicken_shots</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Starkist create project </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Starkist create spot SK_BPouch_shots 5</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Starkist create asset character Charlie</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Starkist create shot Chicken_shots/sh080</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None, -1))
        self.tabWidget_pipeman.setTabText(self.tabWidget_pipeman.indexOf(self.arborist), QtWidgets.QApplication.translate("mainUI", "Arborist", None, -1))
        self.label_9.setText(QtWidgets.QApplication.translate("mainUI", "Comp Input:", None, -1))
        self.pushButton_gondo_setlinks.setText(QtWidgets.QApplication.translate("mainUI", "View/Set Links", None, -1))
        self.label_10.setText(QtWidgets.QApplication.translate("mainUI", "Shots", None, -1))
        self.listWidget_gondo_shots.setSortingEnabled(True)
        self.label_11.setText(QtWidgets.QApplication.translate("mainUI", "Layers", None, -1))
        self.listWidget_gondo_layers.setSortingEnabled(True)
        self.treeWidget_gondo_versions.headerItem().setText(0, QtWidgets.QApplication.translate("mainUI", "Version", None, -1))
        self.treeWidget_gondo_versions.headerItem().setText(1, QtWidgets.QApplication.translate("mainUI", "Range", None, -1))
        self.label_13.setText(QtWidgets.QApplication.translate("mainUI", "Copy List", None, -1))
        self.pushButton_gondo_copy.setText(QtWidgets.QApplication.translate("mainUI", "Copy", None, -1))
        self.tabWidget_pipeman.setTabText(self.tabWidget_pipeman.indexOf(self.tab), QtWidgets.QApplication.translate("mainUI", "Gondolier", None, -1))
