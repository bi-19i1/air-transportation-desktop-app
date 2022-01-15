from tkinter import BOTH, LEFT, Entry, Frame, Label, Tk, Toplevel, X


class AddWindow():
  def __init__(self, mainWindow: Tk) -> None:
      self._mainWindow = mainWindow

  def show(self):
    # window = Toplevel(self._mainWindow)
    # window.geometry('240x300')
    # mainFrame = Frame(window).grid(column=0, row=0).pack(fill=BOTH)

    # lbl = Label(mainFrame, text='123', width=10)
    # lbl.pack()

    # entry = Entry(mainFrame)
    # entry.pack()
    win = Toplevel(self._mainWindow)
    f1 = Frame(win)
    f1.grid(row=0, column=0)
    f2 = Frame(win)
    f2.grid(row=1, column=1)
    Label(f1, text="FRAME 1").grid()
    Label(f2, text="FRAME 2").grid()
