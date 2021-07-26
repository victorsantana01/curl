from tkinter import *
from Rum import Teste

janela = Tk()
janela.geometry('300x300')
janela.title('Bot Autotrac')
def click():
    print('Teste')
bt = Button(janela, width=20, text='Start', command= lambda: Teste.ok("OK   ") )
bt.pack()

janela.mainloop()
