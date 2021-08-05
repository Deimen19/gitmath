from colorama import init
from colorama import Fore, Back, Style

init()

print( Fore.BLACK )
print(Back.GREEN)

what=input('Что делать (+ -) ')
print( Back.CYAN )
a=float(input('Веди первое число '))
b=float(input('Веди второе число '))

print ( Back.YELLOW )

if what == '+':
	c=a+b
	print('Результат '+str(c))
elif what=='-':
	c=a-b
	print('Результат '+str(c))

input()


