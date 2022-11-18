# Мы создали экземпляр класса TinyDB и передали ему имя файла. 
# Это создаст файл JSONcontact-book.json, в котором будут храниться наши данные. 
# Для извлечения данных из этой базы данных нам потребуется экземпляр класса Query из tinydbбиблиотеки.


from tinydb import TinyDB, Query

db = TinyDB('contact-book.json')
db.default_table_name = 'contact-book'
ContactQuery = Query()