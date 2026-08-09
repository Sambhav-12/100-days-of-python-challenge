from tkinter import *

window = Tk()
window.title("GUI")
window.minsize(width=500, height=500)
def button_clicked():
    print("I got Clicked")
    my_label.config(text=button_clicked, font=("Aria", 24 , "bold"))

# label
my_label = Label(text="YOOOOOOOOO!")
my_label.pack(side = "bottom")

# Button
my_button = Button(text="CLICK!", command=button_clicked)
my_button.config(bg="blue")
my_button.pack()




window.mainloop()