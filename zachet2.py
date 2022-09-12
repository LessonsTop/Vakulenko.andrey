"""
TODO 1. Очистить и наполнить базу данных данными из класса(данные предоставлены ниже в списках)
TODO 2. Получить данные из БД и записчать их в JSON
Доп. подсказки:
1. База данных прилагается и называется bank.db
2. Классы изменять не нужно
3. Основня структура есть
"""

from MegaClass import Account
from db import *
import json

"""Подключить  файл базы данных bank.db через SQL lite"""

def main():
    listNames = ["Valera", "Artem", "Kolya", "Petya", "Kostya"]
    listNumbers = ["+7-903-800-00-00", "+7-908-222-80-00", "+79000002121", "89003211234", "89077077070"]
    listEmail = ["test@test.ru", "artem@gmail.com", "kolya@mail.ru", "petya@yandex.ru", "kostya@rambler.ru"]
    listBalance = [1000, 3450, 980, 1250, 398]
    sqlConnect.connect()
    sqlConnect.create_tables([AccountDb])

    account1 = Account("Valera", "+7-903-800-00-00", "test@test.ru", 1000)
    users = AccountDb.create(account=account1.accountName, phone=str(account1.phone), email=account1.email,
                             balance=account1.balance)
    users.save()
    users = users.select()

    account1 = Account('Artem', '+7-908-222-80-00', 'artem@gmail.com', 3450)
    users = AccountDb.create(account=account1.accountName, phone=str(account1.phone), email=account1.email,
                             balance=account1.balance)
    users.save()
    users = users.select()

    account1 = Account('Kolya', '+7-90000002121', 'kolya@mail.ru', 980)
    users = AccountDb.create(account=account1.accountName, phone=str(account1.phone), email=account1.email,
                             balance=account1.balance)
    users.save()
    users = users.select()

    account1 = Account('Petya', '+89003211234', "petya@yandex.ru", 1250)
    users = AccountDb.create(account=account1.accountName, phone=str(account1.phone), email=account1.email,
                             balance=account1.balance)
    users.save()
    users = users.select()

    account1 = Account('Kostya', '+89077077070', "kostya@rambler.ru", 398)
    users = AccountDb.create(account=account1.accountName, phone=str(account1.phone), email=account1.email,
                             balance=account1.balance)
    users.save()
    users = users.select()
    for records in users.tuples().iterator():
        print(records)
    # for v in records:
    #     print(v)

# """Получить данные из БД и записать их в JSON"""

# name1 = (1,"Valera", '+7-903-800-00-00', 'test@test.ru', 1000)
# name2 = (2,"Artem", '+7-908-222-80-00', 'artem@gmail.com', 3450)
# name3 = (3,"Kolya", '+7-90000002121', 'kolya@mail.ru', 980)
# name4 = (4,"Petya", '+89003211234', 'petya@yandex.ru', 1250)
# name5 = (5,"Kostya", '+89077077070', 'kostya@rambler.ru', 398)
# listName = [name1,name2,name3,name4,name5]
# write = json.dumps(listName,indent=4)
# f = open("name.json","w")
# f.write(write)
# f.close()
# f = open("name.json","r")
# readJSON = f.read()
# f.close
# print(readJSON)

# if __name__ == '__main__':
#     main()


