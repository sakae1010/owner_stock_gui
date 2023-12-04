import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QTextEdit, QTabWidget

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
        tab1_layout = QVBoxLayout()
        self.input_view = QLineEdit()
        self.input_view.setPlaceholderText("在這裡輸入文本...")
        tab1_layout.addWidget(self.input_view)
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
        self.input_view.textChanged.connect(self.onTextChanged)

    def onTextChanged(self, text):
        # 當輸入框的文本改變時更新顯示視圖
        self.display_view.setPlainText(text)

# Qt 應用主程式
app = QApplication(sys.argv)
win = MyWindow()
win.show()
sys.exit(app.exec_())
