from sys import argv
import re

def num_format(number):
    l, r = number.split('\\')
    return ''.join(['0']*(4-len(l))) + l + '\\' + ''.join(['0']*(5-len(r))) + r

def get_good_numbers(inpurt_string):
    specials = re.findall(r'(\D|\A)([0-9]{2,4}\\[0-9]{2,5})(\D|\Z)', inpurt_string)
    return list(map(lambda x: num_format(x[1]), specials))


inpurt_string = ' '.join(map(str, argv[1:]))
#inpurt_string = 'Адрес 5467\\456. Номер 405\\549'

good_numbers = get_good_numbers(inpurt_string)

for n in good_numbers:
    print(n)