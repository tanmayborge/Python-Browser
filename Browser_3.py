# importing required libraries
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtPrintSupport import *
import os
import sys

#Creating main window class
class MainWindow(QMainWindow):

	#Constructor
	def __init__(self, *args, **kwargs):
		super(MainWindow, self).__init__(*args, **kwargs)

		#Creating a QWebEngineView
		self.browser = QWebEngineView()

		#Setting default browser url as google
		self.browser.setUrl(QUrl("https://duckduckgo.com"))

		#Adding action when url get changed
		self.browser.urlChanged.connect(self.update_urlbar)

		#Adding action when loading is finished
		self.browser.loadFinished.connect(self.update_title)

		#Set this browser as central widget or main window
		self.setCentralWidget(self.browser)

		#Creating a status bar object
		self.status = QStatusBar()

		#Adding status bar to the main window
		self.setStatusBar(self.status)

		#Creating QToolBar for navigation
		navtb = QToolBar("Navigation")

		#Adding this tool bar tot he main window
		self.addToolBar(navtb)

		#Adding actions to the tool bar
		#Creating a action for back
		back_btn = QAction("Back", self)

		#Setting status tip
		back_btn.setStatusTip("Back to previous page")

		#Adding action to the back button
		#Making browser go back
		back_btn.triggered.connect(self.browser.back)

		#Adding this action to tool bar
		navtb.addAction(back_btn)

		#Similarly for forward action
		next_btn = QAction("Forward", self)
		next_btn.setStatusTip("Forward to next page")

		#Adding action to the next button
		#Making browser go forward
		next_btn.triggered.connect(self.browser.forward)
		navtb.addAction(next_btn)

		#Similarly for reload action
		reload_btn = QAction("Reload", self)
		reload_btn.setStatusTip("Reload page")

		#Adding action to the reload button
		#Making browser to reload
		reload_btn.triggered.connect(self.browser.reload)
		navtb.addAction(reload_btn)

		#Similarly for home action
		home_btn = QAction("Home", self)
		home_btn.setStatusTip("Go home")
		home_btn.triggered.connect(self.navigate_home)
		navtb.addAction(home_btn)

		#Adding a separator in the tool bar
		navtb.addSeparator()

		#Creating a line edit for the url
		self.urlbar = QLineEdit()

		#Adding action when return key is pressed
		self.urlbar.returnPressed.connect(self.navigate_to_url)
        
        #Adding stop action to the tool bar
		stop_btn = QAction("Stop", self)
		stop_btn.setStatusTip("Stop loading current page")
		
        #Adding this to the tool bar
		navtb.addWidget(self.urlbar)

		#Adding action to the stop button
		#Making browser to stop
		stop_btn.triggered.connect(self.browser.stop)
		navtb.addAction(stop_btn)

		#Showing all the components
		self.show()

	#Method for updating the title of the window
	def update_title(self):
		title = self.browser.page().title()
		self.setWindowTitle("% s - Python Browser" % title)

	#Method called by the home action
	def navigate_home(self):

		#Open the Duckduckgo
		self.browser.setUrl(QUrl("http://www.duckduckgo.com"))

	#Method called by the line edit when return key is pressed
	def navigate_to_url(self):

		#Getting url and converting it to QUrl object
		q = QUrl(self.urlbar.text())

		#If url is scheme is blank
		if q.scheme() == "":
			#Set url scheme to html
			q.setScheme("https")

		#Set the url to the browser
		self.browser.setUrl(q)

	#Method for updating url
	def update_urlbar(self, q):

		#Setting text to the url bar
		self.urlbar.setText(q.toString())

		#Setting cursor position of the url bar
		self.urlbar.setCursorPosition(0)

#Creating a pyQt5 application
app = QApplication(sys.argv)

#Setting name to the application
app.setApplicationName("Python Browser")

#Creating a main window object
window = MainWindow()

#Loop
app.exec_()
