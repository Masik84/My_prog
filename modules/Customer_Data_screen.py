import pandas as pd
from PyQt5.Qt import *
from PyQt5.QtWidgets import QFileDialog

from modules.Customer_Edit_screen import *
from modules.Customer_Filter_screen import *
from modules.Customer_New_screen import *
from modules.DB_Tables_creation import *
from modules.DelAddress_Edit_screen import *
from modules.DelAddress_Filter_screen import *
from modules.DelAddress_New_screen import *

db_path = 'modules/Bonus_db.db'

DBTables_creation_if_new()


class SoldTo_Functions(QtWidgets.QWidget):
    def __init__(self):
        super(SoldTo_Functions, self).__init__()

        self.customer_data_page = QtWidgets.QWidget(self)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/images/icons/cil-folder-open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/images/icons/filter.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.customer_data_page.setStyleSheet("QPushButton {\n"
                                             "    border: 2px solid #6272a4;\n"
                                             "    border-radius: 5px;\n"
                                             "    background-color: #6272a4;\n"
                                             "    color: #f8f8f2;\n"
                                             "}\n"
                                             "\n"
                                             "QPushButton:hover {\n"
                                             "    background-color: #bd93f9;\n"
                                             "    border: 2px solid #7082b6;\n"
                                             "}\n"
                                             "\n"
                                             "QPushButton:pressed {\n"
                                             "    background-color: #ff79c6;\n"
                                             "    border: 2px solid #ff79c6;\n"
                                             "}\n"
                                             "\n"
                                             " QLineEdit {\n"
                                             "    background-color: #6272a4;\n"
                                             "    border-radius: 5px;\n"
                                             "    border: 2px solid #6272a4;\n"
                                             "    padding-left: 10px;\n"
                                             "    selection-color: rgb(255, 255, 255);\n"
                                             "    selection-background-color: rgb(255, 121, 198);\n"
                                             "    color: #f8f8f2;\n"
                                             "}\n"
                                             "\n"
                                             "QLineEdit:hover {\n"
                                             "    border: 2px solid #bd93f9;\n"
                                             "}\n"
                                             "\n"
                                             "QLineEdit:focus {\n"
                                             "    border: 2px solid #ff79c6;\n"
                                             "}")
        self.customer_data_page.setObjectName("customer_data_page")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.customer_data_page)
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.row_4 = QtWidgets.QFrame(self.customer_data_page)
        self.row_4.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.row_4.setFont(font)
        self.row_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.row_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.row_4.setObjectName("row_4")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.row_4)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label = QtWidgets.QLabel(self.row_4)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(26)
        font.setBold(True)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_14.addWidget(self.label, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.verticalLayout_20.addWidget(self.row_4)
        self.row_5 = QtWidgets.QFrame(self.customer_data_page)
        self.row_5.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.row_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.row_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.row_5.setObjectName("row_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.row_5)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.soldto_frame = QtWidgets.QFrame(self.row_5)
        self.soldto_frame.setMaximumSize(QtCore.QSize(16777215, 500))
        self.soldto_frame.setStyleSheet("")
        self.soldto_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.soldto_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.soldto_frame.setObjectName("soldto_frame")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.soldto_frame)
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.soldto_heade_frame = QtWidgets.QFrame(self.soldto_frame)
        self.soldto_heade_frame.setMinimumSize(QtCore.QSize(0, 50))
        self.soldto_heade_frame.setMaximumSize(QtCore.QSize(16777215, 50))
        self.soldto_heade_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.soldto_heade_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.soldto_heade_frame.setObjectName("soldto_heade_frame")
        self.verticalLayout_27 = QtWidgets.QVBoxLayout(self.soldto_heade_frame)
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName("verticalLayout_27")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_2 = QtWidgets.QLabel(self.soldto_heade_frame)
        self.label_2.setMinimumSize(QtCore.QSize(0, 50))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 0, 0, 1, 1)
        self.verticalLayout_27.addLayout(self.gridLayout_4)
        self.verticalLayout_21.addWidget(self.soldto_heade_frame)
        self.soldto_body_frame = QtWidgets.QFrame(self.soldto_frame)
        self.soldto_body_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.soldto_body_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.soldto_body_frame.setObjectName("soldto_body_frame")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout(self.soldto_body_frame)
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setContentsMargins(9, 9, 9, 9)
        self.gridLayout_3.setSpacing(9)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.soldto_edit_btn = QtWidgets.QPushButton(self.soldto_body_frame)
        self.soldto_edit_btn.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.soldto_edit_btn.setFont(font)
        self.soldto_edit_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/icons/images/icons/cil-user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.soldto_edit_btn.setIcon(icon11)
        self.soldto_edit_btn.setObjectName("soldto_edit_btn")
        self.gridLayout_3.addWidget(self.soldto_edit_btn, 0, 3, 1, 1)
        self.soldto_update_btn = QtWidgets.QPushButton(self.soldto_body_frame)
        self.soldto_update_btn.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.soldto_update_btn.setFont(font)
        self.soldto_update_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/icons/images/icons/cil-reload.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.soldto_update_btn.setIcon(icon12)
        self.soldto_update_btn.setObjectName("soldto_update_btn")
        self.gridLayout_3.addWidget(self.soldto_update_btn, 0, 0, 1, 1)
        self.soldto_delete_btn = QtWidgets.QPushButton(self.soldto_body_frame)
        self.soldto_delete_btn.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.soldto_delete_btn.setFont(font)
        self.soldto_delete_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/icons/images/icons/cil-user-unfollow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.soldto_delete_btn.setIcon(icon13)
        self.soldto_delete_btn.setObjectName("soldto_delete_btn")
        self.gridLayout_3.addWidget(self.soldto_delete_btn, 0, 4, 1, 1)
        self.soldto_add_btn = QtWidgets.QPushButton(self.soldto_body_frame)
        self.soldto_add_btn.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.soldto_add_btn.setFont(font)
        self.soldto_add_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/icons/images/icons/cil-user-follow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.soldto_add_btn.setIcon(icon14)
        self.soldto_add_btn.setObjectName("soldto_add_btn")
        self.gridLayout_3.addWidget(self.soldto_add_btn, 0, 2, 1, 1)
        self.soldto_filter_btn = QtWidgets.QPushButton(self.soldto_body_frame)
        self.soldto_filter_btn.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.soldto_filter_btn.setFont(font)
        self.soldto_filter_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.soldto_filter_btn.setIcon(icon8)
        self.soldto_filter_btn.setObjectName("soldto_filter_btn")
        self.gridLayout_3.addWidget(self.soldto_filter_btn, 0, 1, 1, 1)
        self.verticalLayout_22.addLayout(self.gridLayout_3)
        self.frame_3 = QtWidgets.QFrame(self.soldto_body_frame)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.frame_3.setFont(font)
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_16.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_16.setSpacing(2)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.soldto_error_lable = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.soldto_error_lable.setFont(font)
        self.soldto_error_lable.setText("")
        self.soldto_error_lable.setAlignment(QtCore.Qt.AlignCenter)
        self.soldto_error_lable.setObjectName("soldto_error_lable")
        self.horizontalLayout_16.addWidget(self.soldto_error_lable)
        self.verticalLayout_22.addWidget(self.frame_3)
        self.soldto_table_frame = QtWidgets.QFrame(self.soldto_body_frame)
        self.soldto_table_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.soldto_table_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.soldto_table_frame.setObjectName("soldto_table_frame")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.soldto_table_frame)
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.soldto_table = QtWidgets.QTableWidget(self.soldto_table_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.soldto_table.sizePolicy().hasHeightForWidth())
        self.soldto_table.setSizePolicy(sizePolicy)
        self.soldto_table.setMinimumSize(QtCore.QSize(510, 250))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(51, 51, 51))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 51, 51))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 51, 51))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 51, 51))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 51, 51))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 51, 51))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 51, 51))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 51, 51))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 51, 51))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 51, 51))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 51, 51))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 51, 51))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.soldto_table.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.soldto_table.setFont(font)
        self.soldto_table.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.soldto_table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.soldto_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.soldto_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.soldto_table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.soldto_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.soldto_table.setShowGrid(True)
        self.soldto_table.setGridStyle(QtCore.Qt.SolidLine)
        self.soldto_table.setRowCount(0)
        self.soldto_table.setColumnCount(3)
        self.soldto_table.setObjectName("soldto_table")
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.soldto_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.soldto_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.soldto_table.setHorizontalHeaderItem(2, item)
        self.soldto_table.horizontalHeader().setVisible(True)
        self.soldto_table.horizontalHeader().setCascadingSectionResizes(True)
        self.soldto_table.horizontalHeader().setDefaultSectionSize(160)
        self.soldto_table.horizontalHeader().setStretchLastSection(True)
        self.soldto_table.verticalHeader().setVisible(False)
        self.soldto_table.verticalHeader().setCascadingSectionResizes(False)
        self.soldto_table.verticalHeader().setHighlightSections(False)
        self.soldto_table.verticalHeader().setStretchLastSection(False)
        self.horizontalLayout_13.addWidget(self.soldto_table)
        self.verticalLayout_22.addWidget(self.soldto_table_frame)
        self.verticalLayout_21.addWidget(self.soldto_body_frame)
        self.horizontalLayout_6.addWidget(self.soldto_frame)
        self.shipto_frame = QtWidgets.QFrame(self.row_5)
        self.shipto_frame.setMaximumSize(QtCore.QSize(16777215, 500))
        self.shipto_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.shipto_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.shipto_frame.setObjectName("shipto_frame")
        self.verticalLayout_23 = QtWidgets.QVBoxLayout(self.shipto_frame)
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.shipto_header_frame = QtWidgets.QFrame(self.shipto_frame)
        self.shipto_header_frame.setMinimumSize(QtCore.QSize(0, 50))
        self.shipto_header_frame.setMaximumSize(QtCore.QSize(16777215, 50))
        self.shipto_header_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.shipto_header_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.shipto_header_frame.setObjectName("shipto_header_frame")
        self.verticalLayout_26 = QtWidgets.QVBoxLayout(self.shipto_header_frame)
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_3 = QtWidgets.QLabel(self.shipto_header_frame)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_5.addWidget(self.label_3, 0, 0, 1, 1)
        self.verticalLayout_26.addLayout(self.gridLayout_5)
        self.verticalLayout_23.addWidget(self.shipto_header_frame)
        self.shipto_body_frame = QtWidgets.QFrame(self.shipto_frame)
        self.shipto_body_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.shipto_body_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.shipto_body_frame.setObjectName("shipto_body_frame")
        self.verticalLayout_24 = QtWidgets.QVBoxLayout(self.shipto_body_frame)
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setContentsMargins(9, 9, 9, 9)
        self.gridLayout_6.setSpacing(9)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.shipto_add_btn = QtWidgets.QPushButton(self.shipto_body_frame)
        self.shipto_add_btn.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.shipto_add_btn.setFont(font)
        self.shipto_add_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.shipto_add_btn.setIcon(icon14)
        self.shipto_add_btn.setObjectName("shipto_add_btn")
        self.gridLayout_6.addWidget(self.shipto_add_btn, 0, 2, 1, 1)
        self.shipto_edit_btn = QtWidgets.QPushButton(self.shipto_body_frame)
        self.shipto_edit_btn.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.shipto_edit_btn.setFont(font)
        self.shipto_edit_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.shipto_edit_btn.setIcon(icon11)
        self.shipto_edit_btn.setObjectName("shipto_edit_btn")
        self.gridLayout_6.addWidget(self.shipto_edit_btn, 0, 3, 1, 1)
        self.shipto_update_btn = QtWidgets.QPushButton(self.shipto_body_frame)
        self.shipto_update_btn.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.shipto_update_btn.setFont(font)
        self.shipto_update_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.shipto_update_btn.setIcon(icon12)
        self.shipto_update_btn.setObjectName("shipto_update_btn")
        self.gridLayout_6.addWidget(self.shipto_update_btn, 0, 0, 1, 1)
        self.shipto_delete_btn = QtWidgets.QPushButton(self.shipto_body_frame)
        self.shipto_delete_btn.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.shipto_delete_btn.setFont(font)
        self.shipto_delete_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.shipto_delete_btn.setIcon(icon13)
        self.shipto_delete_btn.setObjectName("shipto_delete_btn")
        self.gridLayout_6.addWidget(self.shipto_delete_btn, 0, 4, 1, 1)
        self.shipto_filter_btn = QtWidgets.QPushButton(self.shipto_body_frame)
        self.shipto_filter_btn.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.shipto_filter_btn.setFont(font)
        self.shipto_filter_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.shipto_filter_btn.setIcon(icon8)
        self.shipto_filter_btn.setObjectName("shipto_filter_btn")
        self.gridLayout_6.addWidget(self.shipto_filter_btn, 0, 1, 1, 1)
        self.verticalLayout_24.addLayout(self.gridLayout_6)
        self.frame_4 = QtWidgets.QFrame(self.shipto_body_frame)
        self.frame_4.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.frame_4.setFont(font)
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_7.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_7.setSpacing(2)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.shipto_error_lable = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.shipto_error_lable.setFont(font)
        self.shipto_error_lable.setText("")
        self.shipto_error_lable.setAlignment(QtCore.Qt.AlignCenter)
        self.shipto_error_lable.setObjectName("shipto_error_lable")
        self.horizontalLayout_7.addWidget(self.shipto_error_lable)
        self.verticalLayout_24.addWidget(self.frame_4)
        self.shipto_frame_table = QtWidgets.QFrame(self.shipto_body_frame)
        self.shipto_frame_table.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.shipto_frame_table.setFrameShadow(QtWidgets.QFrame.Raised)
        self.shipto_frame_table.setObjectName("shipto_frame_table")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.shipto_frame_table)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.shipto_table = QtWidgets.QTableWidget(self.shipto_frame_table)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.shipto_table.sizePolicy().hasHeightForWidth())
        self.shipto_table.setSizePolicy(sizePolicy)
        self.shipto_table.setMinimumSize(QtCore.QSize(510, 250))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(51, 51, 51))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 51, 51))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 51, 51))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 51, 51))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 51, 51))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 51, 51))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 51, 51))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 51, 51))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 51, 51))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 51, 51))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 51, 51))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 51, 51))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.shipto_table.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.shipto_table.setFont(font)
        self.shipto_table.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.shipto_table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.shipto_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.shipto_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.shipto_table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.shipto_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.shipto_table.setShowGrid(True)
        self.shipto_table.setGridStyle(QtCore.Qt.SolidLine)
        self.shipto_table.setRowCount(0)
        self.shipto_table.setColumnCount(3)
        self.shipto_table.setObjectName("shipto_table")
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.shipto_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.shipto_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.shipto_table.setHorizontalHeaderItem(2, item)
        self.shipto_table.horizontalHeader().setVisible(True)
        self.shipto_table.horizontalHeader().setCascadingSectionResizes(True)
        self.shipto_table.horizontalHeader().setDefaultSectionSize(160)
        self.shipto_table.horizontalHeader().setStretchLastSection(True)
        self.shipto_table.verticalHeader().setVisible(False)
        self.shipto_table.verticalHeader().setCascadingSectionResizes(False)
        self.shipto_table.verticalHeader().setHighlightSections(False)
        self.shipto_table.verticalHeader().setStretchLastSection(False)
        self.horizontalLayout_10.addWidget(self.shipto_table)
        self.verticalLayout_24.addWidget(self.shipto_frame_table)
        self.verticalLayout_23.addWidget(self.shipto_body_frame)
        self.horizontalLayout_6.addWidget(self.shipto_frame)
        self.verticalLayout_20.addWidget(self.row_5)
        self.row_9 = QtWidgets.QFrame(self.customer_data_page)
        self.row_9.setMaximumSize(QtCore.QSize(16777215, 60))
        self.row_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.row_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.row_9.setObjectName("row_9")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.row_9)
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.frame = QtWidgets.QFrame(self.row_9)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.cust_file_path_lable = QtWidgets.QLabel(self.frame)
        self.cust_file_path_lable.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cust_file_path_lable.setFont(font)
        self.cust_file_path_lable.setStyleSheet("background-color: #6272a4;\n"
                                                "                                                                  border-radius: 5px;\n"
                                                "                                                                  border: 2px solid #6272a4;\n"
                                                "                                                                  padding-left: 10px;\n"
                                                "                                                                  selection-color: rgb(255, 255, 255);\n"
                                                "                                                                  selection-background-color: rgb(255, 121, 198);\n"
                                                "                                                                  color: #f8f8f2;\n"
                                                "                                                              ")
        self.cust_file_path_lable.setObjectName("cust_file_path_lable")
        self.horizontalLayout_17.addWidget(self.cust_file_path_lable)
        self.horizontalLayout_19.addWidget(self.frame)
        self.frame_6 = QtWidgets.QFrame(self.row_9)
        self.frame_6.setMinimumSize(QtCore.QSize(100, 0))
        self.frame_6.setMaximumSize(QtCore.QSize(120, 16777215))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.open_file_btn = QtWidgets.QPushButton(self.frame_6)
        self.open_file_btn.setMinimumSize(QtCore.QSize(90, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.open_file_btn.setFont(font)
        self.open_file_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.open_file_btn.setIcon(icon4)
        self.open_file_btn.setObjectName("open_file_btn")
        self.horizontalLayout_18.addWidget(self.open_file_btn)
        self.horizontalLayout_19.addWidget(self.frame_6)
        self.frame_5 = QtWidgets.QFrame(self.row_9)
        self.frame_5.setMinimumSize(QtCore.QSize(100, 0))
        self.frame_5.setMaximumSize(QtCore.QSize(120, 16777215))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.upload_file_btn = QtWidgets.QPushButton(self.frame_5)
        self.upload_file_btn.setMinimumSize(QtCore.QSize(90, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.upload_file_btn.setFont(font)
        self.upload_file_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/icons/images/icons/upload.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.upload_file_btn.setIcon(icon15)
        self.upload_file_btn.setObjectName("upload_file_btn")
        self.horizontalLayout_8.addWidget(self.upload_file_btn)
        self.horizontalLayout_19.addWidget(self.frame_5)
        self.verticalLayout_20.addWidget(self.row_9)

        self.upload_Soldto_from_DB()
        self.upload_Shipto_from_DB()

        self.soldto_update_btn.clicked.connect(self.upload_Soldto_from_DB)
        self.soldto_filter_btn.clicked.connect(self.filter_Client_data)
        self.soldto_add_btn.clicked.connect(self.go_to_Create_Client)
        self.soldto_edit_btn.clicked.connect(self.go_to_Edit_Client)
        self.soldto_delete_btn.clicked.connect(self.go_to_Delete_Client)

        self.shipto_update_btn.clicked.connect(self.upload_Shipto_from_DB)
        self.shipto_filter_btn.clicked.connect(self.filter_Address_data)
        self.shipto_add_btn.clicked.connect(self.go_to_Create_Address)
        self.shipto_edit_btn.clicked.connect(self.go_to_Edit_Address)
        self.shipto_delete_btn.clicked.connect(self.go_to_Delete_Address)

        self.soldto_table.itemDoubleClicked.connect(self.go_to_Edit_Client)
        self.shipto_table.itemDoubleClicked.connect(self.go_to_Edit_Address)

        self.open_file_btn.clicked.connect(self.choose_customer_file)
        self.upload_file_btn.clicked.connect(self.upload_customer_file_to_DB)

        # Разрешить щелчок правой кнопкой мыши для создания меню
        self.soldto_table.setContextMenuPolicy(Qt.CustomContextMenu)
        # Привязать контекстное меню к функции слота generateMenu
        self.soldto_table.customContextMenuRequested.connect(self.generate_Soldto_Menu)

        # Разрешить щелчок правой кнопкой мыши для создания меню
        self.shipto_table.setContextMenuPolicy(Qt.CustomContextMenu)
        # Привязать контекстное меню к функции слота generateMenu
        self.shipto_table.customContextMenuRequested.connect(self.generate_Shipto_Menu)

    def generate_Soldto_Menu(self, pos):
        # Рассчитать, сколько существует данных, по умолчанию -1,
        row_num = -1
        for i in self.soldto_table.selectionModel().selection().indexes():
            row_num = i.row()
            cust_code = self.soldto_table.item(row_num, 0).text()
            cust_name = self.soldto_table.item(row_num, 1).text()

            # В таблице только две допустимые данные, поэтому всплывающее меню с правой кнопкой мыши поддерживают только первые две строки
        if row_num > -1:
            menu = QMenu()
            act_cust_update = menu.addAction(u'Update Table')
            act_cust_edit = menu.addAction(u'Edit Sold-To')
            act_cust_delete = menu.addAction(u'Delete Sold-To')
            action = menu.exec_(self.soldto_table.mapToGlobal(pos))

            if action == act_cust_update:
                self.upload_Soldto_from_DB()

            if action == act_cust_edit:
                self.go_to_Edit_Client()

            if action == act_cust_delete:
                self.go_to_Delete_Client()

    def generate_Shipto_Menu(self, pos):
        # Рассчитать, сколько существует данных, по умолчанию -1,
        row_num = -1
        for i in self.shipto_table.selectionModel().selection().indexes():
            row_num = i.row()
            addr_code = self.shipto_table.item(row_num, 0).text()
            addr_name = self.shipto_table.item(row_num, 1).text()

            # В таблице только две допустимые данные, поэтому всплывающее меню с правой кнопкой мыши поддерживают только первые две строки
        if row_num > -1:
            menu = QMenu()
            act_addr_update = menu.addAction(u'Update Table')
            act_addr_edit = menu.addAction(u'Edit Ship-To')
            act_addr_delete = menu.addAction(u'Delete Ship-To')
            action = menu.exec_(self.shipto_table.mapToGlobal(pos))

            if action == act_addr_update:
                self.upload_Shipto_from_DB()

            if action == act_addr_edit:
                self.go_to_Edit_Address()

            if action == act_addr_delete:
                self.go_to_Delete_Address()

    def upload_Soldto_from_DB(self):
        conn = sqlite3.Connection(db_path)

        show_customer_data = 'SELECT SoldTo, SoldTo_name_en, SoldTo_name_ru FROM Customers'
        result = conn.execute(show_customer_data)
        self.soldto_table.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.soldto_table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.soldto_table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        conn.close()
        self.soldto_error_lable.setText('Table was updated successfully')

    def go_to_Create_Client(self):
        self.client_creation_form = QDialog()
        self.client_new = Ui_Customer_Creation_Form()
        self.client_new.setupUi(self.client_creation_form)
        self.client_creation_form.show()
        self.client_new.save_btn.clicked.connect(self.push_new_client_to_db)
        self.client_new.cancel_btn.clicked.connect(self.client_creation_form.close)

    def push_new_client_to_db(self):
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()

        cust_code = self.client_new.cust_code_feild.text()
        cust_name_en = self.client_new.cust_name_en_feild.text()
        cust_name_ru = self.client_new.cust_name_ru_feild.text()

        cur.execute('SELECT SoldTo FROM Customers WHERE SoldTo = ?', (cust_code,))

        if len(cust_code) == 0:
            self.client_new.soldto_error_lable.setText('Please fill in Customer Sold-to number')
        elif cur.fetchone() is None:
            if len(cust_name_en) == 0 or len(cust_name_ru) == 0:
                self.client_new.soldto_error_lable.setText('Please fill in Customer Name')
            else:
                customer_info = [cust_code, cust_name_en, cust_name_ru]
                cur.execute('INSERT INTO Customers (SoldTo, SoldTo_name_en, SoldTo_name_ru) VALUES (?,?,?)', customer_info)
                conn.commit()
                conn.close()

                self.upload_Soldto_from_DB()
                self.client_creation_form.close()
        else:
            self.client_new.soldto_error_lable.setText('Customer with such Sold-To code already exists')

    def filter_Client_data(self):
        self.upload_Soldto_from_DB()
        self.client_filter_form = QDialog()
        self.client_filter = Ui_Customer_Filter_Form()
        self.client_filter.setupUi(self.client_filter_form)
        self.client_filter_form.show()
        self.client_filter.client_filter_btn.clicked.connect(self.find_client_in_db)
        self.client_filter.client_filter_cancel_btn.clicked.connect(self.client_filter_form.close)

    def find_client_in_db(self):
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()

        cust_code2 = self.client_filter.filter_cust_code_feild.text()

        filter_data_db = (f'SELECT SoldTo, SoldTo_name_en, SoldTo_name_ru FROM Customers WHERE SoldTo ="{cust_code2}";')

        result = cur.execute(filter_data_db)
        self.soldto_table.clearContents()

        self.soldto_table.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.soldto_table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.soldto_table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        self.client_filter_form.close()
        conn.close()

    def go_to_Edit_Client(self):
        self.client_edit_form = QDialog()
        self.client_edit = Ui_Customer_Edit_Form()
        self.client_edit.setupUi(self.client_edit_form)

        cust_row = self.soldto_table.currentRow()  # определяем выделенную строку
        table_cust_code = self.soldto_table.item(cust_row, 0).text()
        table_cust_name_en = self.soldto_table.item(cust_row, 1).text()
        table_cust_name_ru = self.soldto_table.item(cust_row, 2).text()

        self.client_edit.cust_code_lable.setText(table_cust_code)
        self.client_edit.cust_name_en_feild.setText(table_cust_name_en)
        self.client_edit.cust_name_ru_feild.setText(table_cust_name_ru)

        self.client_edit_form.show()
        self.client_edit.save_btn.clicked.connect(self.push_edit_client_to_db)
        self.client_edit.cancel_btn.clicked.connect(self.client_edit_form.close)

    def push_edit_client_to_db(self):
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()

        cust_code = self.client_edit.cust_code_lable.text()
        cust_name_en = self.client_edit.cust_name_en_feild.text()
        cust_name_ru = self.client_edit.cust_name_ru_feild.text()

        customer_info_for_db = [cust_name_en, cust_name_ru, cust_code]

        client_update_request = """UPDATE Customers SET SoldTo_name_en = ?, SoldTo_name_ru = ? WHERE SoldTo = ?"""
        cur.execute(client_update_request, customer_info_for_db)
        conn.commit()
        conn.close()

        self.upload_Soldto_from_DB()
        self.client_edit_form.close()
        self.soldto_error_lable.setText('Customer was updated successfully')

    def go_to_Delete_Client(self):
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()

        cust_row = self.soldto_table.currentRow()                                 # определяем выделенную строку
        cust_code = self.soldto_table.item(cust_row, 0).text()                     # определяем значение в 1й колонке выделенной строки
        cust_code = int(cust_code)

        cur.execute('DELETE FROM Customers WHERE SoldTo = ?', (cust_code, ))
        conn.commit()
        conn.close()

        self.upload_Soldto_from_DB()
        self.soldto_error_lable.setText('Customer was deleted successfully!')

    def upload_Shipto_from_DB(self):
        conn = sqlite3.Connection(db_path)

        show_address_data = 'SELECT ShipTo, SoldTo_name_en, SoldTo_name_ru FROM DeliveryAddress'
        result = conn.execute(show_address_data)
        self.shipto_table.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.shipto_table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.shipto_table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        conn.close()
        self.shipto_error_lable.setText('Table was updated successfully')

    def go_to_Create_Address(self):
        self.address_creation_form = QDialog()
        self.address_new = Ui_DelAddress_Creation_Form()
        self.address_new.setupUi(self.address_creation_form)
        self.address_creation_form.show()
        self.address_new.save_btn.clicked.connect(self.push_new_address_to_db)
        self.address_new.cancel_btn.clicked.connect(self.address_creation_form.close)

    def push_new_address_to_db(self):
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()

        addr_code = self.address_new.addr_code_feild.text()
        addr_name_en = self.address_new.addr_name_en_feild.text()
        addr_name_ru = self.address_new.addr_name_ru_feild.text()

        cur.execute('SELECT ShipTo FROM DeliveryAddress WHERE ShipTo = ?', (addr_code,))

        if len(addr_code) == 0:
            self.address_new.shipto_error_lable.setText('Please fill in Delivery Address Ship-to number')
        elif cur.fetchone() is None:
            if len(addr_name_en) == 0 or len(addr_name_ru) == 0:
                self.address_new.shipto_error_lable.setText('Please fill in Delivery Address Name')
            else:
                address_info = [addr_code, addr_name_en, addr_name_ru]
                cur.execute('INSERT INTO DeliveryAddress (ShipTo, SoldTo_name_en, SoldTo_name_ru) VALUES (?,?,?)', address_info)
                conn.commit()
                conn.close()

                self.upload_Shipto_from_DB()
                self.address_creation_form.close()
        else:
            self.address_new.shipto_error_lable.setText('Delivery Address with such Ship-To code already exists')

    def filter_Address_data(self):
        self.upload_Shipto_from_DB()
        self.address_filter_form = QDialog()
        self.address_filter = Ui_DelAddress_Filter_Form()
        self.address_filter.setupUi(self.address_filter_form)
        self.address_filter_form.show()
        self.address_filter.address_filter_btn.clicked.connect(self.find_address_in_db)
        self.address_filter.address_filter_cancel_btn.clicked.connect(self.address_filter_form.close)

    def find_address_in_db(self):
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()

        addr_code2 = self.address_filter.filter_address_code_feild.text()

        filter_data_db = (f'SELECT ShipTo, SoldTo_name_en, SoldTo_name_ru FROM DeliveryAddress WHERE ShipTo ="{addr_code2}";')

        result = cur.execute(filter_data_db)
        self.shipto_table.clearContents()

        self.shipto_table.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.shipto_table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.shipto_table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        self.address_filter_form.close()
        conn.close()

    def go_to_Edit_Address(self):
        self.address_edit_form = QDialog()
        self.address_edit = Ui_DelAddress_Edit_Form()
        self.address_edit.setupUi(self.address_edit_form)

        addr_row = self.shipto_table.currentRow()  # определяем выделенную строку
        table_addr_code = self.shipto_table.item(addr_row, 0).text()
        table_addr_name_en = self.shipto_table.item(addr_row, 1).text()
        table_addr_name_ru = self.shipto_table.item(addr_row, 2).text()

        self.address_edit.addr_code_lable.setText(table_addr_code)
        self.address_edit.addr_name_en_feild.setText(table_addr_name_en)
        self.address_edit.addr_name_ru_feild.setText(table_addr_name_ru)

        self.address_edit_form.show()
        self.address_edit.save_btn.clicked.connect(self.push_edit_address_to_db)
        self.address_edit.cancel_btn.clicked.connect(self.address_edit_form.close)

    def push_edit_address_to_db(self):
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()

        addr_code = self.address_edit.addr_code_lable.text()
        addr_name_en = self.address_edit.addr_name_en_feild.text()
        addr_name_ru = self.address_edit.addr_name_ru_feild.text()

        address_info_for_db = [addr_name_en, addr_name_ru, addr_code]

        address_update_request = """UPDATE DeliveryAddress SET SoldTo_name_en = ?, SoldTo_name_ru = ? WHERE ShipTo = ?"""
        cur.execute(address_update_request, address_info_for_db)
        conn.commit()
        conn.close()

        self.upload_Shipto_from_DB()
        self.address_edit_form.close()
        self.shipto_error_lable.setText('Delivery Address was updated successfully')

    def go_to_Delete_Address(self):
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()

        addr_row = self.shipto_table.currentRow()  # определяем выделенную строку
        addr_code = self.shipto_table.item(addr_row, 0).text()  # определяем значение в 1й колонке выделенной строки
        addr_code = int(addr_code)

        cur.execute('DELETE FROM DeliveryAddress WHERE ShipTo = ?', (addr_code,))
        conn.commit()
        conn.close()

        self.upload_Shipto_from_DB()
        self.shipto_error_lable.setText('Delivery Address was deleted successfully!')

    def choose_customer_file(self):
        choose_file = QFileDialog.getOpenFileName(self, 'Choose File')
        if choose_file:
            self.cust_file_path_lable.setText(choose_file[0])

    def upload_customer_file_to_DB(self):
        conn = sqlite3.connect(db_path)

        # temporary Customer table creation
        cust_file = pd.read_excel(self.cust_file_path_lable.text(), sheet_name='Sheet1')
        cust_file.to_sql(name='tmp_customers', con=conn, if_exists='replace', index=True)
        conn.commit()

        # Insert new customers
        conn.execute('''
                                    INSERT INTO Customers (SoldTo, Soldto_name_en, Soldto_name_ru)
                                    SELECT DISTINCT tmp.SoldTo, tmp.Soldto_name_en, tmp.Soldto_name_ru
                                    FROM tmp_customers as tmp, Customers as c
                                    ''')

        # Update existed customers
        conn.execute('''
                                    UPDATE Customers
                                    SET SoldTo = (SELECT DISTINCT tmp.SoldTo FROM tmp_customers as tmp WHERE Customers.SoldTo = tmp.SoldTo),
                                    Soldto_name_en = (SELECT DISTINCT tmp.Soldto_name_en FROM tmp_customers as tmp WHERE Customers.SoldTo = tmp.SoldTo),
                                    Soldto_name_ru = (SELECT DISTINCT tmp.Soldto_name_ru FROM tmp_customers as tmp WHERE Customers.SoldTo = tmp.SoldTo)
                                    ''')

        # Insert new addresses
        conn.execute('''
                                    INSERT INTO DeliveryAddress (ShipTo, Soldto_name_en, Soldto_name_ru)
                                    SELECT DISTINCT tmp.ShipTo, tmp.Soldto_name_en, tmp.Soldto_name_ru
                                    FROM tmp_customers as tmp, Customers as c
                                    ''')

        # Update existed addresses
        conn.execute('''
                                    UPDATE DeliveryAddress
                                    SET ShipTo = (SELECT DISTINCT tmp.ShipTo FROM tmp_customers as tmp WHERE DeliveryAddress.ShipTo = tmp.ShipTo),
                                    Soldto_name_en = (SELECT DISTINCT tmp.Soldto_name_en FROM tmp_customers as tmp WHERE DeliveryAddress.ShipTo = tmp.ShipTo),
                                    Soldto_name_ru = (SELECT DISTINCT tmp.Soldto_name_ru FROM tmp_customers as tmp WHERE DeliveryAddress.ShipTo = tmp.ShipTo)
                                    ''')

        conn.commit()

        conn.execute('''DROP TABLE IF EXISTS tmp_customers''')

        conn.commit()
        conn.close()

        self.upload_Soldto_from_DB()
        self.upload_Shipto_from_DB()
        self.cust_file_path_lable.setText('Database was updated successfully')
