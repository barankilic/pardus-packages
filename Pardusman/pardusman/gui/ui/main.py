#!/usr/bin/env python
# coding=UTF-8
#
# Generated by pykdeuic4 from gui/ui/main.ui on Mon Oct 22 15:18:27 2012
#
# WARNING! All changes to this file will be lost.
from PyKDE4 import kdecore
from PyKDE4 import kdeui
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(619, 702)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/raw/pics/pardusman.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_5 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.frame = QtGui.QFrame(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout_2 = QtGui.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.frame)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineTitle = QtGui.QLineEdit(self.frame)
        self.lineTitle.setObjectName(_fromUtf8("lineTitle"))
        self.gridLayout.addWidget(self.lineTitle, 0, 2, 1, 2)
        self.label_5 = QtGui.QLabel(self.frame)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.lineParameters = QtGui.QLineEdit(self.frame)
        self.lineParameters.setObjectName(_fromUtf8("lineParameters"))
        self.gridLayout.addWidget(self.lineParameters, 1, 2, 1, 2)
        self.label_3 = QtGui.QLabel(self.frame)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.lineRepository = QtGui.QLineEdit(self.frame)
        self.lineRepository.setObjectName(_fromUtf8("lineRepository"))
        self.gridLayout.addWidget(self.lineRepository, 2, 2, 1, 1)
        self.pushBrowseRepository = QtGui.QPushButton(self.frame)
        self.pushBrowseRepository.setObjectName(_fromUtf8("pushBrowseRepository"))
        self.gridLayout.addWidget(self.pushBrowseRepository, 2, 3, 1, 1)
        self.label_4 = QtGui.QLabel(self.frame)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.lineReleaseFiles = QtGui.QLineEdit(self.frame)
        self.lineReleaseFiles.setObjectName(_fromUtf8("lineReleaseFiles"))
        self.gridLayout.addWidget(self.lineReleaseFiles, 3, 2, 1, 1)
        self.pushBrowseReleaseFiles = QtGui.QPushButton(self.frame)
        self.pushBrowseReleaseFiles.setObjectName(_fromUtf8("pushBrowseReleaseFiles"))
        self.gridLayout.addWidget(self.pushBrowseReleaseFiles, 3, 3, 1, 1)
        self.label_6 = QtGui.QLabel(self.frame)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)
        self.linePluginPackage = QtGui.QLineEdit(self.frame)
        self.linePluginPackage.setObjectName(_fromUtf8("linePluginPackage"))
        self.gridLayout.addWidget(self.linePluginPackage, 4, 2, 1, 1)
        self.pushBrowsePluginPackage = QtGui.QPushButton(self.frame)
        self.pushBrowsePluginPackage.setObjectName(_fromUtf8("pushBrowsePluginPackage"))
        self.gridLayout.addWidget(self.pushBrowsePluginPackage, 4, 3, 1, 1)
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 5, 0, 1, 1)
        self.lineWorkFolder = QtGui.QLineEdit(self.frame)
        self.lineWorkFolder.setObjectName(_fromUtf8("lineWorkFolder"))
        self.gridLayout.addWidget(self.lineWorkFolder, 5, 2, 1, 1)
        self.pushBrowseWorkFolder = QtGui.QPushButton(self.frame)
        self.pushBrowseWorkFolder.setObjectName(_fromUtf8("pushBrowseWorkFolder"))
        self.gridLayout.addWidget(self.pushBrowseWorkFolder, 5, 3, 1, 1)
        self.label_7 = QtGui.QLabel(self.frame)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)
        self.comboType = QtGui.QComboBox(self.frame)
        self.comboType.setObjectName(_fromUtf8("comboType"))
        self.comboType.addItem(_fromUtf8(""))
        self.comboType.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboType, 6, 2, 1, 1)
        self.comboCompression = QtGui.QComboBox(self.frame)
        self.comboCompression.setObjectName(_fromUtf8("comboCompression"))
        self.comboCompression.addItem(_fromUtf8(""))
        self.comboCompression.addItem(_fromUtf8(""))
        self.comboCompression.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboCompression, 6, 3, 1, 1)
        self.checkCollection = QtGui.QCheckBox(self.frame)
        self.checkCollection.setObjectName(_fromUtf8("checkCollection"))
        self.gridLayout.addWidget(self.checkCollection, 7, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.frame, 0, 0, 1, 1)
        self.collectionFrame = QtGui.QFrame(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.collectionFrame.sizePolicy().hasHeightForWidth())
        self.collectionFrame.setSizePolicy(sizePolicy)
        self.collectionFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.collectionFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.collectionFrame.setObjectName(_fromUtf8("collectionFrame"))
        self.gridLayout_4 = QtGui.QGridLayout(self.collectionFrame)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.listPackageCollection = QtGui.QListWidget(self.collectionFrame)
        self.listPackageCollection.setObjectName(_fromUtf8("listPackageCollection"))
        self.gridLayout_3.addWidget(self.listPackageCollection, 1, 0, 4, 1)
        self.pushModifyCollection = QtGui.QPushButton(self.collectionFrame)
        self.pushModifyCollection.setObjectName(_fromUtf8("pushModifyCollection"))
        self.gridLayout_3.addWidget(self.pushModifyCollection, 2, 1, 1, 1)
        self.label_9 = QtGui.QLabel(self.collectionFrame)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout_3.addWidget(self.label_9, 0, 0, 1, 1)
        self.pushSetDefaultCollection = QtGui.QPushButton(self.collectionFrame)
        self.pushSetDefaultCollection.setEnabled(True)
        self.pushSetDefaultCollection.setCheckable(True)
        self.pushSetDefaultCollection.setChecked(True)
        self.pushSetDefaultCollection.setObjectName(_fromUtf8("pushSetDefaultCollection"))
        self.gridLayout_3.addWidget(self.pushSetDefaultCollection, 4, 1, 1, 1)
        self.pushAddCollection = QtGui.QPushButton(self.collectionFrame)
        self.pushAddCollection.setObjectName(_fromUtf8("pushAddCollection"))
        self.gridLayout_3.addWidget(self.pushAddCollection, 1, 1, 1, 1)
        self.pushRemoveCollection = QtGui.QPushButton(self.collectionFrame)
        self.pushRemoveCollection.setObjectName(_fromUtf8("pushRemoveCollection"))
        self.gridLayout_3.addWidget(self.pushRemoveCollection, 3, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.collectionFrame, 1, 0, 1, 1)
        self.terminalLayout = QtGui.QVBoxLayout()
        self.terminalLayout.setObjectName(_fromUtf8("terminalLayout"))
        self.gridLayout_5.addLayout(self.terminalLayout, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 619, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuProject = QtGui.QMenu(self.menubar)
        self.menuProject.setObjectName(_fromUtf8("menuProject"))
        MainWindow.setMenuBar(self.menubar)
        self.actionNew = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/raw/pics/document-new.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew.setIcon(icon1)
        self.actionNew.setObjectName(_fromUtf8("actionNew"))
        self.actionOpen = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/raw/pics/document-open.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon2)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionSave = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/raw/pics/document-save.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon3)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionSaveAs = QtGui.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/raw/pics/document-save-as.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSaveAs.setIcon(icon4)
        self.actionSaveAs.setObjectName(_fromUtf8("actionSaveAs"))
        self.actionExit = QtGui.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/raw/pics/application-exit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon5)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionUpdateRepo = QtGui.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/raw/pics/view-refresh.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUpdateRepo.setIcon(icon6)
        self.actionUpdateRepo.setObjectName(_fromUtf8("actionUpdateRepo"))
        self.actionPackages = QtGui.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/raw/pics/applications-other.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPackages.setIcon(icon7)
        self.actionPackages.setObjectName(_fromUtf8("actionPackages"))
        self.actionInstallationImagePackages = QtGui.QAction(MainWindow)
        self.actionInstallationImagePackages.setIcon(icon7)
        self.actionInstallationImagePackages.setObjectName(_fromUtf8("actionInstallationImagePackages"))
        self.actionLanguages = QtGui.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/raw/pics/applications-education-language.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLanguages.setIcon(icon8)
        self.actionLanguages.setObjectName(_fromUtf8("actionLanguages"))
        self.actionMakeImage = QtGui.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/raw/pics/media-optical.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionMakeImage.setIcon(icon9)
        self.actionMakeImage.setObjectName(_fromUtf8("actionMakeImage"))
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSaveAs)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuProject.addAction(self.actionUpdateRepo)
        self.menuProject.addSeparator()
        self.menuProject.addAction(self.actionPackages)
        self.menuProject.addAction(self.actionInstallationImagePackages)
        self.menuProject.addAction(self.actionLanguages)
        self.menuProject.addSeparator()
        self.menuProject.addAction(self.actionMakeImage)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuProject.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lineTitle, self.lineParameters)
        MainWindow.setTabOrder(self.lineParameters, self.lineRepository)
        MainWindow.setTabOrder(self.lineRepository, self.lineReleaseFiles)
        MainWindow.setTabOrder(self.lineReleaseFiles, self.linePluginPackage)
        MainWindow.setTabOrder(self.linePluginPackage, self.lineWorkFolder)
        MainWindow.setTabOrder(self.lineWorkFolder, self.comboType)
        MainWindow.setTabOrder(self.comboType, self.pushBrowseRepository)
        MainWindow.setTabOrder(self.pushBrowseRepository, self.pushBrowseReleaseFiles)
        MainWindow.setTabOrder(self.pushBrowseReleaseFiles, self.pushBrowsePluginPackage)
        MainWindow.setTabOrder(self.pushBrowsePluginPackage, self.pushBrowseWorkFolder)
        MainWindow.setTabOrder(self.pushBrowseWorkFolder, self.comboCompression)
        MainWindow.setTabOrder(self.comboCompression, self.listPackageCollection)
        MainWindow.setTabOrder(self.listPackageCollection, self.pushAddCollection)
        MainWindow.setTabOrder(self.pushAddCollection, self.pushModifyCollection)
        MainWindow.setTabOrder(self.pushModifyCollection, self.pushRemoveCollection)
        MainWindow.setTabOrder(self.pushRemoveCollection, self.pushSetDefaultCollection)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(kdecore.i18n("Pardusman"))
        self.label.setText(kdecore.i18n("Image title"))
        self.lineTitle.setToolTip(kdecore.i18n("The title of the Pardus image"))
        self.label_5.setText(kdecore.i18n("Extra parameters"))
        self.lineParameters.setToolTip(kdecore.i18n("Extra parameters to pass to the kernel command line during boot."))
        self.label_3.setText(kdecore.i18n("Repository"))
        self.lineRepository.setToolTip(kdecore.i18n("Local or remote URL of the repository index from which the image will be created"))
        self.pushBrowseRepository.setText(kdecore.i18n("Browse"))
        self.label_4.setText(kdecore.i18n("Release files"))
        self.lineReleaseFiles.setToolTip(kdecore.i18n("Path to the local directory which contains metadata about the image like the release notes, etc."))
        self.pushBrowseReleaseFiles.setText(kdecore.i18n("Browse"))
        self.label_6.setText(kdecore.i18n("Plugin package"))
        self.pushBrowsePluginPackage.setText(kdecore.i18n("Browse"))
        self.label_2.setText(kdecore.i18n("Work folder"))
        self.lineWorkFolder.setToolTip(kdecore.i18n("Path to the directory where Pardusman will work and create the related files and directories"))
        self.pushBrowseWorkFolder.setText(kdecore.i18n("Browse"))
        self.label_7.setText(kdecore.i18n("Image type"))
        self.comboType.setItemText(0, kdecore.i18n("Installation Image"))
        self.comboType.setItemText(1, kdecore.i18n("Live Image"))
        self.comboCompression.setItemText(0, kdecore.i18n("gzip"))
        self.comboCompression.setItemText(1, kdecore.i18n("lzma"))
        self.comboCompression.setItemText(2, kdecore.i18n("lzo"))
        self.checkCollection.setText(kdecore.i18n("Collection Base"))
        self.pushModifyCollection.setText(kdecore.i18n("Modify"))
        self.label_9.setText(kdecore.i18n("Installation Collection List"))
        self.pushSetDefaultCollection.setText(kdecore.i18n("Set as Default"))
        self.pushAddCollection.setText(kdecore.i18n("Add"))
        self.pushRemoveCollection.setText(kdecore.i18n("Remove"))
        self.menuFile.setTitle(kdecore.i18n("File"))
        self.menuProject.setTitle(kdecore.i18n("Project"))
        self.actionNew.setText(kdecore.i18n("New"))
        self.actionOpen.setText(kdecore.i18n("Open..."))
        self.actionSave.setText(kdecore.i18n("Save"))
        self.actionSaveAs.setText(kdecore.i18n("Save As..."))
        self.actionExit.setText(kdecore.i18n("Exit"))
        self.actionUpdateRepo.setText(kdecore.i18n("Update Repo"))
        self.actionPackages.setText(kdecore.i18n("Packages..."))
        self.actionInstallationImagePackages.setText(kdecore.i18n("Installation Image Packages..."))
        self.actionLanguages.setText(kdecore.i18n("Languages..."))
        self.actionMakeImage.setText(kdecore.i18n("Make Image"))

import raw_rc