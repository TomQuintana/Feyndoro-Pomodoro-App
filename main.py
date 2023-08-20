import tkinter
import math
# pyright: reportMissingImports=false
from services.quotes_Feynman import quotes


YELLOW = "#f7f5dd"
reps = 0
PINK = "#e2979c"
RED = "#e7305b"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
timer = None

#TODO: cambiar el tamanio de la imagen
#TODO: ver de pasar las funciones al archivo de timer

def reset_timer():

    window.after_cancel(timer)

    canvas.itemconfigure(timer_text, text="00:00")

    title_label.config(text="Only through hard work can you discover something")
    check_marks.config(text="")

    quotes_feynman = tkinter.Label(text="", bg="#CEE6F3", font=("Courier", 15, "bold"))
    quotes_feynman.grid(column=1, row=2)

    global reps
    reps = 0

def start_timer():

    global reps
    reps += 1
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        title_label.config(text="Long Break", fg="white")
        window.attributes('-topmost', 1)
        window.bell()

    elif reps % 2 == 1:
        count_down(WORK_MIN )
        title_label.config(text="Only through hard work can you discover something", fg="white", font=("Mono", 20, "bold"), bg="#BEADFA")
        window.attributes('-topmost', 0)
        window.bell()

    else:
        count_down(SHORT_BREAK_MIN ) 
        title_label.config(text="Break", fg="white")
        window.attributes('-topmost', 1)
        window.bell()


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec == 0:
        count_sec = "00"

    elif count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfigure(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer 
        timer = window.after(1000, count_down, count - 1)
    else: 
        start_timer()
        text_quotes = quotes()

        quotes_feynman = tkinter.Label(text=text_quotes, bg="#CEE6F3", font=("Courier", 15, "bold"))
        quotes_feynman.grid(column=1, row=2)

        marks = ""
        for _ in range(math.floor(reps/2)):
            marks += "✅"
            check_marks.config(text=marks)


window = tkinter.Tk()
window.title('Feyndoro')
window.config(padx=100, pady=50, bg="#CEE6F3")

canvas = tkinter.Canvas(width=380, height=224, bg="#CEE6F3", highlightthickness=0)

feynman_img = tkinter.PhotoImage(file="richard.png")
canvas.create_image(191, 112, image=feynman_img)

timer_text = canvas.create_text(190, 130, text="00:00", fill="white", font=("Courier", 35, "bold"))
canvas.grid(column=1, row=1)

title_label = tkinter.Label(text="Only through hard work can you discover something", fg="white", font=("Mono", 25, "bold"), bg="#BEADFA", justify="center")
title_label.grid(column=1, row=0)

check_marks = tkinter.Label( bg="#CEE6F3")
check_marks.grid(column=1, row=3)

start_button = tkinter.Button(text="Start", command=start_timer, font=("Mono", 20, "bold"), fg="#279EFF", justify="center")
start_button.config(padx=8, pady=8)
start_button.grid(column=1, row=4)

# reset_button = tkinter.Button(text="Reset", command=reset_timer)
# reset_button.grid(column=1, row=5)

print(reps)

window.mainloop()
