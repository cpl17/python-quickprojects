from tkinter import *
from math import floor 
import time


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1/60
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0 
timer = None

def convert(n):
    return time.strftime("%M:%S", time.gmtime(n))



# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():

    # Reset timer 
    window.after_cancel(timer)

    # Reset time
    time = convert(0)
    canvas.itemconfig(timer_text, text = time)

    # Update label 

    timer_label.config(text = "Timer", fg = GREEN)

    # Reset checkmarks 

    check.config(text = "")

    # Update reps 

    global reps 
    reps = 0



# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    
    global reps 

    reps += 1


    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:

        count_down(long_break_sec)
        timer_label.config(text= "Break", fg = RED)
        
    elif reps % 2 == 0:
        
        count_down(short_break_sec)
        timer_label.config(text= "Break", fg = PINK)
    
    else:
        count_down(work_sec)
        timer_label.config(text= "Work", fg = GREEN)

        

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):

    time = convert(count)
    canvas.itemconfig(timer_text, text = time)
    if count > 0:
        global timer
        timer = window.after(1000,count_down, count -1)
    else:
        start_timer()
        if reps % 2 == 0:
            check.config(text = "✔" * (reps // 2))


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx = 100, pady = 50, bg = YELLOW)



# Tomato

canvas = Canvas(width=200, height = 224, bg = YELLOW, highlightthickness = 0)
img = PhotoImage(file = "tomato.png")
canvas.create_image(100,112, image = img )
timer_text = canvas.create_text(103,130, text = "00:00", fill = 'white', font = (FONT_NAME, 35, "bold"))
canvas.grid(row = 1, column = 1)


# Timer label 

timer_label = Label(text="Timer",bg = YELLOW, fg = GREEN, font = ((FONT_NAME, 50, "bold")))
timer_label.grid(row = 0, column = 1)


# Start and stop buttons 

start_button = Button(text="Start", command=start_timer,highlightthickness = 0)
start_button.grid(row = 2, column = 0)

stop_button = Button(text="Reset", command=reset_timer,highlightthickness = 0)
stop_button.grid(row = 2, column = 2)


# Checkmarks 


check = Label(bg = YELLOW, fg = GREEN )
check.grid(row = 3, column = 1)














window.mainloop()

