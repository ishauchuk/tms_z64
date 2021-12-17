# Вы принимаете от пользователя последовательность чисел, разделённых запятой. 
# Составьте список и кортеж с этими числами.

seq_num = input("Enter a sequence of numbers separated by commas: ").split(',')

print(f"List: {list(map(int, seq_num))}\nTuple: {tuple(map(int, seq_num))}")