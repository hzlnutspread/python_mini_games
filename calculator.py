from tkinter import *


def button_press(num):
    global equation_text
    equation_text = equation_text + str(num)
    equation_label.set(equation_text)


def equals():
    global equation_text

    try:
        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text = total
    except ZeroDivisionError:
        equation_label.set("Can't divide by 0, dumbass")
        equation_text = ""
    except SyntaxError:
        equation_label.set("Syntax error")
        equation_text = ""


def clear():
    global equation_text
    equation_label.set("")
    equation_text = ""


window = Tk()
window.title("Calculator Program")
window.geometry("500x500")

equation_text = ""

equation_label = StringVar()

label = Label(window, textvariable=equation_label,
              font=("consolas", 15),
              bg="beige",
              width=32,
              height=2,
              relief=GROOVE,
              borderwidth=1,
              padx=2,
              pady=2)
label.pack()

frame = Frame(window)
frame.pack()

button1 = Button(frame, text=1, height=4, width=9, font=35,
                 command=lambda: button_press(1),
                 bg="light blue")
button1.grid(row=0, column=0)

button2 = Button(frame, text=2, height=4, width=9, font=35,
                 command=lambda: button_press(2),
                 bg="light blue")
button2.grid(row=0, column=1)

button3 = Button(frame, text=3, height=4, width=9, font=35,
                 command=lambda: button_press(3),
                 bg="light blue")
button3.grid(row=0, column=2)

button4 = Button(frame, text=4, height=4, width=9, font=35,
                 command=lambda: button_press(4),
                 bg="light blue")
button4.grid(row=1, column=0)

button5 = Button(frame, text=5, height=4, width=9, font=35,
                 command=lambda: button_press(5),
                 bg="light blue")
button5.grid(row=1, column=1)

button6 = Button(frame, text=6, height=4, width=9, font=35,
                 command=lambda: button_press(6),
                 bg="light blue")
button6.grid(row=1, column=2)

button7 = Button(frame, text=7, height=4, width=9, font=35,
                 command=lambda: button_press(7),
                 bg="light blue")
button7.grid(row=2, column=0)

button8 = Button(frame, text=8, height=4, width=9, font=35,
                 command=lambda: button_press(8),
                 bg="light blue")
button8.grid(row=2, column=1)

button9 = Button(frame, text=9, height=4, width=9, font=35,
                 command=lambda: button_press(9),
                 bg="light blue")
button9.grid(row=2, column=2)

button0 = Button(frame, text=0, height=4, width=9, font=35,
                 command=lambda: button_press(0),
                 bg="light blue")
button0.grid(row=3, column=0)

plus = Button(frame, text="+", height=4, width=9, font=35,
              command=lambda: button_press("+"),
              bg="pink")
plus.grid(row=0, column=3)

minus = Button(frame, text="-", height=4, width=9, font=35,
               command=lambda: button_press("-"),
               bg="pink")
minus.grid(row=1, column=3)

multiply = Button(frame, text="*", height=4, width=9, font=35,
                  command=lambda: button_press("*"),
                  bg="pink")
multiply.grid(row=2, column=3)

divide = Button(frame, text="/", height=4, width=9, font=35,
                command=lambda: button_press("/"),
                bg="pink")
divide.grid(row=3, column=3)

equal = Button(frame, text="=", height=4, width=9, font=35,
               command=equals,
               bg="green")
equal.grid(row=3, column=2)

decimal = Button(frame, text=".", height=4, width=9, font=35,
                 command=lambda: button_press("."),
                 bg="light blue")
decimal.grid(row=3, column=1)

clear = Button(window, text="ac", height=4, width=12, font=35,
               command=clear,
               bg="red")
clear.pack()

window.mainloop()
