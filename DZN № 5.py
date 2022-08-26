# Задание № 5
# 1. Вывести данные из файла json, а именно id, name, age, gender, balance, email, phone, isActive
# 2. Отсортировать полученные данные по полю isActive, записать полученный результат в файл result.txt
# 3. Отсортировать по возрастанию balance только активных пользователей, записать полученный результат в файл result.txt
# 4. Опубликовать работу на гитхаб. Репозиторий: https://github.com/LessonsTop/practic-1 в ветки practic_FI (Где FI - фамилия и имя).

import sys
import ssl
from urllib import request

def downloadFile():
    ssl._create_default_https_context = ssl._create_unverified_context

    fileName = 'generated.json'
    urlFile = 'https://cloud.it-stepbystep.ru/s/tciPs29rFjxrHpm/download/generated.json'
    headerUrl = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'}

    try:
        url = request.Request(urlFile, None, headerUrl)
        page = request.urlopen(url)
        f = open(fileName, 'wb')
        f.write(page.read())
        f.close()
    except Exception:
        print(sys.exc_info()[1])
        exit()

downloadFile()

# Пункт 1.
# Вывести данные из файла json, а именно id, name, age, gender, balance, email, phone, isActive
import json
jsonDocument = 'generated.json'
# jsonDocument файл скачанный по условию
f = open(jsonDocument,"r")
# прочитать файл
jsonData = json.load(f)
# преобразовать в файл pyton
f.close()
listUsers = []
# создать список
for x in jsonData:
    print("User id: ", x["_id"])
    print("User name: ", x["name"])
    print("User age: ", x["age"])
    print("User gender: ", x["gender"])
    print("User balance: ", x["balance"])
    print("User email: ", x["email"])
    print("User phone: ", x["phone"])
    print("User isActive: ", x["isActive"])
    print("=" * 15)
    intelligence = {
        "_id": x["_id"],
        "name": x["name"],
        "age": x["age"],
        "gender": x["gender"],
        "balance": x["balance"],
        "email": x["email"],
        "phone": x["phone"],
        "isActive": x["isActive"]
    }
    listUsers.append(intelligence)
#     наполнить список


# Пункт №2.
# Отсортировать полученные данные по полю isActive, записать полученный результат в файл result.txt
f = open('result.txt', 'w')
listUsers.sort(key=lambda row: row["isActive"])
text = str(listUsers)
f.write(text)
f.close()
print(listUsers)
# создать файл,
# отсортировать файл,
# перевести список в строку,
# записать,закрыть файл.

# 3.
# Отсортировать по возрастанию balance только активных пользователей, записать полученный результат в файл result.txt
f = open('result.txt', 'w')
listUsers.sort(key=lambda row: row["balance"], reverse=True)
text = str(listUsers)
f.write(text)
f.close()
print(listUsers)
for x in listUsers:
    print(x)

