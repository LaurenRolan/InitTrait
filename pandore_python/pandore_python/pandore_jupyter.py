"""
Python wrapper around Pandore inside Jupyter. You need pandore.py to use it.
"""
__author__ = ("Nicolas Licour")

import pandore
import matplotlib.pyplot as plt
import os

def pvisuJ( imagePan, cmap, title=None ):
	pvisuJTmp = "pvisuJTmp.pan"
	jpegPicture = "pvisuJResut.jpeg" 
	
	pandore.pnormalization(0, 255, imagePan, pvisuJTmp)
	pandore.pim2uc(pvisuJTmp, pvisuJTmp)

	pandore.ppan2jpeg(1, pvisuJTmp, jpegPicture)
	
	m = plt.imread(jpegPicture)
	if title != None:
		plt.title(title)

	plt.imshow(m, cmap=cmap)
	plt.show()
	
	os.remove(pvisuJTmp)
	os.remove(jpegPicture)

def pvisuJG( imagePan, title=None ):
	pvisuJ(imagePan, 'gray', title=title)
	
def pvisuJC( imagePan, title=None ):
	pvisuJ(imagePan, None, title=title)
	
def pstatusJ():
	result = str(pandore.pstatus())
	return result[2:result.index("\\")]
