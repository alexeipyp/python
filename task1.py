#Восстановление русского языка для строки, набранной на английском
#Входящее значение принимается из аргумента командной строки
import sys

if len(sys.argv) > 1:
	print(sys.argv[1].translate(dict(zip(map(ord,
		"qwertyuiop[]asdfghjkl;'zxcvbnm,.&/6"
		'QWERTYUIOP{}ASDFGHJKL:"ZXCVBNM<>&?^'),
		"йцукенгшщзхъфывапролджэячсмитьбю?.6"
		'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ?,:'))
	))


