even_numbers=[x for x in range(11) if x%2 == 0]
odd_numbers=[x for x in range(11) if not(x%2 == 0)]
not_2_and_3=[x for x in range(11) if not(x%3 == 0) and not(x%2 == 0)]
print("Even numbers:{0} Odd numbers:{1} Not /2 and /3:{2}".format(even_numbers,odd_numbers,not_2_and_3))