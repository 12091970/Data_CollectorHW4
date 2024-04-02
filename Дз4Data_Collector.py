"""Выберите веб-сайт с табличными данными, который вас интересует.
Напишите код Python, использующий библиотеку requests для отправки HTTP GET-запроса на сайт и получения HTML-содержимого страницы.
Выполните парсинг содержимого HTML с помощью библиотеки lxml, чтобы извлечь данные из таблицы.
Сохраните извлеченные данные в CSV-файл с помощью модуля csv.

Ваш код должен включать следующее:

Строку агента пользователя в заголовке HTTP-запроса, чтобы имитировать веб-браузер и избежать блокировки сервером.
Выражения XPath для выбора элементов данных таблицы и извлечения их содержимого.
Обработка ошибок для случаев, когда данные не имеют ожидаемого формата.
Комментарии для объяснения цели и логики кода.

Примечание: Пожалуйста, не забывайте соблюдать этические и юридические нормы при веб-скреппинге."""


  




import requests
from lxml import html
import csv

"""def get_result():
    response = requests.get("http://cbr.ru")
    return response.text

print(get_result()) """     #получаем html

url = "https://www.worldathletics.org/records/toplists/sprints/60-metres/indoor/women/senior/2023?page=1"
response = requests.get(url, headers = {
   'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) \
   AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/17.2.1'})

tree = html.fromstring(response.content) #обрабатываем ответ при помощи lxml
table_rows = tree.xpath("//table[@class='records-table']/tbody/tr")
#строки таблицы класса...
columns = table_rows[0].xpath(".//td/text()") #извлечение данных 1й строки

for col in columns:
   print(col)
   print('(-------------------------------)')


with open('data.csv','w',newline='', encoding='utf-8') as f:
  csv_write = csv.writer(f)
  
  for col in columns:
        csv_write.writerow(col)    #запись в csv


for col in columns:
  if col:
    print("OK")
  else:
    print(" Не OK")
  














      
  
