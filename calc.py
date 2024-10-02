from tkinter import *
from tkinter import ttk
# можно сделать для сою
# можно сделать также выбор типа заявления и ввести фиксы
# сделать защиту от дурака
def clicked():
    y = x.get()
    y = y.replace(',', ".")
    if not "".join(y.split(".", 1)).isdigit() or y[0] == "-":
        lbl.configure(text=f'''Ошибка. Вы ввели не число, либо ввели отрицательное число. 
Попробуйте снова''',foreground="#B71C1C")
    else:
        y = float(y)
        if y == 0:
            lbl.configure(text=f'''Цена иска не может быть 0 рублей.
Возможно вы ошиблись при вводе суммы,
либо ваш иск не подлежит оценке - проверьте ваше требование''',foreground="#B71C1C")
        else: 
            y = int(y + 0.5)
            if y < 100001:
                res = 10000
                formula = "до 100 000 рублей - 10 000 рублей"
            elif y > 1905000000:
                res = 10000000
                formula = f'''свыше 50 000 000 рублей - 725 000 рублей 
плюс 0,5 процента суммы, превышающей 50 000 000 рублей, 
но не более 10 000 000 рублей'''
            elif y < 1000001:
                res = 10000 + 0.05 * (y - 100000)
                formula = f'''от 100 001 рубля до 1 000 000 рублей - 
10 000 рублей плюс 5 процентов суммы, 
превышающей 100 000 рублей'''
            elif y < 10000001:
                res = 55000 + 0.03 * (y - 1000000)
                formula = f'''от 1 000 001 рубля до 10 000 000 рублей - 
55 000 рублей плюс 3 процента суммы, 
превышающей 1 000 000 рублей'''
            elif y < 50000001:
                res = 325000 + 0.01 * (y - 10000000)
                formula = f'''от 10 000 001 рубля до 50 000 000 рублей - 
325 000 рублей плюс 1 процент суммы, 
превышающей 10 000 000 рублей'''
            else:
                res = 725000 + 0.005 * (y - 50000000)
                formula = f'''свыше 50 000 000 рублей - 725 000 рублей 
плюс 0,5 процента суммы, превышающей 50 000 000 рублей, 
но не более 10 000 000 рублей'''
            res = int(res + 0.5)
            if bankrupcy_check == 1:
                res = int(res / 2 + 0.5)
            lbl.configure(text=f'Госпошлина - {res} рублей',foreground="#008000")
            formula_text.configure(text=f'Формула: {formula}')  

  
window = Tk()  
window.title("Калькулятор госпошлины в арб. судах")  
window.geometry('400x180')

txt = Label(window, text="Введите в поле внизу цену иска")
txt.grid(column=0, row=0)

lbl = Label(window, text="Здесь будет рассчитанная госпошлина")  
lbl.grid(column=0, row=6)  

formula_text = Label(window, text="Здесь будет формула расчета")
formula_text.grid(column=0, row=5)

x = StringVar()
x1 = Entry(master=window, textvariable=x, width=15)
x1.grid(column=0,row=1)

bankrupcy_check = 0
def pull_bankrupcy():
    global bankrupcy_check
    bankrupcy_check = enabled.get()

enabled = IntVar()
enabled_checkbutton = ttk.Checkbutton(text="За обособленный спор в деле о банкротстве - 50% от стандартного", variable=enabled, command=pull_bankrupcy)
enabled_checkbutton.grid(column=0, row=3)

btn = Button(window, text="Рассчитать госпошлину", command=clicked)  
btn.grid(column=0, row=4)  

window.mainloop()
