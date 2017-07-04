#-*- coding: utf-8 -*-

import os

def return_path_to_file(file_name):
    path_to_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), file_name)
    return path_to_file

def get_list_of_all_sql_files_at_dir():
    list_of_all_sql_files = [file for file in os.listdir(return_path_to_file('Migrations'))
                             if file.endswith('.sql')]
    return list_of_all_sql_files

def find_file_by_keyword(keyword, list_of_all_sql_files):
    list_of_found_files = []
    for file_name in list_of_all_sql_files:
        with open(os.path.join(return_path_to_file('Migrations'), file_name), 'r') as f:
            data = f.read()
            if keyword in data:
                list_of_found_files.append(file_name)
    return len(list_of_found_files), list_of_found_files

def information_for_user():
    while True:
        print('Введите команду: s - start')
        command = input().lower()
        if command == 's':
            list_of_files = get_list_of_all_sql_files_at_dir()
            main_state = True
            while main_state:
                print('Введите слово для поиска:')
                keyword = input().upper()
                results = find_file_by_keyword(keyword, list_of_files)
                list_of_files = results[1]
                print('\nСтрока "{}" найдена в {} следующих файлах:\n'.format(keyword, results[0]))
                if results[0] == 1:
                    print('Файл, содержащий искомую строку найден.')
                    break
                elif results[0] == 0:
                    print('Файлы, содержащие строку не найдены.')
                    break
                if list_of_files:
                    print('\n'.join(list_of_files))
                print('\nВы хотите продолжить поиск в этом списке?(y/n)')
                question_command = input()
                if question_command == 'y':
                     continue
                else:
                    exit()
if __name__ == '__main__':
    information_for_user()