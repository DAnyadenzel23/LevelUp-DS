#1.1 Приветствие пользователя:
name = input('Введите Ваше имя: ')
print(f'Добро пожаловать, {name}!')

#1.2 Любимая цитата:
phrase, author = input('Введите фразу: '), input('Введите автора: ')
print(f'{phrase} -  {author}') 

#1.3 Повторение строки:
word = input('Ввод слова: ')
num = int(input('Введите число: '))
print(word*num)

#1.4 Случай с текстом:
phrase_1 = input('Введите фразу: ')
print(phrase_1.lower(),phrase_1.upper())


#2.1 Простой калькулятор площади прямоугольника:
width = input('Введите ширину, см: ')
height = input('Введите высоту, см: ')
S = float(height.replace(',', '.')) * float(width.replace(',', '.'))
print(f'Площадь прямоугольника: {S} кв.см.')

#2.2 Возраст в месяцах:
old = input('Введите возраст: ')
print(f'Ваш возраст составляет примерно {12*int(old)} месяцев.')

#2.3 Условные операторы:
old_1 = input('Введите возраст: ')
name_2 = input('Введите Ваше имя: ')
if  int(old_1) >= 18 and not name_2 == "Иван":
    print('Доступ разрешен!')  
else: 
    print('Доступ запрещен!')    