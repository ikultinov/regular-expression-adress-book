import re
from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv

with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
pprint(contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ
# ваш код
contacts_list.sort()
count = 1
for elem in contacts_list[1:]:
  if elem[-2]:
    pattern = r"(\+7|8)\s?\(?(\d{3})\)?[\s-]?(\d{3})[\s-]*(\d{2})[\s-]*(\d{2})"
    result = re.sub(pattern, r"+7(\2)\3-\4-\5", elem[-2])
    elem[-2] = result
    pattern_2 = r"(\+7|8)\s?\(?(\d{3})\)?[\s-]?(\d{3})[\s-]*(\d{2})[\s-]*(\d{2})\s\(?доб.\s(\d{4})\)?"
    result_2 = re.sub(pattern_2, r"+7(\2)\3-\4-\5 доб.\6", elem[-2])
    elem[-2] = result_2

  temp_elem = elem[:3]
  temp_1 = " ".join(temp_elem)
  temp_1 = temp_1.split()
  if len(temp_1) == 2:
    temp_1.append("")
  contacts_list[count] = temp_1 + elem[3:]
  count = count + 1

temp_list = contacts_list[0]
list_1 = []
contacts_list_2 = []
for item in contacts_list[1:]:
  if temp_list[0] == item[0] and temp_list[1] == item[1]:
    for i, data in enumerate(item):
      if data:
        list_1.append(data)
      else:
        list_1.append(temp_list[i])
    contacts_list_2.append(list_1)
    list_1 = []
  temp_list = item

for item in contacts_list:
  if not any(item[0] in sl for sl in contacts_list_2) and not any(item[1] in sl for sl in contacts_list_2):
    contacts_list_2.append(item)
contacts_list_2.sort()
contacts_list = contacts_list_2

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding="utf-8") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(contacts_list)
