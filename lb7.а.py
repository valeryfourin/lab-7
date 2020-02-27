while True:
    n=int(input('Input a number of symbols: '))
    a=str()
    for i in range(n):
        a+=input(f'Input a {i} symbol: ')
    a=set(a)
    b=0
    for i in a:
        if i=='+' or i=='-' or i=='*': b+=1
    print(b)
    answer = input('Restart? Yes-1, No-2 ')
    if answer == '1':
        continue
    else:
        break

