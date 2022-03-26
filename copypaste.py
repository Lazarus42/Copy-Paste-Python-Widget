from tkinter import Tk
import pandas as pd
import keyboard
from pynput import keyboard

###Copying in some code to get this to run. Will need to change these functions
###Later on, though

####CURRENT ISSUE: The curr_queue is not getting updated after the call to
#### add_to_queue
###Going to check if it has the ability to actually update the queue on its
###Own though
def on_activate_copy():
    #print('<cmd>+<c>+h pressed')
    #print(curr_queue)
    #add_to_queue(curr_queue, max_len, prev_copied)
    #print(curr_queue)
    curr_queue = curr_queue + ["Michael Spencer Jordan"]

def on_activate_paste_1():
    #print('<ctrl>+<alt>+i pressed')
    print("You have tried to paste the first entry in the queue")
    print(curr_queue)
    paste_from_queue(curr_queue, 1)

def on_activate_paste_2():
    #print('<ctrl>+<alt>+i pressed')
    paste_from_queue(curr_queue, 2)

def on_activate_paste_3():
    #print('<ctrl>+<alt>+i pressed')
    paste_from_queue(curr_queue, 3)

def on_activate_paste_4():
    #print('<ctrl>+<alt>+i pressed')
    paste_from_queue(curr_queue, 4)

def on_activate_paste_5():
    #print('<ctrl>+<alt>+i pressed')
    paste_from_queue(curr_queue, 5)

def on_release():
    return False

###Rough outline -- You can keep up to 5 things copied.
#curr_queue = [Tk().clipboard_get()]
#max_len = 5
#prev_copied = Tk().clipboard_get()
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
    print("The new currqueue is from add_to_queue is", curr_queue)
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

###The program should continuously run in the background and check if new
###Things have been copied without taking up too much computing power
###Now to do: Get this running at all times in the background --  DONE
###To do: Current issue: Not actually adding anything to the queue
def main():
    # global curr_queue
    # global max_len
    # global prev_copied
    # curr_queue = [Tk().clipboard_get()]
    # print(curr_queue, "printing the initial curr_queue")
    # max_len = 5
    # prev_copied = Tk().clipboard_get()
    ###Now start listening
    with keyboard.GlobalHotKeys({
            '<cmd>+c': on_activate_copy,
            '<ctrl>+v+q': on_activate_paste_1,
            '<ctrl>+v+w': on_activate_paste_2,
            '<ctrl>+v+e': on_activate_paste_3,
            '<ctrl>+v+r': on_activate_paste_4,
            '<ctrl>+v+t': on_activate_paste_5,
            '<esc>': on_release}) as h:
        h.join()

if __name__ == "__main__":
    global curr_queue
    global max_len
    global prev_copied
    curr_queue = [Tk().clipboard_get()]
    #print(curr_queue, "printing the initial curr_queue")
    max_len = 5
    prev_copied = Tk().clipboard_get()
    main()
