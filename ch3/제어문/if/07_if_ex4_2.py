# 연습문제 4_2

figure = input('what is your figure type(1 : rectangular, 2 : triangle, 3 : circle) : ')

if figure == '1' or '2' or '3' :
    if figure == '1' :
        w = int(input('width : '))
        h = int(input('height : '))
        area = w * h
        shape = 'rectangular'

    elif figure =='2' :
        b = int(input('bottom : '))
        h = int(input('height : '))
        area = b * h /2
        shape = 'triangle'

    else  :
        r = int(input('radius :'))
        area = 3.14 * r * r
        shape ='circle'
    print('area of %s = %.2f' % (shape, area))

else :
    print('please input number')



