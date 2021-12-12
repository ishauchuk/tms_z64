
print('''\nThere is a riddle as they say "from Steve Jobs." 
There are 2 buckets, one 3 liters, the other 5 liters and unlimited water. 
	
You can:
1. Collect water in any bucket. command: 'fill_up'
2. Pour water out of any bucket. command: 'discharge'
3. Transfer water from one bucket to another. 'transfuse'

Example command for input:
>>> transfuse, bucket_3
What does this command mean? Transfer the water from a three-liter 
bucket to another bucket

The user wins if he manages to get exactly 4 liters.''')

buck_3 = 0
buck_5 = 0
buck_3_const = 3
buck_5_const = 5
counter = 0

while True:
	action = {
				'fill_up': 'fill_up',
				'discharge': 'discharge',
				'transfuse': 'transfuse',
				}

	bucket = {
				'bucket_3': 'bucket_3',
				'bucket_5': 'bucket_5',
				}

	user_input=input('Enter action, enter bucket:\n')
	if user_input == 'exit':
		break
	user_input = user_input.split(', ')
	chose_a = user_input[0]
	chose_b = user_input[1]

	if action.get(chose_a) == 'fill_up':
		if bucket.get(chose_b) == 'bucket_3':
			if buck_3 < buck_3_const:
				buck_3 = buck_3_const
		if bucket.get(chose_b) == 'bucket_5':
			if buck_5 < buck_5_const:
				buck_5 = buck_5_const

	if action.get(chose_a) == 'discharge':
		if bucket.get(chose_b) == 'bucket_3':
			buck_3 = 0
		if bucket.get(chose_b) == 'bucket_5':
			buck_5 = 0

	if action.get(chose_a) == 'transfuse':
		if bucket.get(chose_b) == 'bucket_3':
			spare_5 = buck_5_const - buck_5
			if buck_3 <= spare_5:
				buck_5 += buck_3
				buck_3 = 0
			if buck_3 > spare_5:
				buck_5 = buck_5 + spare_5
				buck_3 = buck_3 - spare_5
		if bucket.get(chose_b) == 'bucket_5':
			spare_3 = buck_3_const - buck_3
			if buck_5 <= spare_3:
				buck_3 += buck_5
				buck_5 = 0
			if buck_5 > spare_3:
				buck_3 = buck_3 + spare_3
				buck_5 = buck_5 - spare_3

	counter += 1
	print(f"Current result: Bucket 3L:{buck_3}, Bucket 5L:{buck_5}. \n\
		This is {counter} step.")
	# print(f"This is {counter} step")

	if buck_5 == 4:
		print("You win!!!")
		break