import tkinter as tk

# Create a window
window = tk.Tk()

# Add a label to the window
label = tk.Label(text="Hello, world!")
label.pack()

# Add a button to the window
button = tk.Button(text="Click me!", command=window.destroy)
button.pack()

# Run the program
window.mainloop()
