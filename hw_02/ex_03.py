# Напишите проверку на то, является ли строка палиндромом. Палиндром — это 
# слово или фраза, которые одинаково читаются слева направо и справа налево.

palindrom = 'Лёша на полке клопа нашёл'
palindrom = ''.join(palindrom.lower().split())
if palindrom == palindrom[::-1]:
	print("yes, it is palindrom")
else:
	print("no, it isn't palindrom")