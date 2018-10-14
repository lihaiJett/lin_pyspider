import os

# 文本文件合并
filelist = os.listdir('D://Pyspider_Result/zn')
# for item in filelist:
#     print (item)

newfile = open('D://Pyspider_Result/new.txt', 'w', encoding='UTF-8')
i = 1
for item in filelist:
    if item.endswith('acount.txt'):
        print("跳过")
        break
    newfile.write("-------------------" + str(i) + "-------------------\n")
    i += 1
    for txt in open('D://Pyspider_Result/zn/'+item, 'r', encoding='UTF-8'):
        newfile.write(txt)

newfile.close()
