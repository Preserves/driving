country = input('請問你是哪國人: ')
age = int(input('輸入你的年齡: '))
if country == '台灣':
    if age >= 18:
        print('你可以考駕照')
    else:
        print('你還不能考駕照')