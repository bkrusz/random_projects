def binary_search(array, target):
    min_array = 0
    max_array = len(array) - 1
    guess = 0
    while(not(max_array < min_array)):
        guess = int((min_array + max_array)/2)
        if(array[guess] == target):
            return guess
        elif(array[guess] < target):
            min_array = guess + 1
        else:
            max_array = guess - 1
    return -1

array = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

print(len(array))

search_result_1 = binary_search(array, 12)
search_result_2 = binary_search(array, 3)
search_result_3 = binary_search(array, 0)

print('Search result for 12: ' + str(search_result_1))
print('Search result for 29: ' + str(search_result_2))
print('Search result for 0: ' + str(search_result_3))