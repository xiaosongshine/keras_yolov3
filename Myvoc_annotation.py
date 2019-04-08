import xml.etree.ElementTree as ET
from os import getcwd
import sys
sys.path.append("./")

output_dir = "./output/"
data_dir = "./shapes/"

sets=[('2019', 'imgs')]

classes = ["aeroplane", "bicycle", "bird", "boat", "bottle", "bus", "car", "cat", "chair", "cow", "diningtable", "dog", "horse", "motorbike", "person", "pottedplant", "sheep", "sofa", "train", "tvmonitor"]
My_classes = ["triangle","circle","square"]

def convert_annotation(year, image_id, list_file):
    img = image_id.strip('.jpg')
    print(image_id)
    in_file = open(data_dir+'xmls/%s.xml'%(img),'r',encoding="UTF-8")
    tree=ET.parse(in_file)
    root = tree.getroot()

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in My_classes or int(difficult)==1:
            continue
        cls_id = My_classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (int(xmlbox.find('xmin').text), int(xmlbox.find('ymin').text), int(xmlbox.find('xmax').text), int(xmlbox.find('ymax').text))
        list_file.write(" " + ",".join([str(a) for a in b]) + ',' + str(cls_id))

wd = getcwd()

for year, image_set in sets:
    image_ids = open(output_dir+'data.txt',encoding="UTF-8").read().strip().split("\n")
    list_file = open(output_dir+'%s.txt'%(image_set), 'w',encoding="UTF-8")
    for image_id in image_ids:
        list_file.write('%s/shapes/imgs/%s'%(wd,image_id))
        convert_annotation(year, image_id, list_file)
        list_file.write('\n')
    list_file.close()
    print("list finish!!")

