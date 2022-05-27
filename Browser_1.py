#Creating Web Browser in Python
#Importing necesssary packages
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *

#Defining window class (to create a window)-sub class of QMainWindow class
class MyWebBrowser(QMainWindow):
    #Defining constructor function
    def __init__(self):
        #Creating connnection with parent class constructor
        super(MyWebBrowser, self).__init__() 
        #---------------------adding browser-------------------
        self.browser = QWebEngineView()

        #to display browser in full screen mode
        self.showMaximized()

        #Setting window title
        self.window = QWidget()
        self.window.setWindowTitle("Web Browser")

        self.layout = QVBoxLayout()
        self.horizontal = QHBoxLayout()

        #Adding back button
        self.back_btn = QPushButton("<")
        self.back_btn.setMinimumHeight(30)

        #Adding forward button
        self.forward_btn = QPushButton(">")
        self.forward_btn.setMinimumHeight(30)

        #Adding Go button
        self.go_btn = QPushButton("Go")
        self.go_btn.setMinimumHeight(30)

        #Setting url for browser
        self.url_bar = QTextEdit("https://www.google.com") 
        self.url_bar.setMaximumHeight(30)

        #Adding created buttons to horizontal layout
        self.horizontal.addWidget(self.back_btn)
        self.horizontal.addWidget(self.forward_btn)
        self.horizontal.addWidget(self.go_btn)
        self.horizontal.addWidget(self.url_bar)

        #Event handling for buttons
        self.go_btn.clicked.connect(lambda: self.navigate(self.url_bar.toPlainText()))
        self.back_btn.clicked.connect(self.browser.back)
        self.forward_btn.clicked.connect(self.browser.forward)

        #Adding created horizontal layout to vertical layout
        self.layout.addLayout(self.horizontal)
        self.layout.addWidget(self.browser)

        #Default url
        self.browser.setUrl(QUrl("https://www.google.com"))

        #Adding created vertical layout to window
        self.window.setLayout(self.layout)
        self.window.show()

    #Method to navigate to the required url
    def navigate(self, url):
        if not url.startswith("https"):
            url = "https://" + url
            self.url_bar.setText(url)
        self.browser.setUrl(QUrl(url))

app = QApplication([]) 
#Creating window object 
window = MyWebBrowser()
#Showing window
app.exec_()  