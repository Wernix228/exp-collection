import random
#7_1
summ = 0
pw = 1
arr = [x for x in range(int(input("Введите длину массива: ")))]
for i in arr:
    if(i % 2 == 0):
        summ+=i
    else:
        pw *= i
print(summ,pw)

#7_2
arr = [x for x in range(int(input("Введите длину массива: ")))]
for i in arr:
    arr[arr.index(i)] = random.randint(1,1000)

print(arr)

min_index = arr.index(min(arr))
max_index = arr.index(max(arr))

arr[min_index], arr[max_index] = arr[max_index], arr[min_index]

print(arr)
# 12_1
arr = [x for x in range(int(input("Введите длину массива: ")))]
for i in arr:
    arr[arr.index(i)] = random.randint(1,1000)

print(arr)
nch = []
for i in arr:
    if i % 2 == 1:
        nch.append(i)
print(min(nch))
# 12_2
print("###############################")
arr1 = [x for x in range(10)]
for i in arr1:
    arr1[arr1.index(i)] = random.randint(1,1000)
print("arr1" , arr1)
arr2 = [x for x in range(10)]
for i in arr2:
    arr2[arr2.index(i)] = random.randint(1,1000)
print("arr2", arr2)
tmp = arr1
arr1 = arr2
arr2 = tmp
print(arr1,arr2)