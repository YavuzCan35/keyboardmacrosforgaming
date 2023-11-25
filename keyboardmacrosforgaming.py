import time
from pynput import keyboard,mouse
from pynput.keyboard import Key, Controller
keyboard1=Controller()
farekontrol=mouse.Controller()
from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener


def on_press(key):
    pass
    #print("Key pressed: {0}".format(key))

def on_release(key):
    """if key == keyboard.Key.esc:
        # Stop listener
        return False"""
    if key==keyboard.KeyCode.from_char('"'):
        keyboard1.tap(Key.enter)
        time.sleep(0.2)
        gn='SHIFT BAS SHIFT'
        keyboard1.type(gn)
        keyboard1.tap(Key.enter)
        print('başarıyla yazıldı')
    if key==keyboard.Key.f1:

        keyboard1.tap(Key.enter)
        time.sleep(0.2)
        gn='adım sesi alan İŞARETLESİN'
        keyboard1.type(gn)
        keyboard1.tap(Key.enter)
    if key==keyboard.Key.f2:

        keyboard1.tap(Key.enter)
        time.sleep(0.2)
        gn='KES'
        keyboard1.type(gn)
        keyboard1.tap(Key.enter)
    if key==keyboard.Key.f3:

        keyboard1.tap(Key.enter)
        time.sleep(0.2)
        gn='Buradalar'
        keyboard1.type(gn)
        keyboard1.tap(Key.enter)
    if key==keyboard.Key.f4:

        keyboard1.tap(Key.enter)
        time.sleep(0.2)
        gn='fake atın atış yapın dönün diğer tarafa'
        keyboard1.type(gn)
        keyboard1.tap(Key.enter)
    if key==keyboard.Key.f5:

        keyboard1.tap(Key.enter)
        time.sleep(0.2)
        gn='laftan da anlamıyorlar'
        keyboard1.type(gn)
        keyboard1.tap(Key.enter)
    if key==keyboard.Key.f6:

        keyboard1.tap(Key.enter)
        time.sleep(0.2)
        gn='ağlaa'
        keyboard1.type(gn)
        keyboard1.tap(Key.enter)
    if key==keyboard.Key.f7:

        keyboard1.tap(Key.enter)
        time.sleep(0.2)
        gn='ARKANDA'
        keyboard1.type(gn)
        keyboard1.tap(Key.enter)
    if key==keyboard.Key.f10:

        keyboard1.tap(Key.enter)
        time.sleep(0.2)
        gn='"=shft f1=admssi f2=ks 3brdlr 4fkeatş 5=anlmyrlr 6=ağl 7arkd'
        keyboard1.type(gn)

def on_move(x, y):
    print("Mouse moved to ({0}, {1})".format(x, y))


def on_click(x, y, button, pressed):
    pass

def on_scroll(x, y, dx, dy):
    print('Mouse scrolled at ({0}, {1})({2}, {3})'.format(x, y, dx, dy))


# Setup the listener threads
keyboard_listener = KeyboardListener(on_press=on_press, on_release=on_release)
#mouse_listener = MouseListener(on_move=on_move, on_click=on_click, on_scroll=on_scroll)

# Start the threads and join them so the script doesn't end early
keyboard_listener.start()
#mouse_listener.start()
keyboard_listener.join()
#mouse_listener.join()
"""keyboard.tap ( Key.enter )
gn ='Aptallar sürüsü'
keyboard.type ( gn )
keyboard.tap ( Key.enter )
keyboard.tap ( Key.enter )"""
print('tamamlandı')
