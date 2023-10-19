# 1.Using the given list, 
# print out a filtered version of the list 
# with only the numbers that are less than ten
alist = [1,11,14,5,8,9]
for num in alist:
    if num < 10:
        print(num)
print('\n')

# 2.Merge and sort the two lists below
# Hint: You can use the .sort() method
list1 = [1,2,3,4,5,6]
list2 = [3,4,5,6,7,8,10]

merge_list = list1 + list2
merge_list.sort()
print(merge_list)

# 3. Square every number from 1 to 15
squared_num = []
for i in range(1, 16):
    squared_num = i**2
    print(f"{i} squared is {squared_num}")


# 4.Using List Comprehension and the given list, 
# print out a filtered list with only 
# the names that start with the letter 'a'. 
# The names in the outputted list should be title cased and 
# have no whitespace.
names_list = ['   amy', 'Briant', 'Ryan ', ' Alex', 'steve', '  ']

filtered_list = [name.strip().title() #name.strip().title() is used to remove whitespace and title case
                for name in names_list
                if name.strip() and name.strip()[0].lower()=='a' 
                #name.strip()[0].lower()=='a' - checks if the first character of the name, after strippin
                #whitespace and converting to lowercase, is 'a'
]
print(filtered_list)
print("\n")

# 5.Print all Prime numbers from 1 to 100
# define a list of prime numbers is empty list.
prime_num = []

#Iterate fril 2 to 100
for i in range(2, 101):
    
    #check if the number is divisible by any number from 2 to its square root.
    for j in range(2, int(i**0.5)+1):
        if i % j ==0:
            break
    #if the number is not divisible by any number from 2 to its square root, it is a prime number
    else:
        prime_num.append(i)

#print the prime number
print(prime_num)






