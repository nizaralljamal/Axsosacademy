# Biggie Size
def biggie_size (input_list):
    for x in range (len(input_list)):
        if input_list[x]> 0 :
            input_list[x]= "big"
    return input_list   
input_list = [-1, 3, 5, -5]
print( biggie_size(input_list))
# ----------------------------------------------
# Count Positives 
def count_positives (input_list):
    positives_count = 0
    for number in input_list:
        if number > 0:
            positives_count += 1

    if len(input_list) > 0:
        last_index = len(input_list) - 1
        input_list[last_index] = positives_count
    return input_list
list1 = [-1,1,1]
print(count_positives(list1))

# ----------------------------------------------
# Sum Total 

def sum_total (input_list):
    total_sum = 0
    
    for number in input_list:
        total_sum += number
    return total_sum
list1 = [1, 2, 3, 4]
print(sum_total (list1))
# ----------------------------------------------
# Average
def average (input_list):
    if len(input_list) == 0:
        return 0
    total_sum = sum(input_list)
    avg = total_sum / len(input_list)
    return avg
list1 = [1, 2, 3, 4]
print(average(list1))

# ----------------------------------------------
# Length
def length (input_list):
    return len(input_list)
list1 = [37, 2, 1, -9]
print(length(list1))

def length (input_list):
    count = 0
    for item in input_list:
        count += 1
    return count
list1 = [37, 2, 1, -9]
print(length(list1))    
# ----------------------------------------------
# Minimum
def minimum (input_list):  
    if not input_list:
        return False
    min_value = input_list[0]
    for number in input_list:
        if number < min_value:
            min_value = number
    return min_value
list1 = [37,2,1,-9]
print(minimum(list1))        
# -----------------------------------
# Maximum
def maximum (input_list):
    if not input_list:
        return False
    maximum_value = input_list[0]
    for number in input_list:
        if number >maximum_value:
            maximum_value = number
        return maximum_value
list2 = [37,2,1,-9]
print(maximum(list2)) 
# -------------------------------------------
# Ultimate Analysis
def ultimate_analysis (input_list):
    if not input_list:
        return {}
    sum_total = 0
    min_value = input_list [0]
    max_value = input_list [0]
    for number in input_list:
        sum_total += number
        if number < min_value:
            min_value = number
        if number > max_value:
            max_value = number
        list_length = len(input_list)   
        average_value = sum_total / list_length
    return {'sumTotal': sum_total, 'average': sum_total / list_length, 'minimum': min_value, 'maximum': max_value}
list2 = [37,2,1,-9]
print(ultimate_analysis(list2))
# ----------------------------------------------
# Reverse List
def reverse_list (input_list):
    for i in range(len(input_list) // 2):
        opposite_index = len(input_list) - 1 - i
        input_list[i], input_list[opposite_index] = input_list[opposite_index],input_list[i]
    return input_list
list1 = [37, 2, 1, -9]
print(reverse_list(list1))
    


   
