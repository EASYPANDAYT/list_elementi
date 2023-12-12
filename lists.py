# коллекция - много в одном
# коллекции состоят из элементов
# индексирован
# изменяем
# len - считает по пальцам
# apppend - присоеденит в конец
# insert - добавить по индексу
# список[0] = 'Петя' - замена элемента
# pop - удаляет элемент и возвращает его (может и по индексу) | surname = hero.pop()
# in - есть ли элемент в списке |  print('Вася' in hero)
# sort - сортирует список
# сортируем только однородные (type) списки
# for - перебирает все элементы
'''
hero = [1, 2, 3, 10, 20, 1, 2, 3]

counter = 0
while counter < len(hero):
    print(hero[counter])
    counter += 1
'''
'''
for element in [1, 2, 3, 4]:
    print('Привет', element)
'''
from random import randint
random_digits = []
for i in range(10):
    random_digits.append(randint(0, 9))
print(random_digits)