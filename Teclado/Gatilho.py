import keyboard


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

elif Confirmacao == "n":
     print ('Cancelando operação')
