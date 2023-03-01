import flash_card_functions as fc
import random as r
from PIL import Image

f= open(input('Hello, what text file are we studying today? '))
print('\n \n')

dic = fc.qa_to_dic(f)
n = len(dic)
n_lst = fc.num_list(n)
next_command = ''
while n_lst != []:
    if next_command == '':
        i = r.choice(n_lst)
        print('Q: ' + dic[i][0])
        a = input('A: ')
        print('\nHere is your answer: \n' + a +'\n' + 'Here is the provided answer:\n' + dic[i][1])
        n_lst.remove(i)
        print('\n')
        next_command = input("Press 'Enter' or type 'Retry' to continue.  \n")
    else:
        if next_command == 'Retry':
            n_lst.append(i)
        next_command = input("Press 'Enter' to continue.  \n")