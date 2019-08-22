def solution(number):
    i = 0
    sum = 0
    list = [x for x in range(1, number) if x % 3 == 0 or x % 5 == 0]
    while i < len(list):
        sum+=list[i]
        i+=1
    return sum