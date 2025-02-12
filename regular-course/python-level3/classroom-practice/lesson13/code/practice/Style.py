from Variable import *
from PyQt5.Qt import *


def init_ui(app, window, table, title, limg, rimg):
    title.setText(titleCnt)
    title.setStyleSheet(f'font-size:{titleFs};color:{titleColor};font-weight:bold')

    title.setGeometry(titleX, titleY, 300, 100)
    table.setGeometry(tableX, tableY, tableW, tableH)
    table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
    table.setStyleSheet(f'font-size:{fs};background-color: transparent;')
    app.setStyleSheet(f'QHeaderView::section {{ background-color:{thColor} }}'
                      f'QTableCornerButton::section {{ background-color: {tcbColor} }}')

    pixmap = QPixmap(bgPath)
    # 缩放图像到窗口的大小
    scaledPixmap = pixmap.scaled(windowW, windowH, Qt.KeepAspectRatio, Qt.SmoothTransformation)

    palette = QPalette()
    palette.setBrush(window.backgroundRole(), QBrush(scaledPixmap))  # 使用图片设置背景
    window.setPalette(palette)
    window.setFixedSize(windowW, windowH)

    limg.setGeometry(limgX, limgY, limgW, limgH)
    pixmap1 = QPixmap(limgPath)
    limg.setPixmap(pixmap1)

    rimg.setGeometry(rimgX, rimgY, rimgW, rimgH)
    pixmap2 = QPixmap(rimgPath)
    rimg.setPixmap(pixmap2)
