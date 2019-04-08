import os
PATH_IMGS = "./shapes/imgs/"
PATH_XMLS = "./shapes/xmls/"
LIST_DIR = "./output/data.txt"


for img in os.listdir(PATH_XMLS):
    os.rename(PATH_XMLS+img,PATH_XMLS+img.replace(" ", "_"))
for img in os.listdir(PATH_IMGS):
    os.rename(PATH_IMGS+img,PATH_IMGS+img.replace(" ", "_"))

def remove_file(path):
    if(os.path.exists(path)):
        os.remove(path)
        print('移除后%s文件成功'%path.split("/")[-1])
    else:
        print("要删除的文件不存在！")
count = 0
for xml in os.listdir(PATH_XMLS):
    if(xml.split(".xml")[0]+".jpg" not in  os.listdir(PATH_IMGS)):
        count += 1
        remove_file(PATH_XMLS+xml)
print(count)
list_file = open(LIST_DIR, 'w',encoding="UTF-8")



for img in os.listdir(PATH_IMGS):
    list_file.write(img.strip(' ')+"\n")

list_file.close()
print("write ok")


