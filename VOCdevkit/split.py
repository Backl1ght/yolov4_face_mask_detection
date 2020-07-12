import os
from shutil import copyfile

src = './val/'
xml_dst = './VOC2007/Annotation/'
jpg_dst = './VOC2007/JPEGImages/'
file_list = os.listdir(src)

print(len(file_list))

for file in file_list:
	if file.endswith('.jpg'):
		copyfile(src+file, jpg_dst+file)
	elif file.endswith('.xml'):
		copyfile(src+file, xml_dst+file)

src = './train/'
xml_dst = './VOC2007/Annotation/'
jpg_dst = './VOC2007/JPEGImages/'
file_list = os.listdir(src)

print(len(file_list))

for file in file_list:
	if file.endswith('.jpg'):
		copyfile(src+file, jpg_dst+file)
	elif file.endswith('.xml'):
		copyfile(src+file, xml_dst+file)

