Python 3.0.1 (r301:69561, Feb 13 2009, 20:04:18) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import copy
import math

students = [
    {'name':'Александр',  'family':'Филипенко', 'gender':'муж', 'experience':False, 'DZ':[9,9,10,10,9], 'exam':9},
    {'name':'Алексей', 'family':'Пидручный', 'gender':'муж', 'experience':False, 'DZ': [10,8,9,10,10], 'exam':10},
    {'name':'Олег', 'family':'Глыба', 'gender':'муж', 'experience':False, 'DZ': [7,7,6,9,8], 'exam':8},
    {'name':'Екатерина',  'family':'Любовная', 'gender':'жен','experience':True, 'DZ': [6,7,8,9,10], 'exam':9},
    {'name':'Люсия',  'family':'Набережная', 'gender':'жен',  'experience':False, 'DZ': [6,5,6,8,7], 'exam':7},
    {'name':'Виктор',  'family':'Пряничный', 'gender':'муж',  'experience':True, 'DZ': [10,9,10,8,10], 'exam':10},
    {'name':'Виктория', 'family':'Сахарная', 'gender':'жен','experience':False, 'DZ': [6,5,6,5,7], 'exam':6},
    {'name':'Елена', 'family':'Капризная', 'gender':'жен', 'experience':False, 'DZ': [8,10,10,9,10], 'exam':10},
    {'name':'Виктор',  'family':'Пряничный', 'gender':'муж',  'experience':False, 'DZ': [6,7,9,8,9], 'exam':8},
]

#TODD1

def get_exam_average_rating(st):
 aver_exam=0
 summ_exam=0
 rate=0
 for person in st:
  summ_exam+=int(person['exam'])
  rate += 1
  aver_exam=summ_exam/rate
  return aver_exam

def get_group_average_rating(st):
 aver_rate=0
 sum_rate=0
 rate=0 
 for person in st:
  for i in person['DZ']:
    sum_rate+=int(i)
    rate += 1
  aver_rate=sum_rate/rate
 return aver_rate

def main_1():
     av_rate=get_group_average_rating(students)
     print('Средняя оценка за домашние задания по группе: {0}'.format(av_rate))
     ex_rate=get_exam_average_rating(students)
     print('Средняя оценка за экзамен: {0}'.format(ex_rate))
 
main_1()
 
#TODD3

def get_integral_grad(persn):
    grad=float(0)
    grad=round(0.6*get_aver_DZ(persn)+0.4*int(persn['exam']),2)
    print('с интегральной оценкой ', grad)
    return grad

def get_aver_DZ(pers):
    aver_hw=0
    summ_hw=0
    rate=0
    for i in pers['DZ']:
        summ_hw+=int(i)
        rate += 1

    aver_hw=summ_hw/rate
    print(pers['name'], pers['family'],':','оценок =',rate,',сумма оценок =',summ_hw,',средний бал за домашку =', aver_hw)
    return aver_hw
    

def get_best_stud (st):
    best_students= [float(0)]
    new_integral_grad=float(0)
    for person in st:
        new_integral_grad=get_integral_grad(person)
        if new_integral_grad > best_students[0]:
            best_students.clear()
            best_students.append(new_integral_grad)
            best_students.append(person['name'] + ' '+ person['family'])
        elif new_integral_grad == best_students[0]:
            best_students.append(person['name'] + ' '+ person['family'])

    return best_students


def main_2():
    best_list=[]
    quantity=0
    best_list=get_best_stud(students)
    quantity=len(best_list)
    if quantity == 2:
        print('Лучший студент: {0} с интегральной оценкой {1}'.format(best_list[1], best_list[0]))
    else:
        print('Лучшие студенты:')
        for i in best_list[1::]:
            print(i)
        print('с интегральной оценкой {0}'.format(best_list[0]))

main_2()
