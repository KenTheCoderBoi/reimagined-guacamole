from tkinter import *

root=Tk()
root.title("mexico")
root.geometry("600x600")

imput = Entry(root)
imput.pack()
def run():
    num=5
    inputnum=imput.get()
    try:
        print(num+inputnum)
    except (TypeError):
        print("convert num to a string")
    


btn= Button(root,text="amogus",command=run)
btn.pack()

root.mainloop()