import tkinter

window = tkinter.Tk()
window.title("Miles to KM Converter")
window.minsize(width=300, height=100)
km_value = 0

def button_clicked():
    new_text = input.get()
    km_value = int(new_text)*2
    my_label3.config(text=km_value)


input = tkinter.Entry()
input.grid(row=1, column=2)

my_label = tkinter.Label(text="Miles", font=("Arial", 12, "italic"))
my_label.grid(row=1, column=3)

my_label2 = tkinter.Label(text="is equal to", font=("Arial", 12, "italic"))
my_label2.grid(row=2, column=1)

button = tkinter.Button(text="Calculate", command=button_clicked)
button.grid(row=3, column=2)

my_label3 = tkinter.Label(text=km_value, font=("Arial", 12, "italic"))
my_label3.grid(row=2, column=2)

my_label4 = tkinter.Label(text="Km", font=("Arial", 12, "italic"))
my_label4.grid(row=2, column=3)



window.mainloop()


