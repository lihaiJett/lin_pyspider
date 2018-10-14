from urllib import parse


path = "D://Pyspider_Result"


def getQuestionCount(self, dir_path):
    t = open(path + dir_path + "/acount.txt", "r", encoding='utf-8')
    count = (int)(t.read())
    t.close()
    return count


def setQuestionCount(self, dir_path, count):
    f = open(path + dir_path + "/acount.txt", "w", encoding='utf-8')
    f.write(str(count))
    f.close()


setQuestionCount("", "/zn", 5)
a = getQuestionCount("", "/zn")
