import tkinter as tk
import ttkbootstrap as ttk

def convert():
    miles = entryInt.get()
    kilometers = miles * 1.61
    output_label.set(f"{miles} M = {kilometers:.2f} Km")

window = ttk.Window(themename="journal")
window.title('DEMO')

title_label = ttk.Label(master=window, text="Mile to Kilometers", font="Calibri 24 bold")
title_label.pack()

input_frame = ttk.Frame(master=window)
entryInt = tk.IntVar()
entry = ttk.Entry(master=input_frame, textvariable=entryInt)
input_button = ttk.Button(master=input_frame, text="convert", command=convert)
entry.pack(side="left", padx=10)
input_button.pack(side="left")
input_frame.pack(pady=10)

output_label = tk.StringVar()
output = ttk.Label(master=window, text="text", font="Calibri 24 ", textvariable=output_label)
output.pack(pady=5)

# Calculate the required size of the window
window.update_idletasks()
window_width = window.winfo_reqwidth()
window_height = window.winfo_reqheight()

# Center the window on the screen
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x_coordinate = (screen_width / 2) - (window_width / 2)
y_coordinate = (screen_height / 2) - (window_height / 2)

# Set the window size and position
window.geometry(f"500x250+{int(x_coordinate)}+{int(y_coordinate)}")

window.mainloop()
