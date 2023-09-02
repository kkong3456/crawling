# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_naver_estate_dataCJIRFu.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(735, 533)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(-80, -30, 821, 581))
        self.label.setStyleSheet(u"background-color:white;")
        self.url1 = QLabel(self.centralwidget)
        self.url1.setObjectName(u"url1")
        self.url1.setGeometry(QRect(30, 30, 61, 41))
        font = QFont()
        font.setFamilies([u"Adobe Hebrew"])
        font.setPointSize(15)
        font.setBold(True)
        self.url1.setFont(font)
        self.url1.setStyleSheet(u"color:black;")
        self.url1.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.get_url_button = QPushButton(self.centralwidget)
        self.get_url_button.setObjectName(u"get_url_button")
        self.get_url_button.setGeometry(QRect(80, 110, 191, 51))
        font1 = QFont()
        font1.setPointSize(15)
        font1.setBold(True)
        font1.setKerning(True)
        self.get_url_button.setFont(font1)
        self.get_url_button.setStyleSheet(u"border:1px solid black;background-color:rgba(230,23,23,0.8)")
        self.url1_line_edit = QLineEdit(self.centralwidget)
        self.url1_line_edit.setObjectName(u"url1_line_edit")
        self.url1_line_edit.setGeometry(QRect(80, 30, 611, 31))
        self.url1_line_edit.setStyleSheet(u"background-color:white;border:1px solid black;color:black;")
        self.url1_2 = QLabel(self.centralwidget)
        self.url1_2.setObjectName(u"url1_2")
        self.url1_2.setGeometry(QRect(30, 70, 61, 41))
        self.url1_2.setFont(font)
        self.url1_2.setStyleSheet(u"color:black;")
        self.url1_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.url1_line_edit_2 = QLineEdit(self.centralwidget)
        self.url1_line_edit_2.setObjectName(u"url1_line_edit_2")
        self.url1_line_edit_2.setGeometry(QRect(80, 70, 611, 31))
        self.url1_line_edit_2.setStyleSheet(u"background-color:white;border:1px solid black;color:black;")
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(30, 170, 661, 271))
        self.textEdit.setStyleSheet(u"background-color:white;color:black;border:1px solid black;")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 735, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.url1.setText(QCoreApplication.translate("MainWindow", u"URL1", None))
        self.get_url_button.setText(QCoreApplication.translate("MainWindow", u"\uac00\uc838\uc624\uae30", None))
        self.url1_line_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"  URL \uc744 \uc785\ub825\ud574\uc8fc\uc138\uc694", None))
        self.url1_2.setText(QCoreApplication.translate("MainWindow", u"URL2", None))
        self.url1_line_edit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"  URL \uc744 \uc785\ub825\ud574\uc8fc\uc138\uc694", None))
    # retranslateUi

