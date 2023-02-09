
import tkinter as tk

def convert():
    try:
        rate = float(entry_rate.get())
        usd = float(entry_usd.get())
        result = rate * usd
        label_result.config(text="Amount in local currency: " + str(result))
    except ValueError:
        label_result.config(text="Invalid input, please enter a number.")

root = tk.Tk()
root.title("Currency Converter")

frame_input = tk.Frame(root)
frame_input.pack()

label_rate = tk.Label(frame_input, text="Exchange rate:")
label_rate.grid(row=0, column=0, padx=5, pady=5)

entry_rate = tk.Entry(frame_input)
entry_rate.grid(row=0, column=1, padx=5, pady=5)

label_usd = tk.Label(frame_input, text="Amount in USD:")
label_usd.grid(row=1, column=0, padx=5, pady=5)

entry_usd = tk.Entry(frame_input)
entry_usd.grid(row=1, column=1, padx=5, pady=5)

frame_result = tk.Frame(root)
frame_result.pack()

label_result = tk.Label(frame_result)
label_result.pack(padx=5, pady=5)

button_convert = tk.Button(root, text="Convert", command=convert)
button_convert.pack(pady=5)

root.mainloop()
