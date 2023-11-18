def check_string_brackets(text):
    counter_1 = 0
    counter_2 = 0
    for word in text:
        if word == '(':
            counter_1 += 1
        if word == ')':
            counter_2 += 1
    if counter_1 == counter_2:
        print('YES')
    else:
        print('NO')


check_string_brackets(input('Введи скобочки'))    