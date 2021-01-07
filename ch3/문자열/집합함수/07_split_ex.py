
birth = input('input your birth(yyyy/mm/dd) : ')
birth_split = birth.split('/')

print('당신은 %s년에 태어났고' % birth_split[0] + '\n' +
      '생일은 %s월 %s일 이군요' % (birth_split[1], birth_split[2]) )