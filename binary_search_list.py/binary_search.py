import  math
def linear_search(number_list,number_to_find):
    for index,element in enumerate(number_list):
        if element == number_to_find:
            return index
    return -1
    
def binary_search(number_list,number_to_find):
    start = 0
    end = len(number_list) -1
    mid =(start + end)//2
    
    while start <= end:
        if number_list[mid] == number_to_find:
            return mid
        elif number_list[mid] < number_to_find:
            start = mid + 1
        else:
            end = mid - 1
        
        mid = (start + end)//2
    
    return -1

def binary_search_recursive(number_list,number_to_find,start,end):
    if start > end:
        return -1
    mid = (start + end)//2

    if number_list[mid] == number_to_find:
        return mid
    elif number_list[mid] < number_to_find:
        return binary_search_recursive(number_list,number_to_find,mid+1,end)
    else:
        return binary_search_recursive(number_list,number_to_find,start,mid-1)

def find_all_occurances(numbers, number_to_find):
    index = binary_search(numbers, number_to_find)
    indices = [index]
    # find indices on left hand side
    i = index-1
    while i >=0:
        if numbers[i] == number_to_find:
            indices.append(i)
        else:
            break
        i = i - 1

    # find indices on right hand side
    i = index + 1
    while i<len(numbers):
        if numbers[i] == number_to_find:
            indices.append(i)
        else:
            break
        i = i + 1

    return sorted(indices)


if __name__ == '__main__':
    numbers = [1,4,6,9,11,15,15,15,17,21,34,34,56]

    print(f"Number found at index ::  {binary_search(numbers,15)} :: using binary search")
    print(f"Number found at index :: {binary_search_recursive(numbers,15,0,len(numbers)-1)} :: using binary search recursive")
    print(f"All occurrences of number found at indices :: {find_all_occurances(numbers,15)}")