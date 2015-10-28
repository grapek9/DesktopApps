from PyQt4.QtGui import *
from PyQt4.QtCore import *

class mainWindow(QWidget):
	def __init__(self):
		super(mainWindow,self).__init__()
		self.initializeUI()
	def initializeUI(self):
		self.setGeometry(200,200,640,480)
		self.setWindowTitle('File Explorer By Grapek9')
		self.show()
def main():
	application = QApplication(sys.argv)
	start = mainWindow()
	sys.exit(application.exec_())
if __name__ == "__main__":
	main()