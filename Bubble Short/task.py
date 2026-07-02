def bubble_sort(numbers_list,key = 'transaction_amount'):
    size = len(numbers_list)
    
    for i in range(size -1):
        swapped = False
        for j in range(size-1-i):
            if numbers_list[j][key] > numbers_list[j + 1][key]:
                tmp = numbers_list[j]
                numbers_list[j] = numbers_list[j+ 1]
                numbers_list[j + 1] = tmp
                swapped = True
        if swapped is False:
            break

if __name__ == '__main__':
    # numbers_list = ["Urvashi","Chetan","Darnisha","Anjali"]
    
    
    numbers_list = [
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
        ]
        
    bubble_sort(numbers_list,'transaction_amount')
    bubble_sort(numbers_list,'name')
    print("numbers_list after sorting :: ",numbers_list)