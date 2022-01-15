import tkinter as tk

from models.airplane_model import Airplane
from storage import Storage
from windows.add_window import AddWindow

storage = Storage()
storage.checkWS()

#
# Main window
#

mainWindow = tk.Tk()
mainWindow.title('Air Transportation')
mainWindow.geometry('320x420')

#
# Самолет
#
addWindow = AddWindow(mainWindow)
frm_airplane = tk.Frame(mainWindow).pack(fill=tk.BOTH)
lbl_airplane_title = tk.Label(frm_airplane, text='Самолет', pady=10).pack(fill=tk.X)
btn_airplane = tk.Button(frm_airplane, text='Добавить', command=addWindow.show).pack(fill=tk.X)

#
# Груз
#

frm_cargo = tk.Frame(mainWindow).pack(fill=tk.BOTH)
lbl_cargo_title = tk.Label(frm_cargo, text='Груз', pady=10).pack(fill=tk.X)
btn_cargo = tk.Button(frm_cargo, text='Добавить').pack(fill=tk.X)

#
# Заказчик
#

frm_customer = tk.Frame(mainWindow).pack(fill=tk.BOTH)
lbl_customer_title = tk.Label(frm_customer, text='Заказчик', pady=10).pack(fill=tk.X)
btn_customer = tk.Button(frm_customer, text='Добавить').pack(fill=tk.X)

#
# Маршрут
#

frm_route = tk.Frame(mainWindow).pack(fill=tk.BOTH)
lbl_route_title = tk.Label(frm_route, text='Маршрут', pady=10).pack(fill=tk.X)
btn_route = tk.Button(frm_route, text='Добавить').pack(fill=tk.X)

#
# Заказ
#

frm_order = tk.Frame(mainWindow).pack(fill=tk.BOTH)
lbl_order_title = tk.Label(frm_order, text='Заказ', pady=10).pack(fill=tk.X)
btn_order = tk.Button(frm_order, text='Добавить', height=3).pack(fill=tk.X)


# ---------------------
mainWindow.mainloop()
