import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QTextEdit, QTabWidget

# class MyWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.input_view = None
#         self.tabs = None
#         self.display_view = None
#         self.init_ui()
#
#     def init_ui(self):
#         # 創建標籤頁容器
#         self.tabs = QTabWidget()
#
#         # 添加標籤頁
#         self.add_tab_input()
#         self.add_tab_display()
#
#         # 主佈局
#         layout = QVBoxLayout()
#         layout.addWidget(self.tabs)
#         self.setLayout(layout)
#
#         # 設置窗口標題
#         self.setWindowTitle('Qt 多標籤視窗')
#
#     def add_tab_input(self):
#         # 第一個標籤頁內容 - 輸入視圖
#         tab1 = QWidget()
#         tab1_layout = QVBoxLayout()
#         self.input_view = QLineEdit()
#         self.input_view.setPlaceholderText("在這裡輸入文本...")
#         self.input_view.textChanged.connect(self.on_text_changed)  # 連接信號
#         tab1_layout.addWidget(self.input_view)
#         tab1.setLayout(tab1_layout)
#         self.tabs.addTab(tab1, "輸入視窗")
#
#     def add_tab_display(self):
#         # 第二個標籤頁內容 - 顯示視圖
#         tab2 = QWidget()
#         tab2_layout = QVBoxLayout()
#         self.display_view = QTextEdit()
#         self.display_view.setPlaceholderText("顯示內容...")
#         tab2_layout.addWidget(self.display_view)
#         tab2.setLayout(tab2_layout)
#         self.tabs.addTab(tab2, "顯示視圖")
#     def on_text_changed(self, text):
#         # 當輸入框的文本改變時更新顯示視圖
#         self.display_view.setPlainText(text)
#
# # Qt 應用主程式
# app = QApplication(sys.argv)
# win = MyWindow()
# win.show()
# sys.exit(app.exec_())
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QTextEdit, QTabWidget, QFormLayout

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 創建標籤頁容器
        tabs = QTabWidget()
        tab1 = QWidget()
        tab2 = QWidget()

        # 將標籤頁加入到標籤容器中
        tabs.addTab(tab1, "輸入視圖")
        tabs.addTab(tab2, "顯示視圖")

        # 第一個標籤頁內容 - 輸入視圖
        tab1_layout = QFormLayout()
        self.trade_date_input = QLineEdit()
        self.stock_quantity_input = QLineEdit()
        self.trade_price_input = QLineEdit()
        self.trade_cost_input = QLineEdit()

        tab1_layout.addRow("交易日期:", self.trade_date_input)
        tab1_layout.addRow("股數:", self.stock_quantity_input)
        tab1_layout.addRow("成交價:", self.trade_price_input)
        tab1_layout.addRow("成交成本:", self.trade_cost_input)
        tab1.setLayout(tab1_layout)

        # 第二個標籤頁內容 - 顯示視圖
        tab2_layout = QVBoxLayout()
        self.display_view = QTextEdit()
        self.display_view.setPlaceholderText("顯示內容...")
        tab2_layout.addWidget(self.display_view)
        tab2.setLayout(tab2_layout)

        # 主佈局
        layout = QVBoxLayout()
        layout.addWidget(tabs)
        self.setLayout(layout)

        # 設置窗口標題
        self.setWindowTitle('Qt 多標籤視窗')

        # 連接輸入視圖的信號
        self.trade_date_input.textChanged.connect(self.updateDisplayView)
        self.stock_quantity_input.textChanged.connect(self.updateDisplayView)
        self.trade_price_input.textChanged.connect(self.updateDisplayView)
        self.trade_cost_input.textChanged.connect(self.updateDisplayView)

    def updateDisplayView(self):
        # 當輸入框的文本改變時更新顯示視圖
        trade_date = self.trade_date_input.text()
        stock_quantity = self.stock_quantity_input.text()
        trade_price = self.trade_price_input.text()
        trade_cost = self.trade_cost_input.text()

        display_text = (
            f"交易日期: {trade_date}\n"
            f"股數: {stock_quantity}\n"
            f"成交價: {trade_price}\n"
            f"成交成本: {trade_cost}"
        )
        self.display_view.setPlainText(display_text)

# Qt 應用主程式
app = QApplication(sys.argv)
win = MyWindow()
win.show()
sys.exit(app.exec_())
