from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
def runHelpWindowGUI():
	class helpWindow(QWidget):
		def __init__(self):
			super(helpWindow,self).__init__()
			self.initializeUI()
		def initializeUI(self):
			self.setGeometry(200,200,640,480)
			self.setWindowTitle('Help Window')
			self.show()
	def main():
		application = QApplication(sys.argv)
		start = helpWindow()
		sys.exit(application.exec_())
	if __name__ == "__main__":
		main()
print("que2")