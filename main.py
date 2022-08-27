import tkinter as tk

calculation = ""

def add_to(symbol):
    global calculation
    calculation += str(symbol)
    text.delete(1.0 , "end")
    text.insert(1.0 , calculation)

def evaluate_funtion():
    global calculation
    try:
        calculation = str(eval(calculation))
        text.delete(1.0 , "end")
        text.insert(1.0 , calculation)
    except:
        clear_funtion()
        text.insert(1.0 , "Error")

def clear_funtion():
    global calculation
    calculation = ""
    text.delete(1.0 , "end")

root = tk.Tk()
root.geometry("310x280")

text = tk.Text(root, height=2 , width=17 , font=("Arial" , 24))
text.grid(columnspan=6)

btn1 = tk.Button(root, text="1", command=lambda: add_to(1), width=5, font=("Arial" , 14))
btn1.grid(row=2 , column=1)
btn2 = tk.Button(root, text="2", command=lambda: add_to(2), width=5, font=("Arial" , 14))
btn2.grid(row=2 , column=2)
btn3 = tk.Button(root, text="3", command=lambda: add_to(3), width=5, font=("Arial" , 14))
btn3.grid(row=2 , column=3)
btn4 = tk.Button(root, text="4", command=lambda: add_to(4), width=5, font=("Arial" , 14))
btn4.grid(row=3 , column=1)
btn5 = tk.Button(root, text="5", command=lambda: add_to(5), width=5, font=("Arial" , 14))
btn5.grid(row=3 , column=2)
btn6 = tk.Button(root, text="6", command=lambda: add_to(6), width=5, font=("Arial" , 14))
btn6.grid(row=3 , column=3)
btn7 = tk.Button(root, text="7", command=lambda: add_to(7), width=5, font=("Arial" , 14))
btn7.grid(row=4 , column=1)
btn8 = tk.Button(root, text="8", command=lambda: add_to(8), width=5, font=("Arial" , 14))
btn8.grid(row=4 , column=2)
btn9 = tk.Button(root, text="9", command=lambda: add_to(9), width=5, font=("Arial" , 14))
btn9.grid(row=4 , column=3)
btn0 = tk.Button(root, text="0", command=lambda: add_to(0), width=5, font=("Arial" , 14))
btn0.grid(row=5 , column=2)

btnplus = tk.Button(root, text="+", command=lambda: add_to("+"), width=5, font=("Arial" , 14))
btnplus.grid(row=2 , column=4)
btnminus = tk.Button(root, text="-", command=lambda: add_to("-"), width=5, font=("Arial" , 14))
btnminus.grid(row=3 , column=4)
btntimes = tk.Button(root, text="x", command=lambda: add_to("*"), width=5, font=("Arial" , 14))
btntimes.grid(row=4 , column=4)
btndvied = tk.Button(root, text="/", command=lambda: add_to("/"), width=5, font=("Arial" , 14))
btndvied.grid(row=5 , column=4)

btnopen = tk.Button(root, text="(", command=lambda: add_to("("), width=5, font=("Arial" , 14))
btnopen.grid(row=5 , column=1)
btnclosed = tk.Button(root, text=")", command=lambda: add_to(")"), width=5, font=("Arial" , 14))
btnclosed.grid(row=5 , column=3)

btncl = tk.Button(root, text="Clear", command=clear_funtion, width=13, font=("Arial" , 14))
btncl.grid(row=6 , column=1, columnspan=2)

btneq = tk.Button(root, text="=", command=evaluate_funtion, width=13, font=("Arial" , 14))
btneq.grid(row=6 , column=3, columnspan=2)

root.mainloop()