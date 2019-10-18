#import from package

''' 
	- MyMainPackage
	  - __init__.py 
	  - main_script.py
	  - SubPackage
	    - __init__.py
	    - mysubscript.py

'''

from MyMainPackage import main_script
from MyMainPackage.SubPackage import mysubscript

main_script.main_report()
mysubscript.sub_report()



'''
Expected Output : 
Function from main package!
Function from sub package!

'''