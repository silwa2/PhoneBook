# Мы создали класс с именем Contact, который принимает два обязательных параметра, 
# name и contact_number.
# Помимо этих двух, он также принимает три необязательных параметра: 
# position, date_createdи date_updated. 
# Если эти три необязательных параметра не переданы, 
# по умолчанию для них используются текущий индекс и текущее время соответственно.
# Кроме того, мы определили __repr__метод, который возвращает объект в более удобочитаемом виде.



import datetime

class Contact:
    def __init__ (self, name, contact_number, position=None, date_created=None, date_updated=None):
        self.name = name
        self.contact_number = contact_number
        self.position = position
        self.date_created = date_created if date_created is not None else datetime.datetime.now().isoformat()
        self.date_updated = date_updated if date_updated is not None else datetime.datetime.now().isoformat()

    def __repr__ (self) -> str:
        return f"({self.name}, {self.contact_number}, {self.position}, {self.date_created}, {self.date_updated})"
