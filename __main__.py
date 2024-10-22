#!/usr/bin/python3
import math
import tkinter as tk

ans = ''

MATH_NAMES = {
    k: v for k, v in math.__dict__.items() if not k.startswith("__")
}
CUSTOM_NAMES = {}
ALLOWED_NAMES = {**MATH_NAMES, **CUSTOM_NAMES}
SYMBOLS_TO_EXPRESSIONS = {'×': '*', '÷': '/', '√': 'sqrt', '𝛑': 'pi', '²': '**2'}

def evaluate(expression):
    """Evaluate a math expression."""
    # Compile the expression
    try:
        code = compile(expression, "<string>", "eval")
    except:
        return 'Syntax Error'

    # Validate allowed names
    for name in code.co_names:
        if name not in ALLOWED_NAMES:
            raise NameError(f"The use of '{name}' is not allowed")
    try:
        return eval(code, {"__builtins__": {}}, ALLOWED_NAMES)
    except:
        return 'Math Error'
def calculate():
    global ans
    calc = calcbox['text'].lower()
    calc = list(calc)
    #     for item in calc:
    #         if item == 'N' or item == 'S':
    #             del calc[calc.index(item)]
    #         else:
    #             print(calc[calc.index(item)])
    for item in calc:
        try:
            calc[calc.index(item)] = SYMBOLS_TO_EXPRESSIONS[item]
        except:
            pass
    calc = ''.join(calc)
    ansbox['text'] = str(evaluate(calc))
    ans = str(evaluate(calc))
    
def add_char(char):
    print(char)
    if ansbox['text'] == '':
        if len(calcbox['text']) > 0:
            try:
                if char in specials and int(calcbox['text'][-1]) in list(range(10)):
                    calcbox['text'] += '×' + char
                else:
                    calcbox['text'] += char
            except ValueError:
                calcbox['text'] += char
        else:
            calcbox['text'] = char
            
    else:
        calcbox['text'] = ''
        if char in operators and len(calcbox['text']) == 0:
            calcbox['text'] = ansbox['text'] + char
        else:
            calcbox['text'] = char
        ansbox['text'] = ''
def clear():
    calcbox['text'] = ''
    ansbox['text'] = ''
def del_one():
    if calcbox['text'][-2] == '√':
        calcbox['text'] = calcbox['text'][:-2]
    elif calcbox['text'][-1] == 'S':
        calcbox['text'] = calcbox['text'][-3]
    else:
        calcbox['text'] = calcbox['text'][:-1]
    ansbox['text'] = ''
specials = ['(', '√(', '𝛑']
operators = ['÷', '×', '-', '+', '²']
nums = [[7,8,9, '÷', '('],[4,5,6, '×', ')'],[1,2,3, '-', ''],[0, '.', '√(', '+', '']]
flat_nums = [str(item) for sublist in nums for item in sublist]
root = tk.Tk()
root.title('PyCalc')
calcbox = tk.Label(bg='white', width=21, height=1, anchor='w', font=('Arial', 15))
calcbox.pack()
ansbox = tk.Label(bg='white', width=21, height=1, anchor='e', font=('Arial', 15))
ansbox.pack()
frame = tk.Frame()
num_buttons = []
for y in range(4):
    for x in range(5):
        button = tk.Button(master=frame, text=str(nums[y][x]), command=lambda char=str(nums[y][x]):(add_char(char)))
        num_buttons.append(button)
        button.grid(row=y, column=x)
for button in num_buttons:
    if button['text'] == '':
        button.grid_forget()
equals = tk.Button(master=frame, text=str('='), command=calculate, height=3)
equals.grid(row=2, column=5, rowspan=2)
ac = tk.Button(master=frame, text=str('AC'), command=clear)
ac.grid(row=0, column=5)
del_btn = tk.Button(master=frame, text=str('DEL'), command=del_one)
del_btn.grid(row=1, column=5)
squared = tk.Button(master=frame, text=str('²'), command=lambda: add_char('²'))
squared.grid(row=2, column=4)
pi = tk.Button(master=frame, text=str('𝛑'), command=lambda: add_char('𝛑'))
pi.grid(row=3, column=4)
frame.pack()

root.mainloop()