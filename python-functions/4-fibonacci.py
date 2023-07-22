def fibonacci_sequence(n):
    list = []
    n1, n2 = 0, 1
    count = 0
    if n == 0:
       return list 
    else:
        while count < n:
            list.append(n1)
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1
        return list