import tkinter as tk

def run_gui(detect_function):
    root = tk.Tk()
    root.title("Hawking Chair Interface")

    label = tk.Label(root, text="Welcome to Hawking Chair Interface")
    label.pack()

    start_button = tk.Button(root, text="Start Detection", command=detect_function)
    start_button.pack()

    exit_button = tk.Button(root, text="Exit", command=root.quit)
    exit_button.pack()

    root.mainloop()
