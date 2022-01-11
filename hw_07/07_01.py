"""
Есть архив с книгами, необходимо сделать программу помощник читателя, прошу 
использовать ООП. Программа должна принять от пользователя слово или некоторое 
количество слов, в ответ программа должна выдать все названия книг в тексте 
которых есть все введенные пользователем слова.
"""

import chardet
import os

wordcheck = input('Enter words separated by commas without spaces: \n')
wordcheck = wordcheck.replace(' ', '').split(',')
path = ".\\books"
dict_code = {}


def reading(wordcheck):
    with open(os.path.join(path, filename),
              encoding=dict_code.get('filename')) as file:
        flag = 1
        flag_sum = 0
        file_read = file.read()
        for i in range(len(wordcheck)):
            if wordcheck[i] in file_read:
                flag_sum += 1
            if flag_sum == len(wordcheck):
                print(f'{filename[:-4].replace("__", " - ")}')


for root, dirs, files in os.walk(path):
    for filename in files:
        try:
            reading(wordcheck)

        except UnicodeDecodeError:
            with open(os.path.join(path, filename), 'br') as file:
                data = file.read()
                dict_code['filename'] = chardet.detect(data)['encoding']
                reading(wordcheck)
