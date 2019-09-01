'''
4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20,
inclusive .

4-4. One Million: Make a list of the numbers from one to one million, and then
use a for loop to print the numbers . (If the output is taking too long, stop it by
pressing ctrl-C or by closing the output window .)

4-5. Summing a Million: Make a list of the numbers from one to one million,
and then use min() and max() to make sure your list actually starts at one and
ends at one million . Also, use the sum() function to see how quickly Python can
add a million numbers .

4-6. Odd Numbers: Use the third argument of the range() function to make a list
of the odd numbers from 1 to 20 . Use a for loop to print each number .

4 -7.  Threes: Make a list of the multiples of 3 from 3 to 30 . Use a for loop to
print the numbers in your list .

4-8. Cubes: A number raised to the third power is called a cube . For example,
the cube of 2 is written as 2**3 in Python . Make a list of the first 10 cubes (that
is, the cube of each integer from 1 through 10), and use a for loop to print out
the value of each cube .

4-9. Cube Comprehension: Use a list comprehension to generate a list of the
first 10 cubes .
'''

# 4-3
for number in range(1,21):
    print(number)

# 4-4
one_million = []
for number in range(1,10000001):
    one_million.append(number)
# for i in one_million:
#    print(i)

# 4-5
print(max(one_million))
print(min(one_million))

# 4-6
for number in range(1,21,2):
    print(number)

# 4-7
threes = []
for number in range(3,33,3):
    threes.append(number)
print(threes)

# 4-8
cubes = []
for number in range(1,11):
    cubes.append(number**3)
print(cubes)

# 4-9
cubes_list_com = [number**3 for number in range(1,11)]
print(cubes_list_com)
