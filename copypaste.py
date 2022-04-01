from pynput import keyboard
import sys
from pyperclip import copy, paste
from time import sleep

class React_to_Keyboard():
    def __init__(self):
        self.curr_queue = [paste()]
        self.max_len = 5
        self.prev_copied = paste()

    def on_activate_copy(self):
        sleep(.01)
        (self.curr_queue, self.prev_copied) = add_to_queue(self.curr_queue, self.max_len, self.prev_copied)

    def on_activate_paste_1(self):
        paste_from_queue(self.curr_queue, 0)

    def on_activate_paste_2(self):
        paste_from_queue(self.curr_queue, 1)

    def on_activate_paste_3(self):
        paste_from_queue(self.curr_queue, 2)

    def on_activate_paste_4(self):
        paste_from_queue(self.curr_queue, 3)

    def on_activate_paste_5(self):
        paste_from_queue(self.curr_queue, 4)

    def on_release(self):
        self.curr_queue = []
        raise sys.exit(1)

###Rough outline -- You can keep up to 5 things copied.
###If you add sometThe Death of Democracy: Hitler's Rise to Power and the Downfall of the Weimar Republicclipboard, then you should add it to the front
###Of the queue. If there are too many items in the queue, remove the last item
###Before adding the new copied text
def add_to_queue(curr_queue, max_len, prev_copied):
    copied_Text = paste()
    if copied_Text == prev_copied:
        return (curr_queue, prev_copied)
    if len(curr_queue) > max_len:
        curr_queue = [copied_Text] + curr_queue[:4]
        return (curr_queue, copied_Text)
    curr_queue = [copied_Text] + curr_queue
    return (curr_queue, copied_Text)

###This function pastes what you copied in a certain position
###It will use pandas to do this
def paste_from_queue(curr_queue, pos):
    ###Check that the position is valid
    if pos < 0 or pos >= len(curr_queue):
        return
    copy(curr_queue[pos])
    return

###The program should continuously run in the background and check if new
###Things have been copied without taking up too much computing power
def main():
    react = React_to_Keyboard()
    with keyboard.GlobalHotKeys({
            '<cmd>+c': react.on_activate_copy,
            '<ctrl>+v+q': react.on_activate_paste_1,
            '<ctrl>+v+w': react.on_activate_paste_2,
            '<ctrl>+v+e': react.on_activate_paste_3,
            '<ctrl>+v+r': react.on_activate_paste_4,
            '<ctrl>+v+t': react.on_activate_paste_5,
            '<ctrl>+j': react.on_release}) as h:
        h.join()

if __name__ == "__main__":
    main()
