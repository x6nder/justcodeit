# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\MyNext\Python\Projects\GUI\perforg\perforg_gui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_main_window(object):
    def setupUi(self, main_window):
        main_window.setObjectName("main_window")
        main_window.resize(500, 212)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(main_window.sizePolicy().hasHeightForWidth())
        main_window.setSizePolicy(sizePolicy)
        main_window.setMinimumSize(QtCore.QSize(500, 212))
        main_window.setMaximumSize(QtCore.QSize(500, 212))
        main_window.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        main_window.setAutoFillBackground(False)
        main_window.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        main_window.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")
        self.label_downloads = QtWidgets.QLabel(self.centralwidget)
        self.label_downloads.setGeometry(QtCore.QRect(10, 10, 291, 31))
        self.label_downloads.setTextFormat(QtCore.Qt.RichText)
        self.label_downloads.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_downloads.setWordWrap(True)
        self.label_downloads.setObjectName("label_downloads")
        self.label_downloads_answer = QtWidgets.QLineEdit(self.centralwidget)
        self.label_downloads_answer.setGeometry(QtCore.QRect(10, 40, 261, 20))
        self.label_downloads_answer.setObjectName("label_downloads_answer")
        self.delete_files_answer = QtWidgets.QLabel(self.centralwidget)
        self.delete_files_answer.setGeometry(QtCore.QRect(11, 74, 311, 31))
        self.delete_files_answer.setTextFormat(QtCore.Qt.RichText)
        self.delete_files_answer.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.delete_files_answer.setWordWrap(True)
        self.delete_files_answer.setObjectName("delete_files_answer")
        self.delete_answer_yes = QtWidgets.QRadioButton(self.centralwidget)
        self.delete_answer_yes.setGeometry(QtCore.QRect(11, 114, 37, 17))
        self.delete_answer_yes.setObjectName("delete_answer_yes")
        self.delete_answer_no_default = QtWidgets.QRadioButton(self.centralwidget)
        self.delete_answer_no_default.setGeometry(QtCore.QRect(101, 114, 42, 17))
        self.delete_answer_no_default.setChecked(True)
        self.delete_answer_no_default.setObjectName("delete_answer_no_default")
        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_button.setGeometry(QtCore.QRect(330, 10, 161, 121))
        self.start_button.setAutoDefault(False)
        self.start_button.setDefault(False)
        self.start_button.setFlat(False)
        self.start_button.setObjectName("start_button")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(10, 150, 481, 23))
        self.progressBar.setProperty("value", 41)
        self.progressBar.setTextVisible(True)
        self.progressBar.setObjectName("progressBar")
        main_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(main_window)
        self.menubar.setEnabled(True)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 21))
        self.menubar.setObjectName("menubar")
        main_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(main_window)
        self.statusbar.setObjectName("statusbar")
        main_window.setStatusBar(self.statusbar)

        self.retranslateUi(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "Perfectionist Organizer"))
        self.label_downloads.setText(_translate("main_window", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Как у вас называется папка с загрузками?</span></p></body></html>"))
        self.label_downloads_answer.setPlaceholderText(_translate("main_window", "по-умолчанию Загрузки"))
        self.delete_files_answer.setText(_translate("main_window", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Удалить из папки загрузок оставшиеся файлы?</span></p></body></html>"))
        self.delete_answer_yes.setText(_translate("main_window", "Да"))
        self.delete_answer_no_default.setText(_translate("main_window", "Нет"))
        self.start_button.setText(_translate("main_window", "СТАРТ"))