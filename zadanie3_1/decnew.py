import chardet
import json


def input_file_name():
    file_name = input('Введите имя файла: ')
    return file_name


def encoding_file():
    file_name = input_file_name()
    with open(file_name, 'rb') as f:
        data = f.read()
        result = chardet.detect(data)
    return file_name, result['encoding']


def list_dict():
    file_name, cod_name = encoding_file()
    with open(file_name, encoding=cod_name) as fin:
        data = json.load(fin)
        info = data['rss']['channel']['items']
    return info


def generate_list():
    d_full = []
    for i in list_dict():
        d_full += (i['description'] + ' ' + i['title']).split()
    d_full = [i for i in d_full if len(i) > 6]
    return d_full


def main():
    dy = {}
    for i in generate_list():
        dy[i] = dy.get(i, 0) + 1
    print('{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}'.format(*sorted(dy.items(),
        key=lambda x: x[1], reverse=True)))


main()