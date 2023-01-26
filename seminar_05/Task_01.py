# 1. Напишите программу, удаляющую из текста все слова, 
# содержащие "абв". В тексте используется разделитель пробел.

from random import sample

def List_num_rand(count: int, alp: str = 'абв'):
    num_List = []
    for i in range(count):
        letters = sample(alp, k=3)
        num_List.append(''.join(letters))
    return ' '.join(num_List)

def simple_sentence(words: str) -> str:
    return " ".join(i for i in words.split() if i !='абв')

all_list = List_num_rand(int(input('Rоличество слов: ')))
print(all_list)
print(simple_sentence(all_list))

