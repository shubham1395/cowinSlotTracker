# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.0.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_CowinSlots(object):
    def setupUi(self, CowinSlots):
        if not CowinSlots.objectName():
            CowinSlots.setObjectName(u"CowinSlots")
        CowinSlots.resize(900, 665)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CowinSlots.sizePolicy().hasHeightForWidth())
        CowinSlots.setSizePolicy(sizePolicy)
        CowinSlots.setMaximumSize(QSize(900, 665))
        self.gridLayout = QGridLayout(CowinSlots)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer, 0, 0, 1, 4)

        self.runButton = QPushButton(CowinSlots)
        self.runButton.setObjectName(u"runButton")
        icon = QIcon()
        icon.addFile(u"images/run.png", QSize(), QIcon.Normal, QIcon.Off)
        self.runButton.setIcon(icon)

        self.gridLayout.addWidget(self.runButton, 1, 2, 1, 1)

        self.districtSelect = QComboBox(CowinSlots)
        self.districtSelect.addItem("")
        self.districtSelect.setObjectName(u"districtSelect")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.districtSelect.sizePolicy().hasHeightForWidth())
        self.districtSelect.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.districtSelect, 1, 1, 1, 1)

        self.slotsTable = QTableWidget(CowinSlots)
        if (self.slotsTable.columnCount() < 6):
            self.slotsTable.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.slotsTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.slotsTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.slotsTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.slotsTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.slotsTable.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.slotsTable.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.slotsTable.setObjectName(u"slotsTable")
        self.slotsTable.horizontalHeader().setDefaultSectionSize(147)
        self.slotsTable.horizontalHeader().setStretchLastSection(False)

        self.gridLayout.addWidget(self.slotsTable, 4, 0, 1, 4)

        self.label = QLabel(CowinSlots)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)

        self.stopButton = QPushButton(CowinSlots)
        self.stopButton.setObjectName(u"stopButton")
        icon1 = QIcon()
        icon1.addFile(u"images/stop.png", QSize(), QIcon.Normal, QIcon.Off)
        self.stopButton.setIcon(icon1)

        self.gridLayout.addWidget(self.stopButton, 1, 3, 1, 1)

        self.stateSelect = QComboBox(CowinSlots)
        self.stateSelect.addItem("")
        self.stateSelect.setObjectName(u"stateSelect")
        sizePolicy1.setHeightForWidth(self.stateSelect.sizePolicy().hasHeightForWidth())
        self.stateSelect.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.stateSelect, 1, 0, 1, 1)

        self.runningStatus = QLabel(CowinSlots)
        self.runningStatus.setObjectName(u"runningStatus")

        self.gridLayout.addWidget(self.runningStatus, 2, 0, 1, 1)


        self.retranslateUi(CowinSlots)

        QMetaObject.connectSlotsByName(CowinSlots)
    # setupUi

    def retranslateUi(self, CowinSlots):
        CowinSlots.setWindowTitle(QCoreApplication.translate("CowinSlots", u"CowinSlots", None))
        self.runButton.setText(QCoreApplication.translate("CowinSlots", u"Run", None))
        self.districtSelect.setItemText(0, QCoreApplication.translate("CowinSlots", u"Select District", None))

        ___qtablewidgetitem = self.slotsTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("CowinSlots", u"Date", None));
        ___qtablewidgetitem1 = self.slotsTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("CowinSlots", u"Vaccine", None));
        ___qtablewidgetitem2 = self.slotsTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("CowinSlots", u"Centre Name", None));
        ___qtablewidgetitem3 = self.slotsTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("CowinSlots", u"Address", None));
        ___qtablewidgetitem4 = self.slotsTable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("CowinSlots", u"Block Name", None));
        ___qtablewidgetitem5 = self.slotsTable.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("CowinSlots", u"Available Slots", None));
        self.label.setText("")
        self.stopButton.setText(QCoreApplication.translate("CowinSlots", u"Stop", None))
        self.stateSelect.setItemText(0, QCoreApplication.translate("CowinSlots", u"Select State", None))

        self.runningStatus.setText(QCoreApplication.translate("CowinSlots", u"Currently Not Running!", None))
    # retranslateUi

