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



if __name__ == '__main__':
    numbers = [4,6,9,11,15,19,22,27,31,36,40]

    print(f"Number found at index ::  {binary_search(numbers,4)} :: using binary search")
    print(f"Number found at index :: {binary_search_recursive(numbers,4,0,len(numbers)-1)} :: using binary search recursive")