#!/usr/bin/env python
# coding=UTF-8
#
# Generated by pykdeuic4 from gui/ui/rawlanguages.ui on Mon Oct 22 15:18:27 2012
#
# WARNING! All changes to this file will be lost.
from PyKDE4 import kdecore
from PyKDE4 import kdeui
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_LanguagesDialog(object):
    def setupUi(self, LanguagesDialog):
        LanguagesDialog.setObjectName(_fromUtf8("LanguagesDialog"))
        LanguagesDialog.resize(467, 350)
        self.gridLayout = QtGui.QGridLayout(LanguagesDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(LanguagesDialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 2, 1)
        self.label_2 = QtGui.QLabel(LanguagesDialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.selectedListWidget = QtGui.QListWidget(LanguagesDialog)
        self.selectedListWidget.setObjectName(_fromUtf8("selectedListWidget"))
        self.gridLayout.addWidget(self.selectedListWidget, 1, 2, 5, 1)
        self.availableListWidget = QtGui.QListWidget(LanguagesDialog)
        self.availableListWidget.setObjectName(_fromUtf8("availableListWidget"))
        self.gridLayout.addWidget(self.availableListWidget, 2, 0, 4, 1)
        spacerItem = QtGui.QSpacerItem(49, 153, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(21, 153, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 2, 3, 1, 1)
        self.addButton = QtGui.QPushButton(LanguagesDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addButton.sizePolicy().hasHeightForWidth())
        self.addButton.setSizePolicy(sizePolicy)
        self.addButton.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/raw/pics/go-next.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addButton.setIcon(icon)
        self.addButton.setObjectName(_fromUtf8("addButton"))
        self.gridLayout.addWidget(self.addButton, 3, 1, 1, 1)
        self.upButton = QtGui.QPushButton(LanguagesDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.upButton.sizePolicy().hasHeightForWidth())
        self.upButton.setSizePolicy(sizePolicy)
        self.upButton.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/raw/pics/go-up.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.upButton.setIcon(icon1)
        self.upButton.setObjectName(_fromUtf8("upButton"))
        self.gridLayout.addWidget(self.upButton, 3, 3, 1, 1)
        self.removeButton = QtGui.QPushButton(LanguagesDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.removeButton.sizePolicy().hasHeightForWidth())
        self.removeButton.setSizePolicy(sizePolicy)
        self.removeButton.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/raw/pics/go-previous.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.removeButton.setIcon(icon2)
        self.removeButton.setObjectName(_fromUtf8("removeButton"))
        self.gridLayout.addWidget(self.removeButton, 4, 1, 1, 1)
        self.downButton = QtGui.QPushButton(LanguagesDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.downButton.sizePolicy().hasHeightForWidth())
        self.downButton.setSizePolicy(sizePolicy)
        self.downButton.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/raw/pics/go-down.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.downButton.setIcon(icon3)
        self.downButton.setObjectName(_fromUtf8("downButton"))
        self.gridLayout.addWidget(self.downButton, 4, 3, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(49, 68, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 5, 1, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(21, 68, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 5, 3, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(LanguagesDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 6, 2, 1, 1)

        self.retranslateUi(LanguagesDialog)
        QtCore.QMetaObject.connectSlotsByName(LanguagesDialog)
        LanguagesDialog.setTabOrder(self.addButton, self.removeButton)
        LanguagesDialog.setTabOrder(self.removeButton, self.upButton)
        LanguagesDialog.setTabOrder(self.upButton, self.downButton)
        LanguagesDialog.setTabOrder(self.downButton, self.buttonBox)

    def retranslateUi(self, LanguagesDialog):
        LanguagesDialog.setWindowTitle(kdecore.i18n("Languages"))
        self.label.setText(kdecore.i18n("Available:"))
        self.label_2.setText(kdecore.i18n("Selected:"))

import raw_rc
