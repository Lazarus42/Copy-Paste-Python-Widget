from tkinter import Tk
import pandas as pd
import keyboard

###Rough outline -- You can keep up to 5 things copied.
curr_queue = [Tk().clipboard_get()]
max_len = 5
prev_copied = Tk().clipboard_get()
###If you add sometThe Death of Democracy: Hitler's Rise to Power and the Downfall of the Weimar Republicclipboard, then you should add it to the front
###Of the queue. If there are too many items in the queue, remove the last item
###Before adding the new copied text
def add_to_queue(curr_queue, max_len, prev_copied):
    copied_Text = Tk().clipboard_get()
    if copied_Text == prev_copied:
        return curr_queue
    if len(curr_queue) > max_len:
        curr_queue = [copied_Text] + curr_queue[:4]
        return curr_queue
    curr_queue = [copied_Text] + curr_queue
    return curr_queue

###This function pastes what you copied in a certain position
###It will use pandas to do this
###One issue: This currently has an additional /n at the end
def paste_from_queue(curr_queue, pos):
    ###Check that the position is valid
    if pos < 0 or pos >= len(curr_queue):
        return
    df = pd.DataFrame([curr_queue[pos]])
    df.to_clipboard(index = False, header = False)
    return

#paste_from_queue(curr_queue, 1)
#print(Tk().clipboard_get() == "HI\n")
#print(curr_queue[1])
###The program should continuously run in the background and check if new
###Things have been copied without taking up too much computing power
###Now to do: Get this running at all times in the background
while(True):
    ###I do not need to check if you tried to copy something, but rather, if
    ###You tried to paste something
    if (keyboard.is_pressed('shift + c')):
        add_to_queue(curr_queue, max_len, prev_copied)
        prev_copied = Tk().clipboard_get()
    for i in range(max_len):
        if keyboard.is_pressed('shift + v + ' + str(i)):
            paste_from_queue(curr_queue, i)
