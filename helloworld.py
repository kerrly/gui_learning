import tkinter
root = tkinter.Tk()

root.title("Hello World!!!")
root.geometry("600x200")

my_label = tkinter.Label(root)
my_label.config(text= "R U Real??!!", fg="blue", bg="violet", font=("Times", "100"))
my_label.grid()

my_label2 = tkinter.Label(root)
my_label2.config(text= "ooft", fg="orange", bg="hot pink", font=("Bookman", "50"), padx="20")
my_label2.grid()

my_label3 = tkinter.Label(root)
my_label3.config(text= "ruelle", fg="pink", bg="green", font=("Garamond", "80"))
my_label3.grid()


root.mainloop()