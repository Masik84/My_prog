# convert with application settings in the end
# pyuic5 -x Customer_Filter_screen.ui -o Customer_Filter_screen.py

# convert w/o app settings
# pyuic5 -o Customer_New_screen.py Customer_New_screen.ui

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve
from PyQt5.QtGui import QColor, QIcon
from PyQt5.QtWidgets import QMainWindow, QGraphicsDropShadowEffect, QSizeGrip

from modules.ui_main import Ui_MainWindow
import sys

WINDOW_SIZE = 0


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # DROP SHADOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(17)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 150))
        self.ui.bgApp.setGraphicsEffect(self.shadow)

        # MINIMIZE
        self.ui.minimizeAppBtn.clicked.connect(lambda: self.showMinimized())
        # MAXIMIZE/RESTORE
        self.ui.maximizeRestoreAppBtn.clicked.connect(lambda: self.maximize_restore())
        # CLOSE APPLICATION
        self.ui.closeAppBtn.clicked.connect(lambda: self.close())
        # SLIDE MENU
        self.ui.toggleButton.clicked.connect(lambda: self.toggleMenu())
        self.ui.contentTopBg.mouseMoveEvent = self.MoveWindow

        self.ui.stackedWidget.setCurrentWidget(self.ui.home)

        self.ui.btn_home.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.home))
        self.ui.btn_bonuses.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.bonus_data_page))
        # self.ui.btn_invoices.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.product_data_page))
        self.ui.btn_customers.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.customer_data_page))
        self.ui.btn_products.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.product_data_page))

        # RESIZE WINDOW
        self.sizegrip = QSizeGrip(self.ui.frame_size_grip)
        self.sizegrip.setStyleSheet("width: 20px; height: 20px; margin 0px; padding: 0px;")
        # APPLY DROPSHADOW TO FRAME
        self.ui.frame_size_grip.setGraphicsEffect(self.shadow)



    def maximize_restore(self):
        global WINDOW_SIZE
        status = WINDOW_SIZE
        if status == 0:
            WINDOW_SIZE = 1
            self.showMaximized()

            self.ui.appMargins.setContentsMargins(0, 0, 0, 0)
            self.ui.maximizeRestoreAppBtn.setToolTip("Restore")
            self.ui.maximizeRestoreAppBtn.setIcon(QIcon(u":/icons/images/icons/icon_restore.png"))
        else:
            WINDOW_SIZE = 0
            self.showNormal()

            self.resize(self.width() + 1, self.height() + 1)
            self.ui.appMargins.setContentsMargins(10, 10, 10, 10)
            self.ui.maximizeRestoreAppBtn.setToolTip("Maximize")
            self.ui.maximizeRestoreAppBtn.setIcon(QIcon(u":/icons/images/icons/icon_maximize.png"))

    def MoveWindow(self, event):
        if self.isMaximized() == False:
            self.move(self.pos() + event.globalPos() - self.clickPosition)
            self.clickPosition = event.globalPos()
            event.accept()

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

    def toggleMenu(self):
        width = self.ui.leftMenuBg.width()
        maxExtend = 150
        standard = 60

        # SET MAX WIDTH
        if width == 60:
            widthExtended = maxExtend
        else:
            widthExtended = standard

        # ANIMATION
        self.animation = QPropertyAnimation(self.ui.leftMenuBg, b"minimumWidth")
        self.animation.setDuration(500)
        self.animation.setStartValue(width)
        self.animation.setEndValue(widthExtended)
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()











if __name__ == "__main__":
    MainApp = QtWidgets.QApplication(sys.argv)
    App = MainWindow()
    App.show()
    sys.exit(MainApp.exec_())
