my_list = [44,4345,435,4565,6768,23]

even = []
for i in my_list:
    if i%2 == 0:
        even.append(i)

sum_num = 0
for i in even:
    sum_num +=i
    
print('The sum of even numbers', sum_num)