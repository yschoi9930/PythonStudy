
def show_keywards(**kwargs) :
    print('-----------------------')
    for key in kwargs.keys() :
        print(key, end=' ')
    print('\n')

    for val in kwargs.values() :
        print(val, end=' ')
    print('\n')

    for item in kwargs.items() :
        print(item)

show_keywards(id='sum', name = 'kim', phone = '010-1234-1234')

show_keywards(n1=2, n2=2, n3=3, n4=4)