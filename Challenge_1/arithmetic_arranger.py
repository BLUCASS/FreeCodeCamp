def arranger():
    arranger = []
    func = {}
    correct = True
    while True:
        try:
            if len(arranger) > 5: raise MemoryError
            print('\033[32mType "=" in the operator to stop!\033[m')
            func['n1'] = int(input('First Number: '))
            if len(str(func['n1'])) > 4:
                raise IndentationError
            func['operator'] = str(input('Operator: '))
            if func['operator'] == '=': break
            if func['operator'] != '+' and func['operator'] != '-':
                raise ArithmeticError
            func['n2'] = int(input('Second number: '))
            if len(str(func['n2'])) > 4:
                raise IndentationError
            if func['operator'] == '+':
                func['result'] = func['n1'] + func['n2']
            elif func['operator'] == '-':
                func['result'] = func['n1'] - func['n2']
            arranger.append(func.copy())
        except IndentationError:
            print('\033[31mNumbers cannot be more than four digits.\nPROGRAM FINISHED\033[m')
            correct = False
            break
        except MemoryError:
            print('\033[31mToo many problems.\nPROGRAM FINISHED\033[m')
            correct = False
            break
        except ArithmeticError:
            print('\033[31mOperator must be "+" or "-".\nPROGRAM FINISHED\033[m')
            correct = False
            break
        except ValueError:
            print('\033[31mNumbers must only contain digits.\nPROGRAM FINISHED\033[m')
            correct = False
            break

    if correct:
        for c in range(0, len(arranger)):
            print(f'{arranger[c]["n1"]:>9} ', end='   ')
        print()
        for c in range(0, len(arranger)):
            print(f'{arranger[c]["operator"]}{arranger[c]["n2"]:>8} ', end='   ')
        print()
        for c in range(0, len(arranger)):
            print(f'-'*10, end='   ')
        print()
        for c in range(0, len(arranger)):
            print(f'{arranger[c]["result"]:>9} ', end='   ')