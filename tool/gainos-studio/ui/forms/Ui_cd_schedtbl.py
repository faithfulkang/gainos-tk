# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\parai@foxmail.com\github\gainos-tk\tool\gainos-studio\ui\forms\cd_schedtbl.ui'
#
# Created: Thu Jul 18 20:00:51 2013
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_cd_schedtbl(object):
    def setupUi(self, cd_schedtbl):
        cd_schedtbl.setObjectName(_fromUtf8("cd_schedtbl"))
        cd_schedtbl.resize(956, 584)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(12)
        font.setWeight(50)
        font.setBold(False)
        cd_schedtbl.setFont(font)
        cd_schedtbl.setStyleSheet(_fromUtf8("font: 12pt \"Consolas\";"))
        self.groupBox = QtGui.QGroupBox(cd_schedtbl)
        self.groupBox.setGeometry(QtCore.QRect(20, 0, 931, 181))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.layoutWidget = QtGui.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(430, 20, 471, 161))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_5 = QtGui.QLabel(self.layoutWidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_6.addWidget(self.label_5)
        self.cmbxSchedTblDrivingCounter = QtGui.QComboBox(self.layoutWidget)
        self.cmbxSchedTblDrivingCounter.setMinimumSize(QtCore.QSize(0, 0))
        self.cmbxSchedTblDrivingCounter.setObjectName(_fromUtf8("cmbxSchedTblDrivingCounter"))
        self.horizontalLayout_6.addWidget(self.cmbxSchedTblDrivingCounter)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_8 = QtGui.QLabel(self.layoutWidget)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_5.addWidget(self.label_8)
        self.cmbxSchedTblSyncStrategy = QtGui.QComboBox(self.layoutWidget)
        self.cmbxSchedTblSyncStrategy.setMinimumSize(QtCore.QSize(0, 0))
        self.cmbxSchedTblSyncStrategy.setObjectName(_fromUtf8("cmbxSchedTblSyncStrategy"))
        self.cmbxSchedTblSyncStrategy.addItem(_fromUtf8(""))
        self.cmbxSchedTblSyncStrategy.addItem(_fromUtf8(""))
        self.cmbxSchedTblSyncStrategy.addItem(_fromUtf8(""))
        self.horizontalLayout_5.addWidget(self.cmbxSchedTblSyncStrategy)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.label_9 = QtGui.QLabel(self.layoutWidget)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_10.addWidget(self.label_9)
        self.spbxSchedTblMaxAdvance = QtGui.QSpinBox(self.layoutWidget)
        self.spbxSchedTblMaxAdvance.setEnabled(True)
        self.spbxSchedTblMaxAdvance.setMinimumSize(QtCore.QSize(181, 0))
        self.spbxSchedTblMaxAdvance.setMinimum(1)
        self.spbxSchedTblMaxAdvance.setMaximum(65535)
        self.spbxSchedTblMaxAdvance.setObjectName(_fromUtf8("spbxSchedTblMaxAdvance"))
        self.horizontalLayout_10.addWidget(self.spbxSchedTblMaxAdvance)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label_10 = QtGui.QLabel(self.layoutWidget)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_8.addWidget(self.label_10)
        self.spbxSchedTblMaxRetard = QtGui.QSpinBox(self.layoutWidget)
        self.spbxSchedTblMaxRetard.setEnabled(True)
        self.spbxSchedTblMaxRetard.setMinimumSize(QtCore.QSize(0, 0))
        self.spbxSchedTblMaxRetard.setMinimum(1)
        self.spbxSchedTblMaxRetard.setMaximum(65535)
        self.spbxSchedTblMaxRetard.setObjectName(_fromUtf8("spbxSchedTblMaxRetard"))
        self.horizontalLayout_8.addWidget(self.spbxSchedTblMaxRetard)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.label_11 = QtGui.QLabel(self.layoutWidget)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_9.addWidget(self.label_11)
        self.spbxSchedTblPrecision = QtGui.QSpinBox(self.layoutWidget)
        self.spbxSchedTblPrecision.setEnabled(False)
        self.spbxSchedTblPrecision.setMinimumSize(QtCore.QSize(181, 0))
        self.spbxSchedTblPrecision.setMinimum(0)
        self.spbxSchedTblPrecision.setMaximum(65535)
        self.spbxSchedTblPrecision.setProperty(_fromUtf8("value"), 0)
        self.spbxSchedTblPrecision.setObjectName(_fromUtf8("spbxSchedTblPrecision"))
        self.horizontalLayout_9.addWidget(self.spbxSchedTblPrecision)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.layoutWidget1 = QtGui.QWidget(self.groupBox)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 20, 361, 153))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.cbxSchedTblRepeatable = QtGui.QCheckBox(self.layoutWidget1)
        self.cbxSchedTblRepeatable.setObjectName(_fromUtf8("cbxSchedTblRepeatable"))
        self.verticalLayout_3.addWidget(self.cbxSchedTblRepeatable)
        self.cbxSchedTblAutostartable = QtGui.QCheckBox(self.layoutWidget1)
        self.cbxSchedTblAutostartable.setEnabled(False)
        self.cbxSchedTblAutostartable.setObjectName(_fromUtf8("cbxSchedTblAutostartable"))
        self.verticalLayout_3.addWidget(self.cbxSchedTblAutostartable)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_6 = QtGui.QLabel(self.layoutWidget1)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_7.addWidget(self.label_6)
        self.cmbxSchedTblAutoStartType = QtGui.QComboBox(self.layoutWidget1)
        self.cmbxSchedTblAutoStartType.setEnabled(False)
        self.cmbxSchedTblAutoStartType.setMinimumSize(QtCore.QSize(0, 0))
        self.cmbxSchedTblAutoStartType.setObjectName(_fromUtf8("cmbxSchedTblAutoStartType"))
        self.cmbxSchedTblAutoStartType.addItem(_fromUtf8(""))
        self.cmbxSchedTblAutoStartType.addItem(_fromUtf8(""))
        self.cmbxSchedTblAutoStartType.addItem(_fromUtf8(""))
        self.horizontalLayout_7.addWidget(self.cmbxSchedTblAutoStartType)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.lblSchedTblAbsRel = QtGui.QLabel(self.layoutWidget1)
        self.lblSchedTblAbsRel.setObjectName(_fromUtf8("lblSchedTblAbsRel"))
        self.horizontalLayout_2.addWidget(self.lblSchedTblAbsRel)
        self.spbxSchedTblAbsRel = QtGui.QSpinBox(self.layoutWidget1)
        self.spbxSchedTblAbsRel.setEnabled(False)
        self.spbxSchedTblAbsRel.setMinimumSize(QtCore.QSize(0, 0))
        self.spbxSchedTblAbsRel.setMaximum(65535)
        self.spbxSchedTblAbsRel.setObjectName(_fromUtf8("spbxSchedTblAbsRel"))
        self.horizontalLayout_2.addWidget(self.spbxSchedTblAbsRel)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_7 = QtGui.QLabel(self.layoutWidget1)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_4.addWidget(self.label_7)
        self.spbxSchedTblFinalDelay = QtGui.QSpinBox(self.layoutWidget1)
        self.spbxSchedTblFinalDelay.setMinimumSize(QtCore.QSize(0, 0))
        self.spbxSchedTblFinalDelay.setMinimum(1)
        self.spbxSchedTblFinalDelay.setMaximum(65535)
        self.spbxSchedTblFinalDelay.setObjectName(_fromUtf8("spbxSchedTblFinalDelay"))
        self.horizontalLayout_4.addWidget(self.spbxSchedTblFinalDelay)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.groupBox_2 = QtGui.QGroupBox(cd_schedtbl)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 190, 931, 391))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.trSchedTable = QtGui.QTreeWidget(self.groupBox_2)
        self.trSchedTable.setGeometry(QtCore.QRect(10, 20, 371, 361))
        self.trSchedTable.setObjectName(_fromUtf8("trSchedTable"))
        item_0 = QtGui.QTreeWidgetItem(self.trSchedTable)
        self.tabSchedTblCfg = QtGui.QTabWidget(self.groupBox_2)
        self.tabSchedTblCfg.setGeometry(QtCore.QRect(390, 170, 541, 80))
        self.tabSchedTblCfg.setObjectName(_fromUtf8("tabSchedTblCfg"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.layoutWidget2 = QtGui.QWidget(self.tab)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 10, 441, 27))
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_4 = QtGui.QLabel(self.layoutWidget2)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_3.addWidget(self.label_4)
        self.spbxSchedEpOffset = QtGui.QSpinBox(self.layoutWidget2)
        self.spbxSchedEpOffset.setMinimumSize(QtCore.QSize(0, 0))
        self.spbxSchedEpOffset.setMaximum(65535)
        self.spbxSchedEpOffset.setObjectName(_fromUtf8("spbxSchedEpOffset"))
        self.horizontalLayout_3.addWidget(self.spbxSchedEpOffset)
        self.tabSchedTblCfg.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.layoutWidget3 = QtGui.QWidget(self.tab_2)
        self.layoutWidget3.setGeometry(QtCore.QRect(10, 10, 401, 27))
        self.layoutWidget3.setObjectName(_fromUtf8("layoutWidget3"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.layoutWidget3)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.cmbxActTskId = QtGui.QComboBox(self.layoutWidget3)
        self.cmbxActTskId.setMinimumSize(QtCore.QSize(250, 0))
        self.cmbxActTskId.setObjectName(_fromUtf8("cmbxActTskId"))
        self.horizontalLayout.addWidget(self.cmbxActTskId)
        self.label_13 = QtGui.QLabel(self.layoutWidget3)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.horizontalLayout.addWidget(self.label_13)
        self.tabSchedTblCfg.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.layoutWidget4 = QtGui.QWidget(self.tab_3)
        self.layoutWidget4.setGeometry(QtCore.QRect(12, 12, 525, 27))
        self.layoutWidget4.setObjectName(_fromUtf8("layoutWidget4"))
        self.horizontalLayout_11 = QtGui.QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout_11.setMargin(0)
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.label_2 = QtGui.QLabel(self.layoutWidget4)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_11.addWidget(self.label_2)
        self.cmbxSetTskId = QtGui.QComboBox(self.layoutWidget4)
        self.cmbxSetTskId.setMinimumSize(QtCore.QSize(180, 0))
        self.cmbxSetTskId.setObjectName(_fromUtf8("cmbxSetTskId"))
        self.horizontalLayout_11.addWidget(self.cmbxSetTskId)
        self.label_12 = QtGui.QLabel(self.layoutWidget4)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.horizontalLayout_11.addWidget(self.label_12)
        self.cmbxSetEnt = QtGui.QComboBox(self.layoutWidget4)
        self.cmbxSetEnt.setMinimumSize(QtCore.QSize(220, 0))
        self.cmbxSetEnt.setObjectName(_fromUtf8("cmbxSetEnt"))
        self.horizontalLayout_11.addWidget(self.cmbxSetEnt)
        self.label_3 = QtGui.QLabel(self.layoutWidget4)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_11.addWidget(self.label_3)
        self.tabSchedTblCfg.addTab(self.tab_3, _fromUtf8(""))
        self.layoutWidget5 = QtGui.QWidget(self.groupBox_2)
        self.layoutWidget5.setGeometry(QtCore.QRect(401, 50, 183, 95))
        self.layoutWidget5.setObjectName(_fromUtf8("layoutWidget5"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget5)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.btnAdd1 = QtGui.QPushButton(self.layoutWidget5)
        self.btnAdd1.setMinimumSize(QtCore.QSize(181, 0))
        self.btnAdd1.setObjectName(_fromUtf8("btnAdd1"))
        self.verticalLayout.addWidget(self.btnAdd1)
        self.btnAdd2 = QtGui.QPushButton(self.layoutWidget5)
        self.btnAdd2.setObjectName(_fromUtf8("btnAdd2"))
        self.verticalLayout.addWidget(self.btnAdd2)
        self.btnDel = QtGui.QPushButton(self.layoutWidget5)
        self.btnDel.setObjectName(_fromUtf8("btnDel"))
        self.verticalLayout.addWidget(self.btnDel)

        self.retranslateUi(cd_schedtbl)
        self.tabSchedTblCfg.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(cd_schedtbl)

    def retranslateUi(self, cd_schedtbl):
        cd_schedtbl.setWindowTitle(QtGui.QApplication.translate("cd_schedtbl", "GaInOS Schedule Table Configure", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("cd_schedtbl", "General", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("cd_schedtbl", "Dirving Counter:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("cd_schedtbl", "Sync Strategy:", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbxSchedTblSyncStrategy.setItemText(0, QtGui.QApplication.translate("cd_schedtbl", "NONE", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbxSchedTblSyncStrategy.setItemText(1, QtGui.QApplication.translate("cd_schedtbl", "EXPLICIT", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbxSchedTblSyncStrategy.setItemText(2, QtGui.QApplication.translate("cd_schedtbl", "IMPLICIT", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("cd_schedtbl", "Max Advance:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("cd_schedtbl", "Max Retard:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("cd_schedtbl", "Precision:", None, QtGui.QApplication.UnicodeUTF8))
        self.cbxSchedTblRepeatable.setText(QtGui.QApplication.translate("cd_schedtbl", "Schedule Table Repeatable", None, QtGui.QApplication.UnicodeUTF8))
        self.cbxSchedTblAutostartable.setText(QtGui.QApplication.translate("cd_schedtbl", "Schedule Table Auto-Start", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("cd_schedtbl", "Auto-Start Type:", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbxSchedTblAutoStartType.setItemText(0, QtGui.QApplication.translate("cd_schedtbl", "ABSOLUTE", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbxSchedTblAutoStartType.setItemText(1, QtGui.QApplication.translate("cd_schedtbl", "RELATIVE", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbxSchedTblAutoStartType.setItemText(2, QtGui.QApplication.translate("cd_schedtbl", "SYNCHRON", None, QtGui.QApplication.UnicodeUTF8))
        self.lblSchedTblAbsRel.setText(QtGui.QApplication.translate("cd_schedtbl", "Absolut Value:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("cd_schedtbl", "Final Delay:", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("cd_schedtbl", "Expiry Point", None, QtGui.QApplication.UnicodeUTF8))
        self.trSchedTable.headerItem().setText(0, QtGui.QApplication.translate("cd_schedtbl", "Schedule Table", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.trSchedTable.isSortingEnabled()
        self.trSchedTable.setSortingEnabled(False)
        self.trSchedTable.topLevelItem(0).setText(0, QtGui.QApplication.translate("cd_schedtbl", "Expiry Point List", None, QtGui.QApplication.UnicodeUTF8))
        self.trSchedTable.setSortingEnabled(__sortingEnabled)
        self.label_4.setText(QtGui.QApplication.translate("cd_schedtbl", "Offset:", None, QtGui.QApplication.UnicodeUTF8))
        self.tabSchedTblCfg.setTabText(self.tabSchedTblCfg.indexOf(self.tab), QtGui.QApplication.translate("cd_schedtbl", "Offset", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("cd_schedtbl", "ActivateTask(", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("cd_schedtbl", ")", None, QtGui.QApplication.UnicodeUTF8))
        self.tabSchedTblCfg.setTabText(self.tabSchedTblCfg.indexOf(self.tab_2), QtGui.QApplication.translate("cd_schedtbl", "ActivateTask", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("cd_schedtbl", "SetEvent(", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("cd_schedtbl", ",", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("cd_schedtbl", ")", None, QtGui.QApplication.UnicodeUTF8))
        self.tabSchedTblCfg.setTabText(self.tabSchedTblCfg.indexOf(self.tab_3), QtGui.QApplication.translate("cd_schedtbl", "SetEvent", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAdd1.setText(QtGui.QApplication.translate("cd_schedtbl", "Add ActivateTask", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAdd2.setText(QtGui.QApplication.translate("cd_schedtbl", "Add SetEvent", None, QtGui.QApplication.UnicodeUTF8))
        self.btnDel.setText(QtGui.QApplication.translate("cd_schedtbl", "Del Expiry Point", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    cd_schedtbl = QtGui.QDialog()
    ui = Ui_cd_schedtbl()
    ui.setupUi(cd_schedtbl)
    cd_schedtbl.show()
    sys.exit(app.exec_())

