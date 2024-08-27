def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print('Функция с параметрами по умолчанию')
print_params(b=25)
print_params(c=[1, 2, 3])
print()

print('Распаковка параметров: ')
values_list = [1405, 213123, 12312312]
print_params(*values_list)
values_dict = {'a':333, 'b':555, 'c':666}
print_params(**values_dict)
print()

print('Распаковка + отдельные параметры')
values_list_2=['qweqweq', 3423]
print_params(*values_list_2, 42)