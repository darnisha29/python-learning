# read the values from the file 
# What was the average temperature in first week of Jan
# What was the maximum temperature in first 10 days of Jan
# arr = []
# with open('Hast Table/nyc_weather.csv', 'r') as f:
#     lines = f.readlines()
#     for line in lines:
#         token = line.strip().split(',')
#         try:
#             temperature = int(token[1])
#             arr.append(temperature)
#         except:
#             print("Error: Invalid temperature value in the file.")

# max_temperature = max(arr)
# print("Maximum temperature recorded in January:", max_temperature)
# avg_temperature = sum(arr[0:7])/len(arr[0:7])
# print("Average temperature for the first week of January:", avg_temperature)


# 
arr = {}
with open("Hast Table/nyc_weather.csv",'r') as f:
    lines = f.readlines()
    for line in lines:
        token = line.strip().split(',')
        try:
            arr[token[0]] = int(token[1])
        except:
            print("Error: Invalid temperature value in the file.")

print(arr)
print("Temperature on Jan 9 :: ", arr['Jan 9'])
print("Temperature on Jan 4 :: ", arr['Jan 4'])