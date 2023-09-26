import pyautogui

bd_passwords = [1234,654321]


for i in bd_passwords:
    while True:
        try:
            password = int(pyautogui.password(text='DIGITE A SENHA PARA ENTRAR NA CALCULADORA', title='', default='', mask='*'))
        except ValueError:
            op = pyautogui.confirm(text='SENHA INCORRETA!!!\nDESEJA CONTINUAR?', title='', buttons=['SIM', 'NAO'])
            if op == 'SIM':
                continue
            else:
                exit()         
        
        if password == i:

            while True:
                try:
                    op = int(pyautogui.prompt(text='Escolha a operação a fazer:\n1-ADIÇÃO\n2-SUBTRAÇÃO\n3-MULTIPLICAÇÃO\n4-DIVISÃO', title='CALCULADORA' , default=''))
                
                    if (op <=0) or (op >=5):
                        pyautogui.alert(text='ERRO!!!\nESCOLHA AS OPÇÕES DISPONÍVEIS.', button='OK')
                        continue

                    num1 = float(pyautogui.prompt(text='DIGITE O PRIMEIRO NUMERO:', default=''))
                    num2 = float(pyautogui.prompt(text='DIGITE O SEGUNDO NUMERO:', default=''))
                except ValueError:
                    pyautogui.alert(text='ERRO!!!\nVALOR INCORRETO.', button='OK')
                    continue

                if op == 1:
                    calc = num1 + num2
                elif op == 2:
                    calc = num1 - num2
                elif op == 3:
                    calc = num1 * num2
                elif op == 4:
                    try:
                        calc = num1 / num2
                    except ZeroDivisionError:
                        pyautogui.alert(text=f'ERRO!!!\nNÃO É POSSÍVEL DIVIDIR POR ZERO.', button='OK')
                        continue

                pyautogui.alert(text=f'RESULTADO = {calc}', button='OK')

                op = pyautogui.confirm(text='DESEJA CONTINUAR?', title='', buttons=['SIM', 'NAO'])
                if op == 'SIM':
                    continue
                else:
                    exit()
        else:
            op = pyautogui.confirm(text='SENHA INCORRETA!!!\nDESEJA CONTINUAR?', title='', buttons=['SIM', 'NAO'])
            if op == 'SIM':
                continue
            else:
                exit()         



