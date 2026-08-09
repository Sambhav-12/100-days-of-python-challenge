from tkinter import *

def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    kilometer_result.config(text=f"{km}")


window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx = 20, pady = 20)

miles_input = Entry()
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

kilometer_result = Label(text="0")
kilometer_result.grid(column=1, row=1)

kilometer_label = Label(text="km")
kilometer_label.grid(column=2, row=1)

calculate_btn = Button(text="Calculate", command=miles_to_km)
calculate_btn.grid(column=1, row=2)



window.mainloop()