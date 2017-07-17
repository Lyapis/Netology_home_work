import requests
import os


def lang_file_in(input_folder, text_file):
    with open(os.path.join(input_folder, text_file), encoding='utf-8') as f:
        text = f.read()
        lang_in = text_file[0:2].lower()
    return text, lang_in


def tr(input_folder = input('Введите путь к исх. файлу: '), output_folder = input('Введите путь к кон. файлу: '),
 lang_out='ru'):
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    key = 'trnsl.1.1.20170717T203129Z.0f54dfb5d234ccc4.de45858071dd7d42f5224b151ba13974dd704ec2'
    for lang_file in os.listdir(input_folder):
        text, lang_in = lang_file_in(input_folder, lang_file)
        params = {
        'key': key,
        'lang': f'{lang_in}-{lang_out}',
        'text': text
            }
        response = requests.get(url, params=params).json()
        translate_text = ' '.join(response.get('text', []))

        with open(os.path.join(output_folder, f'{lang_file[0:2]}-{lang_out.upper()}.{lang_file[3:]}'), 'w',
             encoding='utf-8') as fw:
             fw.write(translate_text)


tr()
tr(lang_out='it')
