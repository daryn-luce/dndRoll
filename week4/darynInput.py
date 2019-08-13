import daryn

equation = input('Enter equation 3 * 3, 1 / 4, 2 + 2\n').split()
if len(equation) == 3:
    if equation[1] == '+':
        print(' '.join(equation),f'= {daryn.add_num(int(equation[0]),int(equation[2]))}')
    elif equation[1] == '-':
        print(' '.join(equation),f'= {daryn.sub_num(int(equation[0]),int(equation[2]))}')
    elif equation[1] == '*':
        print(' '.join(equation),f'= {daryn.mult_num(int(equation[0]),int(equation[2]))}')
    elif equation[1] == '/':
        print(' '.join(equation),f'= {daryn.div_num(int(equation[0]),int(equation[2]))}')