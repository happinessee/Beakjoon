# def sort(n, arr) :
#     answer = []
#     arr1 = arr

#     for i in range(n) :
#         tmp = 100001
#         for j in range(len(arr)) :
#             if (arr1[j][0] < tmp) :
#                 tmp = arr1[j][0]
#                 temp = arr1[j]

#             elif (arr1[j][0] == tmp) :
#                 if (arr1[j][1] < temp[1]) :
#                     temp = arr1[j]

#         answer.append(temp)
#         arr1.remove(temp)

#     return answer

# n = int(input())
# arr = []

# for i in range(n) :
#     arr.append(list(map(int, input().split())))

# result = sort(n = n, arr = arr)
# for i in range(n) :
#     print(result[i][0], result[i][1])

# 위의 문장으로는 시간 초과가 발생했다.

n = int(input())
arr = []
for i in range(n) :
    arr.append(list(map(int, input().split())))

arr.sort(key=lambda x: x[1])
arr.sort(key=lambda x: x[0])

for i in range(n) :
    print(arr[i][0], arr[i][1])