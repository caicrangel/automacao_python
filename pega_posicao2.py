#pegando as coordenadas X e Y do mouse em tempo real

import pyautogui, sys
print('Press Ctrl-C to quit.')
try:
    while True:
        x, y = pyautogui.position()
        positionStr = f'X:{str(x).rjust(4)} Y:{str(y).rjust(4)}'
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\n')