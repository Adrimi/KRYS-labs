from numpy import array, bitwise_xor
from PIL import Image

pathToFlag = 'General/flag.png'
pathToLemur = 'General/lemur.png'

flag = Image.open(pathToFlag)
lemur = Image.open(pathToLemur)

flagBytesArray = array(flag)
lemurBytesArray = array(lemur)

xorowanie = bitwise_xor(flagBytesArray, lemurBytesArray)
output = Image.fromarray(xorowanie)
output.show()