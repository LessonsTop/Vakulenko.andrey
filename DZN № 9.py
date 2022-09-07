from peewee import *
# """подключение модуля управления базами данных"""
def main():
    db = PostgresqlDatabase("DZN9.", user='postgres', password=12345)
# """Установить соединение с базой данных """
    class BaseModel(Model):
        class Meta:
            database = db

    class City(BaseModel):
        city = CharField()
        street = CharField()
        number_house = CharField()

    class Country(BaseModel):
        country = CharField()
        city = ForeignKeyField(City, backref='Country')


    db.connect()
# """подключение к базе данных"""
    db.create_tables([City, Country])
# """Создать таблицы City,Coutry ,наполнить их""""

    moscow = City.create(city="Moscow",street="Leninskiy", number_house='26')
    sanktpeterburg = City.create(city="sanktpeterburg", street="Nevskiy", number_house='22/1')
    sochi = City.create(city="sochi", street="lenina", number_house='1')
    russia = Country.create(country="Russia", city=1)
    russia = Country.create(country="Russia", city=2)
    russia = Country.create(country="Russia", city=3)


    comb = Country.select().join(City)
# """соединить данные таблиц"""
    for w in comb:
        print(w.country, w.city.city, w.city.street, w.city.number_house)
        # """Вывести данные"""

if __name__ == '__main__':
    main()

