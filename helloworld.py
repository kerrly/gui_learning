import tkinter
root = tkinter.Tk()

root.title("Hello World!!!")
root.geometry("600x200")

my_label = tkinter.Label(root)
my_label.config(text= "Hello dickhead!!", fg="blue")
my_label.grid()

my_label2 = tkinter.Label(root)
my_label2.config(text= "sup bro", fg="orange")
my_label2.grid()

my_label3 = tkinter.Label(root)
my_label3.config(txt= "yeaa nahhh", fg="red")
my_label3.grid()

root.mainloop()