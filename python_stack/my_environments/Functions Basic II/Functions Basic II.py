# countdown
def countdown(number): 
    new_list = []
    for x in range (number , -1 , -1):
        new_list.append(x)
    return new_list
print(countdown(5))
# ....................................
# Print and Returdef 
def print_and_return(numbers_list):
    print(numbers_list[0])
    return(numbers_list[1])
returned_val = print_and_return([1, 2])
print("The returned value is:", returned_val) 
# ....................................

# First Plus Length 
def first_plus_length (input_list):
    return input_list[0] + len(input_list)
result = first_plus_length([1, 2, 3, 4, 5])
print(result)
# ....................................

# Values Greater than Second
def values_greater_than_second(input_list):
    if len(input_list) < 2:
        return False
    second_value = input_list[1]
    new_list = []
    for value in input_list:
        if value > second_value:
            new_list.append(value)
    print("Number of values greater than the second:", len(new_list))
    return new_list

result1 = values_greater_than_second([5,2,3,2,1,4]) 

print("Returned list:", result1)
# ....................................

# This Length, That Value 
def length_and_value (size,value):
    new_list = []
    for _ in range (size):
        new_list.append(value)
    return new_list
result1 = length_and_value(4, 7)
print( result1) 