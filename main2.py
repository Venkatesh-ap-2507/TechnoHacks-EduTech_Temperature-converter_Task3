import tkinter as tk

def convert_to_celsius():
    fahrenheit = float(entry.get())
    celsius = (fahrenheit - 32) * 5/9
    result_label.config(text=f"{celsius:.2f} °C")

def convert_to_fahrenheit():
    celsius = float(entry.get())
    fahrenheit = celsius * 9/5 + 32
    result_label.config(text=f"{fahrenheit:.2f} °F")

window = tk.Tk()
window.title("Temperature Converter")

entry_label = tk.Label(window, text="Temperature:")
entry_label.pack()

entry = tk.Entry(window)
entry.pack()

to_celsius_button = tk.Button(window, text="Convert to Celsius", command=convert_to_celsius)
to_celsius_button.pack()

to_fahrenheit_button = tk.Button(window, text="Convert to Fahrenheit", command=convert_to_fahrenheit)
to_fahrenheit_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()
