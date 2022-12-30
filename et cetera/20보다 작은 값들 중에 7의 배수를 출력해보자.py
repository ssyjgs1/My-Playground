# 2022-04-22 Python Loop practice

# 20보다 작은 값들 중에 7의 배수를 출력하시오.(while 문으로 작성)

n=1
list = []
while n <= 20 :
    if n % 7 == 0 :
        list.append(n)
    n = n + 1
print(list)

# 20보다 작은 값들 중에 7의 배수를 출력하시오.(while 문으로 작성)

n=1
while n <= 20 :
    if n % 7 == 0 :
        print(n)
    n = n + 1