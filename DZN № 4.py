# Задание № 4
# Пункт 1
# Создать файл с текстом, а затем написать программу которая будет считывать текст из файла выбирая только
# нужные слова и поместить данные слова в отдельный документ
f = open("dz№4.txt",'w')
text = "Python -это скриптованный язык программирования"
f.write(text)
f.close()
f = open("dz№4.txt","r")
text = f.read()
text = text.split()
print(text)
f.close()
for x in text:
    if x == "Python":
       f = open("dz№4(1).txt",'w')
       f.write(x)
       f.write("\n")
       f.close()
    elif x == "скриптованный":
        f = open("dz№4(1).txt",'a')
        f.write(x)
        f.write("\n")
        f.close()
    elif x == "язык":
        f = open("dz№4(1).txt",'a')
        f.write(x)
        f.write("\n")
        f.close()
f = open("dz№4(1).txt",'r')
print(f.read())
f.close()
#
# 
# Задание № 4
# Пункт 2
# Закрепить работу с json файлами, создать простенький json файл и затем его прочитать.
import json
jsonText ={
"person":[
    {
    "id":"01",
    "name":"Ivan",
    "age": "25",
    "edukation": "higher",
    "work":"manadger",
    "hobby sport":[
        {
        "running": "long disstances",
         "swimming":"short disstances",
         "jumping":"in hight"
           }
         ]
     }
   ]
}
write = json.dumps(jsonText)
f = open("test.json","w")
f.write(write)
f.close()
f = open("test.json","r")
readJSON = f.read()
f.close
print(readJSON)