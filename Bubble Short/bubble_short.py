def bubble_sort(numbers_list):
    size = len(numbers_list)
    
    for i in range(size -1):
        swapped = False
        for j in range(size-1-i):
            if numbers_list[j] > numbers_list[j + 1]:
                tmp = numbers_list[j]
                numbers_list[j] = numbers_list[j+ 1]
                numbers_list[j + 1] = tmp
                swapped = True
        if swapped is False:
            break

if __name__ == '__main__':
    numbers_list = ["Urvashi","Chetan","Darnisha","Anjali"]
    bubble_sort(numbers_list)
    print("numbers_list after sorting :: ",numbers_list)