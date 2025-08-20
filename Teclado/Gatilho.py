import keyboard
import time


Confirmacao = input("deseja começar? s/n")

def parar_func():
     print("Opereção parada!")
     keyboard.wait('esc')

keyboard.add_hotkey('esc',parar_func)

if Confirmacao == "s":
    keyboard.press_and_release('win+r')
    keyboard.send('c')
    keyboard.send('l')
    keyboard.send('e')
    keyboard.send('a')
    keyboard.send('n')
    keyboard.send('m')
    keyboard.send('g')
    keyboard.send('r')
    keyboard.send('enter')
    time.sleep(1)
    keyboard.send('enter')
    time.sleep(1)
    keyboard.send('enter')
    time.sleep(1)
    keyboard.send('enter')
    time.sleep(40)
    keyboard.press_and_release('win+r')
    keyboard.send

elif Confirmacao == "n":
     print ('Cancelando operação')
