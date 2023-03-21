from tkinter import *

def converter():
    m = int(miles_value.get())
    km_v = m*1.609
    km_value.config(text=f"{km_v}")


window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=200, height=70)
window.config(padx=20, pady=20)

#entry
miles_value = Entry(width=10) 
miles_value.grid(column=1, row=0)

#labels
miles = Label(text="Miles")
equal = Label(text="is equal to")
km_value = Label(text="0")
km = Label(text="Km")
miles.grid(column=2, row=0)
equal.grid(column=0, row=1)
km_value.grid(column=1, row=1)
km.grid(column=2, row=1)

#button
calc = Button(text="Calculate", command=converter)
calc.grid(column=1, row=2)



window.mainloop()