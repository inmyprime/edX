trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si',
          '5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi'}

def convert_to_mandarin(us_num):
    '''
    us_num, a string representing a US number 0 to 99
    returns the string mandarin representation of us_num
    '''
    digits = int(us_num)
    first = digits // 10
    second = digits % 10

    if digits <= 10:
        mandarin = trans[str(digits)]
    elif digits <= 19:
        mandarin = trans['10'] + ' ' + trans[str(second)]
    elif second == 0:
        mandarin = trans[str(first)] + ' ' + trans['10']
    else:
        mandarin = trans[str(first)] + ' ' + trans['10'] + ' ' + trans[str(second)]

    return mandarin

print(convert_to_mandarin('36'))
print(convert_to_mandarin('20'))
print(convert_to_mandarin('16'))
print(convert_to_mandarin('0'))
print(convert_to_mandarin('10'))
