from io import StringIO
import xml.etree.ElementTree as ET
# mở file và đọc các nút
file_object = open('demo.jff')  # demo.jff is file'name which located in the same folder as the project
xml = file_object.read()
xml_file = StringIO(xml)
tree = ET.parse(xml_file)
root = tree.getroot()

from ReadFile import *
print('Hãy nhập vào xâu nhị phân: ')
strA = input()
Automat=readFile(strA,root)
