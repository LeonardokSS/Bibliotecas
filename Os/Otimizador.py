import keyboard
import time

# Espera 1 segundo antes de simular
time.sleep(1)

# Simula o atalho Windows + R
keyboard.press('windows')
keyboard.press_and_release('r')
keyboard.release('windows')